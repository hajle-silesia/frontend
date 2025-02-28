import asyncio
import json
import pathlib

import js
import pyodide.ffi.wrappers

from container import ParametersContainer, RecordsContainer
from object_factory import HTML
from pythonapi import download_file_content, upload_raw_file_content

registry = {}


def register(func):
    registry[func.__name__] = func
    return func


def console(func):
    def wrapper(*args, **kwargs):
        print(f"len args: {len(args)}")  # noqa: T201
        print(f"type: {args[0].type}")  # noqa: T201
        print(f"target: {args[0].target}")  # noqa: T201
        print(f"target.id: {args[0].target.id}")  # noqa: T201
        print(f"target.src: {args[0].target.src}")  # noqa: T201
        print(f"type(target.id): {type(args[0].target.id)}")  # noqa: T201

        func(*args, **kwargs)

    return wrapper


@register
async def activate_tab(_event, element_id):
    for element in js.document.getElementsByClassName("canvas"):
        element.hidden = True
    js.document.getElementById(element_id).hidden = False


@register
def switch(_event, element_id):
    (
        js.document.getElementById(element_id).src,
        js.document.getElementById(element_id).alt,
    ) = (
        js.document.getElementById(element_id).alt,
        js.document.getElementById(element_id).src,
    )


@register
def switch_visibility(_event, element_id):
    if js.document.getElementById(element_id).hidden:
        js.document.getElementById(element_id).hidden = False
    else:
        js.document.getElementById(element_id).hidden = True


@register
async def upload_file_and_show_its_content(event, _element_id):
    upload_response = await upload_file(event)
    if upload_response:
        await show_last_file_content()


async def upload_file(event):
    file_list = event.target.files.to_py()
    for file in file_list:
        file_content = await file.text()
        return await upload_raw_file_content(file_content)


async def show_last_file_content():
    download_response = await download_file_content()
    if download_response:
        recipe_table = js.document.getElementById("recipe_table")
        if recipe_table:
            recipe_table.remove()

        HTML("div", "recipe", {"id": "recipe_table_container"})
        HTML("table", "recipe_table_container", {"id": "recipe_table", "class": "outer"})

        HTML("tr", "recipe_table", {"id": "miscs_fermentables_parameters_headers"})
        HTML("th", "miscs_fermentables_parameters_headers", {"inner_html": "Miscs"})
        HTML("th", "miscs_fermentables_parameters_headers", {"inner_html": "Fermentables"})
        HTML("th", "miscs_fermentables_parameters_headers", {"inner_html": "Parameters"})

        HTML("tr", "recipe_table", {"id": "miscs_fermentables_parameters_values"})
        HTML("td", "miscs_fermentables_parameters_values", {"id": "miscs_container"})
        HTML("td", "miscs_fermentables_parameters_values", {"id": "fermentables_container"})
        HTML(
            "td",
            "miscs_fermentables_parameters_values",
            {"id": "parameters_container", "rowspan": 3},
        )

        HTML("tr", "recipe_table", {"id": "mash_steps_hops_headers"})
        HTML("th", "mash_steps_hops_headers", {"inner_html": "Mash steps"})
        HTML("th", "mash_steps_hops_headers", {"inner_html": "Hops"})

        HTML("tr", "recipe_table", {"id": "mash_steps_hops_values"})
        HTML("td", "mash_steps_hops_values", {"id": "mash_steps_container"})
        HTML("td", "mash_steps_hops_values", {"id": "hops_container"})

        with pathlib.Path("config/table_config.json").open(encoding="utf-8") as table_config_json:  # noqa: ASYNC230
            table_config = json.load(table_config_json)

        miscs_container = RecordsContainer("miscs_container", table_config["miscs"])
        fermentables_container = RecordsContainer("fermentables_container", table_config["fermentables"])
        parameters_container = ParametersContainer("parameters_container", table_config["parameters"])
        mash_steps_container = RecordsContainer("mash_steps_container", table_config["mash_steps"])
        hops_container = RecordsContainer("hops_container", table_config["hops"])

        recipe_tab_containers = [
            miscs_container,
            fermentables_container,
            parameters_container,
            mash_steps_container,
            hops_container,
        ]

        for container in recipe_tab_containers:
            container.update_content(download_response)

        js.document.getElementById("recipe_upload").value = ""


def set_listener(element, event, listener, element_id):
    async def wrapper(event):
        if asyncio.iscoroutinefunction(listener):
            await listener(event, element_id)
        else:
            listener(event, element_id)

    pyodide.ffi.wrappers.add_event_listener(
        element,
        event,
        wrapper,
    )
