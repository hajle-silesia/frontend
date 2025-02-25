import asyncio
import json

import anyio
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

        async with await anyio.open_file("config/table_config.json", encoding="utf-8") as table_config_json:
            table_config = await json.load(table_config_json)

        miscs = RecordsContainer(miscs_container, table_config["miscs"])
        fermentables = RecordsContainer(fermentables_container, table_config["fermentables"])
        parameters = ParametersContainer(parameters_container, table_config["parameters"])
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
