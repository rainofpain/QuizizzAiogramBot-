import aiogram
import aiogram.types as types

from config import dispatcher
from ..fsm_handlers import test1, test2

@dispatcher.callback_query(aiogram.F.data == 'yes_callback')
async def yes_callback(callback_query: types.CallbackQuery):
    mistakes = "помилки"
    await callback_query.message.answer(text = f"{mistakes}")