import aiogram.filters as filters
import aiogram.types as types
import aiogram.fsm.context as context

from config import dispatcher
from ..state_groups import Join_state

@dispatcher.message(filters.Command(commands = "join"))
async def join_command(message: types.Message, state: context.FSMContext):
    await message.answer(text = "Введіть код: ")
    await state.set_state(Join_state.code)
    