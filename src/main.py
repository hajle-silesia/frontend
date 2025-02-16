import asyncio
import js

from brewing import create_brewing
from menu import create_menu
from recipe import create_recipe


async def main():
    js.document.title = "Hajle Silesia Homebrewing System"

    create_menu()
    await create_recipe()
    create_brewing()

    js.document.getElementById("start").click()


asyncio.ensure_future(main())
