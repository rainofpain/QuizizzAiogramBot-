import aiogram
import aiogram.filters as filters
import aiogram.types as types

from config import dispatcher
from modules import inline_keyboard_markup

@dispatcher.message(filters.CommandStart())
async def start_handler(message: types.Message):
    await message.answer(text = "Hello!", reply_markup = inline_keyboard_markup)
