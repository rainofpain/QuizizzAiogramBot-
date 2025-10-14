import aiogram.types as types

inline_keyboard_list = [
    [
        types.InlineKeyboardButton(text = "hello", callback_data = "hello_data"),
        types.InlineKeyboardButton(text = "bye", callback_data = "bye_data")  
    ]
]

inline_keyboard_markup = types.InlineKeyboardMarkup(inline_keyboard = inline_keyboard_list)