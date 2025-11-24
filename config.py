import aiogram
import dotenv
import os

import aiogram.filters.callback_data as callback_data


dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = aiogram.Bot(token = TOKEN)
dispatcher = aiogram.Dispatcher()

my_id = 996602601
mentors_ids = [my_id, 1521234621]
entry_code_list = []

active_tests_list = []
"""
Ідея в тому щоб у цьому списку зберігати списки з інформацією про активні тести

у списку з інформацією про тест зміст елементів виглядає так:

test = ["code", "loaded_json", [students_list]]

"""


class StartCallback(callback_data.CallbackData, prefix = "start_test"):
    filename: str

class AnswerButtonCallback(callback_data.CallbackData, prefix = "answer_button"):
    answer_key: int
    correct_answer: int
    index: int
    points: int
    filename: str
