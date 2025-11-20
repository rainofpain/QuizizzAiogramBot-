import aiogram
import aiogram.types as types
import aiogram.filters.callback_data as callback_data
import json

from config import dispatcher, active_tests_list, StartCallback
from utils import create_path


@dispatcher.callback_query(StartCallback.filter())
async def start_test_callback(callback_query: types.CallbackQuery, callback_data: StartCallback):
    
    filename = callback_data.filename
    with open(filename) as file:
        loaded_file = json.load(file)
    
    
    
    callback_query.message.edit_text("text", reply_markup = "new_keyboard")
    
    
