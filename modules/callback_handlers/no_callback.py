import aiogram
import aiogram.types as types

from config import dispatcher

@dispatcher.callback_query(aiogram.F.data == 'no_callback')
async def no_callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = "ТОДІ, ДО ЗУСТРІЧІ!")