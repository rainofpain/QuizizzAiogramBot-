import aiogram.types as types

from config import FinishTestCallback, bot


async def lobby_progress(test: dict, entry_code: str, test_length: int):
    lobby_progress = "\n".join(f"{user["user_lobby_name"]}: {user["user_progress"]}/{test_length}" for user in test["students_list"])
    
    mentor_id = test["mentor_id"]
    mentor_message_id = test["message_id"]
    
    await bot.edit_message_text(
        chat_id = mentor_id,
        message_id = mentor_message_id, 
        text = f"Прогресс проходження тесту:\n {lobby_progress}",
        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [
            [
                types.InlineKeyboardButton(
                    text = "Завершити тест", 
                    callback_data = FinishTestCallback(entry_code = entry_code).pack()
                )
            ]
        ])
    )
