import asyncio 
import aiogram.filters as filters
import aiogram.types as types

from config import dispatcher, bot
from modules import *

async def main():
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
