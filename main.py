import asyncio 
import aiogram
import aiogram.filters as filters
import aiogram.types as types
import aiogram.fsm.state as state
import aiogram.fsm.context as context
import dotenv
import os

from keyboard import inline_keyboard_markup

dotenv.load_dotenv()



TOKEN = os.getenv("TOKEN")

bot = aiogram.Bot(token = TOKEN)
dispatcher = aiogram.Dispatcher()


class User_info(state.StatesGroup):
    name = state.State()
    age = state.State()


@dispatcher.message(filters.CommandStart())
async def start_handler(message: types.Message):
    await message.answer(text = "Hello!", reply_markup= inline_keyboard_markup)

@dispatcher.callback_query(aiogram.F.data == "hello_data")
async def hello_data(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = "hello")

@dispatcher.callback_query(aiogram.F.data == "bye_data")
async def bye_data(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = "bye")



@dispatcher.message(filters.Command(commands = "register"))
async def register_handler(message: types.Message, state: context.FSMContext):
    await message.answer("Введіть ім'я: ")

    await state.set_state(User_info.name)

@dispatcher.message(User_info.name)
async def name_state(message: types.Message, state: context.FSMContext):
    await state.update_data(name = message.text)

    await message.answer(text = "Введіть ваш вік: ")

    await state.set_state(User_info.age)

@dispatcher.message(User_info.age)
async def age_state(message: types.Message, state: context.FSMContext):
    await state.update_data(age = message.text)

    user_info_data = await state.get_data()

    await message.answer(text = f"Info: {user_info_data}")
    await state.clear()


async def main():
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
