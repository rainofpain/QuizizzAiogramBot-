import aiogram.fsm.context as context
import aiogram.types as types

from config import bot, dispatcher, active_tests_list, StartCallback
from ..keyboards import start_test_keyboard
from ..state_groups import LobbyAuthorizationState


@dispatcher.message(LobbyAuthorizationState.lobby_name)
async def update_lobby_authorization_state(message: types.Message, state: context.FSMContext):
    
    user_id = message.from_user.id
    lobby_name = message.text
    
    await state.update_data(lobby_name = lobby_name)
    
    user_message = await message.answer("Чейкайте початку тесту")
    user_message_id = user_message.message_id
    
    for test in active_tests_list:
        for user in test["students_list"]:
            if user_id == user["user_id"]:
                user["user_lobby_name"] = lobby_name
                user["user_message_id"] = user_message_id
                mentor_id = test["mentor_id"]
                mentor_message_id = test["message_id"]
                
                filename = test["loaded_test_name"]
                entry_code = test["entry_code"]
                lobby_names = ", ".join(user["user_lobby_name"] for user in test["students_list"])
                
                if len(test["students_list"]) > 0:
                    start_test_keyboard.inline_keyboard[0][0] = types.InlineKeyboardButton(
                        text = "ПОЧАТИ ТЕСТ", 
                        callback_data = StartCallback(filename = filename, entry_code = entry_code).pack()
                    )
                
                await bot.edit_message_text(
                    chat_id = mentor_id,
                    message_id = mentor_message_id, 
                    text = f"Всі учасники: \n{lobby_names}",
                    reply_markup = start_test_keyboard
                )
                break
    await state.clear()
