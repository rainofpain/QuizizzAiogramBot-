import aiogram.types as types

inline_keyboard_list = [
    types.InlineKeyboardButton(text="test_1", callback_data= "test_1_callback"),
    types.InlineKeyboardButton(text="test_2", callback_data= "test_2_callback")
] 

inline_keyboard_markup = types.InlineKeyboardMarkup(inline_keyboard = inline_keyboard_list)