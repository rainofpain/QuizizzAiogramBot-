import aiogram
import aiogram.types as types
import aiogram.fsm.context as context
import aiogram.filters.callback_data as callback_data
import json

from utils import create_path, create_code
from config import dispatcher


class TypeCallback(callback_data.CallbackData, prefix = "type_callback"):
    callback_type: str
    callback_filename: str
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
    З параметрами:
    - callback_query
    - callback_data -> зберігає в собі атрибути які прив'язані до кнопки
    """
    
    loaded_json = json.load(open(create_path(f"static/json/{callback_data.callback_filename}.json")))
    
    await callback_query.message.answer(text = f"Код підтвердження: {create_code()}") 
