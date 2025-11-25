import aiogram.types as types

from config import dispatcher, FinishTestCallback, active_tests_list, bot


@dispatcher.callback_query(FinishTestCallback.filter())
async def finish_test_callback(callback_query: types.CallbackQuery, callback_data: FinishTestCallback):
    for test in active_tests_list:
        if test["entry_code"] == callback_data.entry_code:
            for user in test["students_list"]:
                await bot.edit_message_text(
                    chat_id = user["user_id"],
                    message_id = user["user_message_id"], 
                    text = f"Тест завершено!"
                    )
            active_tests_list.remove(test)
            await callback_query.message.answer(text = "Тест успішно завершено!")
    
    