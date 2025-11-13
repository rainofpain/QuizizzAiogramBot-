import aiogram.types as types



test_keyboard = types.InlineKeyboardMarkup(inline_keyboard = [])

start_test_keyboard = types.InlineKeyboardMarkup(
    inline_keyboard = [[
        types.InlineKeyboardButton(
        text = "ПОЧАТИ ТЕСТ", 
        callback_data= "")
        ]]
        )
