import aiogram.types as types

inline_keyboard_list = [
    [types.InlineKeyboardButton(text = "ТЕСТ 1", callback_data= "test1_callback")],
    [types.InlineKeyboardButton(text = "ТЕСТ 2", callback_data= "test2_callback")],
    [types.InlineKeyboardButton(text = "ТЕСТ 3", callback_data= "test3_callback")]
] 

test_keyboard = types.InlineKeyboardMarkup(inline_keyboard = inline_keyboard_list)