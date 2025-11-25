import aiogram.types as types
from config import FinishTestCallback


test_keyboard = types.InlineKeyboardMarkup(inline_keyboard = [])

start_test_keyboard = types.InlineKeyboardMarkup(inline_keyboard = [[
    types.InlineKeyboardButton(text = "", 
        callback_data= "start_test")
]])

answer_keyboard = types.InlineKeyboardMarkup(inline_keyboard = [])

