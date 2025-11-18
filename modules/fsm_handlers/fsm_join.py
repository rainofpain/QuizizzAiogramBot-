import aiogram.fsm.context as context
import aiogram.types as types

from config import dispatcher, active_tests_list
from ..command_handlers import join_command
from ..keyboards import start_test_keyboard
from ..state_groups import Join_state

@dispatcher.message(Join_state.code)
async def update_join_state(message: types.Message, state: context.FSMContext):
    is_code_in_list = False
    entered_code = message.text
    
    await state.update_data(code = message.text)
    # entered_code = await state.get_data()
    for test in active_tests_list:
        if entered_code in test["entry_code"]:
            test["students_list"].append((message.from_user.full_name,message.from_user.id))
            mentor_id = test["mentor_id"]
            
            await message.answer(text = "Правильно")
            await state.clear()
            
            is_code_in_list = True
            break
        else: 
            is_code_in_list = False
    
    if is_code_in_list == False:
        await message.answer(text = "Такого коду немає!")
        
        await state.clear()
        
        await message.answer(text = "Введіть код: ")
        await state.set_state(Join_state.code)
        
