import aiogram.types as types
import json

from config import dispatcher, StartCallback, AnswerButtonCallback
from utils import create_path
from ..keyboards import answer_keyboard

@dispatcher.callback_query(StartCallback.filter())
async def start_test_callback(callback_query: types.CallbackQuery, callback_data: StartCallback):
    
    filename = callback_data.filename
    with open(create_path(filename)) as file:
        loaded_file = json.load(file)
    
    buttons_list = []
    answer_keyboard.inline_keyboard = []
    
    question_number = 1

    question = loaded_file["questions"][f"{question_number}"]["text"]
    correct = loaded_file["questions"][f"{question_number}"]["correct"]

    for answer in loaded_file["questions"][f"{question_number}"]["answers"]:
        
        button = types.InlineKeyboardButton(
            text = answer, 
            callback_data = AnswerButtonCallback(
                answer_key = question_number,
                correct_answer = correct,
                points = 0,
                filename = filename                        
                ).pack()
            )
        
        buttons_list.append(button)
        
    answer_keyboard.inline_keyboard.append(buttons_list)
    
    await callback_query.message.edit_text(text = question, reply_markup = answer_keyboard)
    
    
