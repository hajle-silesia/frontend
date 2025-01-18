import json

import js
import pyodide.ffi.wrappers
import pyodide.http

from pythonapi import upload_raw_file_content, download_file_content
from container import RecordsContainer, ParametersContainer
from object_factory import HTML


async def upload_file_and_show_its_content(event):
    upload_response = await upload_file(event)
    if upload_response:
        await show_last_file_content()


async def upload_file(event):
    file_list = event.target.files.to_py()
    for file in file_list:
        file_content = await file.text()
        upload_response = await upload_raw_file_content(file_content)
        return upload_response


async def show_last_file_content():
    download_response = await download_file_content()
    if download_response:
        recipe_table = js.document.getElementById("recipe_table")
        if recipe_table:
            recipe_table.remove()

        recipe_tab = js.document.getElementById("recipe")

        recipe_table = HTML("div", recipe_tab, {"id": "recipe_table"})
        table = HTML("table", recipe_table.element, {"class": "outer"})

        row = HTML("tr", table.element)
        HTML("th", row.element, {"inner_html": "Miscs"})
        HTML("th", row.element, {"inner_html": "Fermentables"})
        HTML("th", row.element, {"inner_html": "Parameters"})

        row = HTML("tr", table.element)
        miscs_container = HTML("td", row.element)
        fermentables_container = HTML("td", row.element)
        parameters_container = HTML("td", row.element, {"rowspan": 3})

        row = HTML("tr", table.element)
        HTML("th", row.element, {"inner_html": "Mash steps"})
        HTML("th", row.element, {"inner_html": "Hops"})

        row = HTML("tr", table.element)
        mash_steps_container = HTML("td", row.element)
        hops_container = HTML("td", row.element)

        with open("./config/table_config.json", encoding="utf-8") as table_config_json:
            table_config = json.load(table_config_json)

        miscs = RecordsContainer(miscs_container, table_config["miscs"])
        fermentables = RecordsContainer(
            fermentables_container, table_config["fermentables"]
        )
        parameters = ParametersContainer(
            parameters_container, table_config["parameters"]
        )
        mash_steps = RecordsContainer(mash_steps_container, table_config["mash_steps"])
        hops = RecordsContainer(hops_container, table_config["hops"])

        recipe_tab_containers = [
            miscs,
            fermentables,
            parameters,
            mash_steps,
            hops,
        ]

        for container in recipe_tab_containers:
            container.update_content(download_response)

        js.document.getElementById("recipe_upload").value = ""


async def create_recipe():
    recipe_tab = HTML("div", None, {"id": "recipe", "class": "canvas"})

    upload_container = HTML("div", recipe_tab.element)
    recipe_upload = HTML(
        "input",
        upload_container.element,
        {
            "id": "recipe_upload",
            "type": "file",
        },
    )
    HTML(
        "label",
        upload_container.element,
        {
            "id": "label_recipe_upload",
            "html_for": "recipe_upload",
            "inner_html": "Upload recipe &#129045;",
        },
    )
    await show_last_file_content()
    pyodide.ffi.wrappers.add_event_listener(
        recipe_upload.element, "change", upload_file_and_show_its_content
    )
