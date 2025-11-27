import aiogram.types as types
import json

from config import dispatcher, AnswerButtonCallback, FinishTestCallback, active_tests_list, bot
from utils import create_path
from ..keyboards import answer_keyboard


@dispatcher.callback_query(AnswerButtonCallback.filter())
async def answer_button_callback(callback_query: types.CallbackQuery, callback_data: AnswerButtonCallback):
    
    filename = callback_data.filename
    entry_code = callback_data.entry_code
    
    with open(create_path(filename)) as file:
        loaded_file = json.load(file)
    
    test_length = len(loaded_file["questions"].keys())
    
    question_number = callback_data.answer_key + 1
    
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
            if test["entry_code"] == entry_code:
                for user in test["students_list"]:
                    if callback_query.from_user.id == user["user_id"]:
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
                lobby_progress = "\n".join(f"{user["user_lobby_name"]}: {user["user_progress"]}/{test_length}" for user in test["students_list"])
                
                mentor_id = test["mentor_id"]
                mentor_message_id = test["message_id"]
                
                await bot.edit_message_text(
                    chat_id = mentor_id,
                    message_id = mentor_message_id, 
                    text = f"Прогресс проходження тесту:\n {lobby_progress}",
                    reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [
                        [
                            types.InlineKeyboardButton(text = "Завершити тест", callback_data = FinishTestCallback(entry_code = entry_code).pack())
                        ]
                    ])
                )
                break
    else:
        for test in active_tests_list:
            if test["entry_code"] == entry_code:
                for user in test["students_list"]:
                    
                    if callback_query.from_user.id == user["user_id"]:
                        user["user_progress"] += 1
                        if callback_data.correct_answer == callback_data.index:
                            user["user_points"] += 1
                        
                        await bot.edit_message_text(
                            chat_id = user["user_id"],
                            message_id = user["user_message_id"], 
                            text = f"Тест завершено!\n Правильніх відповідей: {user["user_points"]}"
                        )
                        
                        break
                
                lobby_progress = "\n".join(f"{user["user_lobby_name"]}: {user["user_progress"]}/{test_length}" for user in test["students_list"])
                
                mentor_id = test["mentor_id"]
                mentor_message_id = test["message_id"]
                
                await bot.edit_message_text(
                    chat_id = mentor_id,
                    message_id = mentor_message_id, 
                    text = f"Прогресс проходження тесту:\n {lobby_progress}",
                    reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [
                        [
                            types.InlineKeyboardButton(text = "Завершити тест", callback_data = FinishTestCallback(entry_code = entry_code).pack())
                        ]
                    ])
                )
                
                break
