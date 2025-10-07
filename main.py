import asyncio 
import aiogram
import aiogram.types as types
import aiogram.filters as filters
import dotenv
import os


from keyboards import reply_keyboard, actions_inline_keyboard

dotenv.load_dotenv()


TOKEN = os.getenv("TOKEN")

bot = aiogram.Bot(token = TOKEN)
dispatcher = aiogram.Dispatcher()


@dispatcher.message(filters.CommandStart())
async def start_handler(message: types.Message):
    await message.answer(text = "Hello!", reply_markup = actions_inline_keyboard)


@dispatcher.callback_query(aiogram.F.data == "plus_numbers")
async def plus_numbers(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"Сплюсуємо 2 та 10: {2 + 10}")


async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
