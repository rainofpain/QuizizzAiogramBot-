import aiogram
import aiogram.types as types
import aiogram.fsm.context as context

from config import dispatcher
from ..fsm_handlers import Test2, test2

@dispatcher.callback_query(aiogram.F.data == 'test2_callback')
async def test2_callback(callback_query: types.CallbackQuery, state: context.FSMContext):
    await callback_query.message.answer(text = "ВИ ОБРАЛИ ТЕСТ НОМЕР 2")
    for value in test2["questions"]["1"].keys():
        if value == "text":
            await callback_query.message.answer(text = "Питання 1: ")
            await callback_query.message.answer(text = f"{test2["questions"]["1"][f"{value}"]}")
            await callback_query.message.answer(text = "Варіанти відповіді: ")
        if value == "answers":
            for answer in test2["questions"]["1"][f"{value}"]:
                await callback_query.message.answer(text = f"{answer}")
    await callback_query.message.answer(text = "Введіть відповідь: ")
    
    await state.set_state(Test2.question_1)
    
