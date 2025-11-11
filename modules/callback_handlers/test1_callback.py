import aiogram
import aiogram.types as types
import aiogram.fsm.context as context
from config import dispatcher
from ..fsm_handlers import Test1, test1

@dispatcher.callback_query(aiogram.F.data == 'test1_callback')
async def test1_callback(callback_query: types.CallbackQuery, state: context.FSMContext):
    await callback_query.message.answer(text = "ВИ ОБРАЛИ ТЕСТ НОМЕР 1")
    for value in test1["questions"]["1"].keys():
        if value == "text":
            await callback_query.message.answer(text = "Питання 1: ")
            await callback_query.message.answer(text = f"{test1["questions"]["1"][f"{value}"]}")
            await callback_query.message.answer(text = "Варіанти відповіді: ")
        if value == "answers":
            for answer in test1["questions"]["1"][f"{value}"]:
                await callback_query.message.answer(text = f"{answer}")
    await callback_query.message.answer(text = "Введіть відповідь: ")
    
    await state.set_state(Test1.question_1)
    
                    
                    
                 