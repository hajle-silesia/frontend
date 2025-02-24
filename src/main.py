import asyncio

import js

import listeners
from canvas import create_canvas
from menu import create_menu
from object_factory import HTML


async def main():
    js.document.title = "Hajle Silesia Homebrewing System"

    HTML("div", None, {"id": "menu_container", "class": "menu"})
    tabs = [
        "recipe",
        "brewing",
        # "calibration",
        "ferm",
        # "analysis",
    ]
    for tab in tabs:
        create_menu(tab)
        create_canvas(tab)

    await listeners.show_last_file_content()

    js.document.getElementById("start").click()


asyncio.ensure_future(main())
