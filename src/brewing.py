import csv

import js
import pyodide.ffi.wrappers
import pyodide.http

from object_factory import HTML


async def show(*args, **kwargs):
    js.console.log(f"len args: {len(args)}")
    js.console.log(f"type: {args[0].type}")
    js.console.log(f"target: {args[0].target}")
    js.console.log(f"target.id: {args[0].target.id}")
    js.console.log(f"target.src: {args[0].target.src}")
    js.console.log(f"type(target.id): {type(args[0].target.id)}")

    if "_off" in args[0].target.src:
        js.document.getElementById(args[0].target.id).setAttribute("src", "./img/button_on.png")
    elif "_on" in args[0].target.src:
        js.document.getElementById(args[0].target.id).setAttribute("src", "./img/button_off.png")


def create_brewing():
    brewing_tab = HTML('div', None, {'id': "brewing", 'class': "canvas"})

    with open("./config/brewing_imgs_coords.csv", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        imgs_coords = list(reader)

    HTML('img', brewing_tab.element, {'id': "brewing_bg",
                                      'class': "background",
                                      'src': "./img/brewing_bg.png",
                                      })

    for img_coords in imgs_coords:
        canvas_item = HTML('img', brewing_tab.element, {'id': img_coords['id'],
                                                        'class': "canvas_item",
                                                        'src': f"./img/{img_coords['name']}.png",
                                                        'style_left': f"{100 * float(img_coords['x'])}%",
                                                        'style_top': f"{100 * float(img_coords['y'])}%",
                                                        })
        pyodide.ffi.wrappers.add_event_listener(canvas_item.element, "click", show)

    js.document.getElementById("brewing").hidden = True
