import aiogram.filters as filters
import aiogram.types as types

import os

from config import dispatcher
from ..keyboards import test_keyboard


@dispatcher.message(filters.Command(commands = "quizzes"))
async def quizzes_command(message: types.Message):
    
    json_filenames_list = os.listdir("static/json")
    buttons_list = []
    
    test_keyboard.inline_keyboard = []
    
    for json_filename in json_filenames_list:
        
        button = types.InlineKeyboardButton(text = json_filename, callback_data= f"{json_filename[0:-5]}_callback")
        
        buttons_list.append(button)
    
    test_keyboard.inline_keyboard.append(buttons_list)
    
    
    await message.answer(text = "Ось доступні тести: ", reply_markup = test_keyboard)
