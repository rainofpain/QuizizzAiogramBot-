import aiogram
import aiogram.types as types
import aiogram.filters.callback_data as callback_data
import json

from config import dispatcher, active_tests_list

class StartTestCallback(callback_data.CallbackData, prefix = "start_test"):
    test_code: str


@dispatcher.callback_query(StartTestCallback.filter(aiogram.F.test_code != ""))
async def start_test(callback_query: types.CallbackQuery, callback_data: StartTestCallback):
    for test in active_tests_list:
        if callback_data.test_code in test["entry_code"]:
            await callback_query.message.answer(text = f"{test["loaded_test"]}")