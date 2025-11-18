import aiogram
import aiogram.types as types
import aiogram.filters.callback_data as callback_data
import json

from utils import create_path, create_code
from config import dispatcher, entry_code_list, active_tests_list


class TypeCallback(callback_data.CallbackData, prefix = "type_callback"):
    callback_type: str
    callback_filename: str
    mentor_id: int
"""
Створюємо класс TypeCallback від классу CallbackData 

З атрибутами :

- callback_type: str -> атрибут для зберігання виду колбеку (ключ по котрому вони будуть визиватись)
- callback_filename: str -> атрибут для зберігання назви файлу

"""


@dispatcher.callback_query(TypeCallback.filter(aiogram.F.callback_type == "test"))
async def test_callback(callback_query: types.CallbackQuery, callback_data: TypeCallback):
    """
    Функція для обробки Колбеку виду test
    з параметрами:
    - callback_query
    - callback_data -> зберігає в собі атрибути які прив'язані до кнопки
    """
    with open(create_path(f"static/json/{callback_data.callback_filename}.json")) as json_file:
        loaded_json = json.load(json_file)

    students_list = []

    entry_code = create_code()
    while entry_code in entry_code_list:
        entry_code = create_code()
    
    
    
    print(callback_data.mentor_id)


    await callback_query.message.answer(text = f"Код підтвердження: {entry_code}") 
    
    
    await callback_query.message.answer(text = f"Всі учасники: ")
    message_id = callback_query.message.message_id

    test = {
        "entry_code": entry_code,
        "loaded_test": loaded_json,
        "students_list": students_list,
        "mentor_id": callback_data.mentor_id,
        "message_id": message_id
    }
    
    active_tests_list.append(test)

    print(message_id)
