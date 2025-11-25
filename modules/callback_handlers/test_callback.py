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


@dispatcher.callback_query(TypeCallback.filter())
async def test_callback(callback_query: types.CallbackQuery, callback_data: TypeCallback):
    """
    Функція для обробки Колбеку виду test
    з параметрами:
    - callback_query
    - callback_data -> зберігає в собі атрибути які прив'язані до кнопки
    """
    loaded_test_name = f"static/json/{callback_data.callback_filename}.json"

    students_list = []

    entry_code = create_code()
    while entry_code in entry_code_list:
        entry_code = create_code()


    await callback_query.message.answer(text = f"Код підтвердження: {entry_code}") 
    
    members_message = await callback_query.message.answer(text = "Всі учасники: ")
    message_id = members_message.message_id
    print(message_id)
    
    test = {
        "entry_code": entry_code,
        "loaded_test_name": loaded_test_name,
        "students_list": students_list,
        "mentor_id": callback_data.mentor_id,
        "message_id": message_id
    }
    
    active_tests_list.append(test)

