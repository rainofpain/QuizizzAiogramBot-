import aiogram.types as types
import json

from config import dispatcher, StartCallback, AnswerButtonCallback, active_tests_list, bot
from utils import create_path
from ..keyboards import answer_keyboard


@dispatcher.callback_query(StartCallback.filter())
async def start_test_callback(callback_query: types.CallbackQuery, callback_data: StartCallback):
    
    filename = callback_data.filename
    entry_code = callback_data.entry_code
    
    with open(create_path(filename)) as file:
        loaded_file = json.load(file)
    
    buttons_list = []
    answer_keyboard.inline_keyboard = []
    
    question_number = 1
    
    question = loaded_file["questions"][f"{question_number}"]["text"]
    correct = loaded_file["questions"][f"{question_number}"]["correct"]
    answers_list = loaded_file["questions"][f"{question_number}"]["answers"]
    test_lenght = len(loaded_file["questions"].keys())
    
    for answer in answers_list:
        
        button = types.InlineKeyboardButton(
            text = answer, 
            callback_data = AnswerButtonCallback(
                answer_key = question_number,
                correct_answer = correct,
                index = answers_list.index(answer),
                points = 0,
                filename = filename,
                entry_code = entry_code                       
                ).pack()
            )
        
        buttons_list.append(button)
    
    answer_keyboard.inline_keyboard.append(buttons_list)
    
    for test in active_tests_list:
        if test["entry_code"] == entry_code:
            
            for user in test["students_list"]:
                await bot.edit_message_text(
                    chat_id = user["user_id"],
                    message_id = user["user_message_id"], 
                    text = question,
                    reply_markup = answer_keyboard
                ) 
        
        lobby_progress = "\n".join(f"{user["user_lobby_name"]}: {user["user_progress"]}/{test_lenght}" for user in test["students_list"])
        progress = await callback_query.message.edit_text(text = f"Прогресс проходження тесту:\n {lobby_progress}")
        print(progress.message_id)
        
        break
