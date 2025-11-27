import aiogram.types as types
import json

from config import dispatcher, AnswerButtonCallback, active_tests_list, bot
from utils import create_path, check_entry_code, check_user_id
from ...keyboards import answer_keyboard
from .lobby_progress import lobby_progress


@dispatcher.callback_query(AnswerButtonCallback.filter())
async def answer_button_callback(callback_query: types.CallbackQuery, callback_data: AnswerButtonCallback):
    
    filename = callback_data.filename
    entry_code = callback_data.entry_code
    question_number = callback_data.answer_key + 1
    
    callback_user_id = callback_query.from_user.id
    
    
    with open(create_path(filename)) as file:
        loaded_file = json.load(file)
    
    test_length = len(loaded_file["questions"].keys())
    
    
    buttons_list = []
    answer_keyboard.inline_keyboard = []
    
    if question_number <= test_length:
        
        question = loaded_file["questions"][f"{question_number}"]["text"]
        correct = loaded_file["questions"][f"{question_number}"]["correct"]
        answers_list = loaded_file["questions"][f"{question_number}"]["answers"]
        
        for answer in answers_list:
            button = types.InlineKeyboardButton(
                text = answer, 
                callback_data = AnswerButtonCallback(
                    answer_key = question_number,
                    correct_answer = correct,
                    index = answers_list.index(answer),
                    filename = filename,
                    entry_code = entry_code                       
                    ).pack()
                )
            buttons_list.append(button)
            
        answer_keyboard.inline_keyboard.append(buttons_list)
        
        for test in active_tests_list:
            if check_entry_code(test, entry_code):
                for user in test["students_list"]:
                    if check_user_id(callback_user_id, user["user_id"]):
                        user["user_progress"] += 1
                        if callback_data.correct_answer == callback_data.index:
                            user["user_points"] += 1
                        await bot.edit_message_text(
                            chat_id = user["user_id"],
                            message_id = user["user_message_id"], 
                            text = question,
                            reply_markup = answer_keyboard
                        )
                        break
                
                await lobby_progress(
                    test = test,
                    entry_code = entry_code,
                    test_length = test_length
                )
                
                break
    else:
        for test in active_tests_list:
            if check_entry_code(test, entry_code):
                for user in test["students_list"]:
                    
                    if check_user_id(callback_user_id, user["user_id"]):
                        user["user_progress"] += 1
                        if callback_data.correct_answer == callback_data.index:
                            user["user_points"] += 1
                        
                        await bot.edit_message_text(
                            chat_id = user["user_id"],
                            message_id = user["user_message_id"], 
                            text = f"Тест завершено!\n Правильніх відповідей: {user["user_points"]}"
                        )
                        
                        break
                
                await lobby_progress(
                    test = test,
                    entry_code = entry_code,
                    test_length = test_length
                )
                
                break
