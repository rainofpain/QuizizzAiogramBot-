import aiogram.types as types

inline_keyboard_list = [
    [types.InlineKeyboardButton(text = "ТАК", callback_data= "yes_callback")],
    [types.InlineKeyboardButton(text = "НІ", callback_data= "no_callback")]
] 

yes_or_no_keyboard = types.InlineKeyboardMarkup(inline_keyboard = inline_keyboard_list)