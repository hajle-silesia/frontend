import js
import pyodide.ffi.wrappers
import pyodide.http

from object_factory import HTML


async def activate_tab(*args, **kwargs):
    for element in js.document.getElementsByClassName("canvas"):
        element.hidden = True
    js.document.getElementById(args[0].target.id.split("_")[0]).hidden = False


def create_menu():
    menu_container = HTML('div', None, {'class': "menu"})
    tabs = ["recipe",
            "brewing",
            "calibration",
            "fermentation",
            "analysis",
            ]

    for tab in tabs:
        item = HTML('div', menu_container.element, {'class': "menu_item"})
        image = HTML('img', item.element, {'class': "image", 'src': f"./img/{tab}.png"})
        overlay = HTML('div', item.element,
                       {'id': f"{tab}_tab_overlay", 'class': "overlay"})
        text = HTML('div', overlay.element,
                    {'id': f"{tab}_tab_text", 'class': "text", 'inner_html': tab.title()})
        pyodide.ffi.wrappers.add_event_listener(overlay.element, "click", activate_tab)
        pyodide.ffi.wrappers.add_event_listener(text.element, "click", activate_tab)
