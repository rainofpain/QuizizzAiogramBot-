import aiogram
import dotenv
import os


dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = aiogram.Bot(token = TOKEN)
dispatcher = aiogram.Dispatcher()

my_id = 996602601
mentors_ids = [my_id]
entry_code_list = []

active_tests_list = []
"""
Ідея в тому щоб у цьому списку зберігати списки з інформацією про активні тести

у списку з інформацією про тест зміст елементів виглядає так:

test = ["code", "loaded_json", [students_list]]

"""