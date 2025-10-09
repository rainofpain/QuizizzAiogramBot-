import asyncio 
import aiogram
import aiogram.types as types
import aiogram.fsm.state as state
import aiogram.fsm.context as context
import aiogram.filters as filters
import dotenv
import os

from keyboards import reply_keyboard


dotenv.load_dotenv()



TOKEN = os.getenv("TOKEN")

bot = aiogram.Bot(token = TOKEN)
dispatcher = aiogram.Dispatcher()


class User_info(state.StatesGroup):
    name = state.State()
    email = state.State()
    age = state.State()


@dispatcher.message(filters.CommandStart())
async def start_handler(message: types.Message, state: context.FSMContext):
    await message.answer(text = "Це реєтрація! Введіть ваше ім'я:")
    
    await state.set_state(User_info.name)


@dispatcher.message(User_info.name)
async def name_state(message: types.Message, state: context.FSMContext):
    await state.update_data(name = message.text)
    
    await message.answer(text = "Введіть вашу пошту:")
    
    await state.set_state(User_info.email)

@dispatcher.message(User_info.email)
async def name_state(message: types.Message, state: context.FSMContext):
    await state.update_data(email = message.text)
    
    await message.answer(text = "Введіть ваш вік:")
    
    await state.set_state(User_info.age)

@dispatcher.message(User_info.age)
async def name_state(message: types.Message, state: context.FSMContext):
    await state.update_data(age = message.text)
    
    user_info_data = await state.get_data()
    
    await message.answer(text = f"Info: {user_info_data.get("age")}")
    await state.clear()


async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
