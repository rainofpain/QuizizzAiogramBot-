import aiogram.types as types

start_keyboard_btn_list = [
    [
        types.KeyboardButton(text = "/start")
    ]
]

start_keyboard = types.ReplyKeyboardMarkup(keyboard = start_keyboard_btn_list)
