import js
import asyncio

from brewing import create_brewing, show
from menu import create_menu, activate_tab
from recipe import create_recipe


async def main():
    js.document.title = "Hajle Silesia Homebrewing System"

    create_menu()
    await create_recipe()
    create_brewing()


if __name__ == '__main__':
    asyncio.gather(main())
