import asyncio 
import aiogram
import aiogram.types as types
import aiogram.filters as filters
import dotenv
import os

from keyboard import start_keyboard


dotenv.load_dotenv()


TOKEN = os.getenv("TOKEN")

bot = aiogram.Bot(token = TOKEN)
dispatcher = aiogram.Dispatcher()


@dispatcher.message(filters.CommandStart())
async def start_handler(message: types.Message):
    await message.answer(text = "Hello!", reply_markup = start_keyboard)


async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
