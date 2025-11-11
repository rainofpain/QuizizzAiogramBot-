import aiogram
import aiogram.types as types
import aiogram.fsm.context as context


from config import dispatcher


@dispatcher.callback_query(aiogram.F.data == 'test1_callback')
async def test1_callback(callback_query: types.CallbackQuery, state: context.FSMContext):
    pass
    