import asyncio 

from config import dispatcher, bot
from modules import *


async def main():
    try:
        await dispatcher.start_polling(bot)
    except Exception as error:
        print(f"Помилка під час запуску проєкту: {error}")


if __name__ == "__main__":
    asyncio.run(main())
