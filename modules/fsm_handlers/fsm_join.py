import aiogram.fsm.context as context
import aiogram.types as types

from config import dispatcher, active_tests_list
from ..state_groups import JoinState, LobbyAuthorizationState

@dispatcher.message(JoinState.code)
async def update_join_state(message: types.Message, state: context.FSMContext):
    is_code_in_list = False
    entered_code = message.text
    
    await state.update_data(code = message.text)
    
    for test in active_tests_list:
        if entered_code in test["entry_code"]:
            user_info = {
                "user_id": message.from_user.id,
                "user_lobby_name": "",
                "user_message_id": None
            }
            if len(test["students_list"]) == 0:
                test["students_list"].append(user_info)
                await state.clear()
                await message.answer(text = "Введіть ваше ім'я: ")
                await state.set_state(LobbyAuthorizationState.lobby_name)
                is_code_in_list = True
                break
            
            elif len(test["students_list"]) > 0:
                for user in test["students_list"]:
                    if user_info["user_id"] == user["user_id"] and user["user_lobby_name"] != "":
                        await message.answer(text= "Користувач вже є в списку")
                        is_code_in_list = True
                        break
                    else:    
                        test["students_list"].append(user_info)
                        await state.clear()
                        await message.answer(text = "Введіть ваше ім'я: ")
                        await state.set_state(LobbyAuthorizationState.lobby_name)
                        is_code_in_list = True
                break
        else: 
            is_code_in_list = False
    
    if is_code_in_list == False:
        await message.answer(text = "Такого коду немає!")
        
        await state.clear()
        
        await message.answer(text = "Введіть код: ")
        await state.set_state(JoinState.code)
        
