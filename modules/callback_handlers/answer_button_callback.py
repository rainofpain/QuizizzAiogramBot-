import aiogram.types as types
import json

from config import dispatcher, StartCallback, AnswerButtonCallback
from utils import create_path
from ..keyboards import answer_keyboard

@dispatcher.callback_query(AnswerButtonCallback.filter())
async def answer_button_callback(callback_query: types.CallbackQuery, callback_data: AnswerButtonCallback):

    filename = callback_data.filename

    with open(create_path(filename)) as file:
        loaded_file = json.load(file)
    
    test_length = loaded_file["questions"].keys()
    previous_answers_list = loaded_file["questions"][f"{callback_data.answer_key}"]["answers"]
    points = callback_data.points

    for answer in previous_answers_list:
            if callback_data.correct_answer == previous_answers_list.index(answer):
                points += 1
                
    question_number = callback_data.answer_key + 1

    buttons_list = []
    answer_keyboard.inline_keyboard = []

    if question_number <= len(test_length):
        

        question = loaded_file["questions"][f"{question_number}"]["text"]
        correct = loaded_file["questions"][f"{question_number}"]["correct"]
        answers_list = loaded_file["questions"][f"{question_number}"]["answers"]

        for answer in answers_list:
        
            button = types.InlineKeyboardButton(
                text = answer, 
                callback_data = AnswerButtonCallback(
                    answer_key = question_number,
                    correct_answer = correct,
                    points = points,
                    filename = filename                        
                    ).pack()
                )
            buttons_list.append(button)
            
        answer_keyboard.inline_keyboard.append(buttons_list)
        
        await callback_query.message.edit_text(text = question, reply_markup = answer_keyboard)
    else:
        await callback_query.message.edit_text(text = f"Тест завершено!\n Правильніх відповідей: {points}", reply_markup = answer_keyboard)