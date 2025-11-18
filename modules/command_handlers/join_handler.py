import aiogram.filters as filters
import aiogram.types as types
import aiogram.fsm.context as context

from config import dispatcher, mentors_ids
from ..state_groups import Join_state

@dispatcher.message(filters.Command(commands = "join"))
async def join_command(message: types.Message, state: context.FSMContext):
    telegram_id = message.from_user.id
    
    if telegram_id in mentors_ids:
        await message.answer(text = "Ментор не може проходити тест")
    else:
        await message.answer(text = "Введіть код: ")
        await state.set_state(Join_state.code)
    