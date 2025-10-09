import aiogram.types as types

reply_keyboard_list = [
    [
        types.KeyboardButton(text = "hello")
    ]
]
reply_keyboard = types.ReplyKeyboardMarkup(
    keyboard = reply_keyboard_list,
    resize_keyboard = True,
    input_field_placeholder = "Оберіть дію серед поданих"
)

