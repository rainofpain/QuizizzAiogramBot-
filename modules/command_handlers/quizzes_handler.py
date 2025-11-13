import aiogram.filters as filters
import aiogram.types as types
import os

from utils import create_path
from config import dispatcher, mentors_ids
from ..callback_handlers import TypeCallback
from ..keyboards import test_keyboard


"""
В цьому модули оброблюємо команду /quizzes, в результаті надсилаємо клавіатуру із тестами боту

Тут ми беремо тести з папки static/json
"""


@dispatcher.message(filters.Command(commands = "quizzes"))
async def quizzes_command(message: types.Message):
    
    telegram_id = message.from_user.id
    
    if telegram_id in mentors_ids:
        # Функція обробник хендлера команди /quizzes
        json_filenames_list = os.listdir(create_path("static/json"))
        
        buttons_list = []
        test_keyboard.inline_keyboard = []
        
        
        for json_filename in json_filenames_list:
            
            button = types.InlineKeyboardButton(text = json_filename, callback_data= TypeCallback(callback_type = "test", callback_filename = json_filename[0:-5]).pack())
            
            buttons_list.append(button)
        test_keyboard.inline_keyboard.append(buttons_list)
        
        
        await message.answer(text = "Ось доступні тести: ", reply_markup = test_keyboard)
    else:
        await message.answer(text = "Ви не являєтесь ментором")
