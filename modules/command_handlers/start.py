import aiogram.filters as filters
import aiogram.types as types

from config import dispatcher
from keyboards import test_keyboard

@dispatcher.message(filters.CommandStart())
async def start_handler(message: types.Message):
    await message.answer(text = "ОБЕРІТЬ ТЕСТ", reply_markup = test_keyboard)
    