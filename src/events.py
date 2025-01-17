import js
import pyodide.ffi.wrappers

registry = {}


def register(func):
    registry[func.__name__] = func
    return func


def console(func):
    def wrapper(*args, **kwargs):
        print(f"len args: {len(args)}")
        print(f"type: {args[0].type}")
        print(f"target: {args[0].target}")
        print(f"target.id: {args[0].target.id}")
        print(f"target.src: {args[0].target.src}")
        print(f"type(target.id): {type(args[0].target.id)}")

        func(*args, **kwargs)

    return wrapper


@register
def switch(event, element_id):
    (
        js.document.getElementById(element_id).src,
        js.document.getElementById(element_id).alt,
    ) = (
        js.document.getElementById(element_id).alt,
        js.document.getElementById(element_id).src,
    )


@register
def switch_visibility(event, element_id):
    if js.document.getElementById(element_id).hidden:
        js.document.getElementById(element_id).hidden = False
    else:
        js.document.getElementById(element_id).hidden = True


def set_event(element, func, element_id):
    def wrapper(event):
        func(event, element_id)

    pyodide.ffi.wrappers.add_event_listener(
        element,
        "click",
        wrapper,
    )
