from object_factory import HTML


def create_menu(tab):
    HTML(
        "div",
        "menu",
        {
            "id": f"{tab}_menu_item",
            "class": "menu_item",
        },
    )
    HTML(
        "img",
        f"{tab}_menu_item",
        {
            "class": "image",
            "src": f"./img/{tab}.png",
        },
    )
    HTML(
        "div",
        f"{tab}_menu_item",
        {
            "id": f"{tab}_item_overlay",
            "class": "overlay",
            "event": "click",
            "listener": "activate_tab",
            "element_id": tab,
        },
    )
    HTML(
        "div",
        f"{tab}_item_overlay",
        {
            "id": f"{tab}_item_text",
            "class": "text",
            "event": "click",
            "listener": "activate_tab",
            "element_id": tab,
            "inner_html": tab.title(),
        },
    )
