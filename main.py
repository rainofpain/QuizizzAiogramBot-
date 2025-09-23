import asyncio 
import aiogram
import aiogram.types as types
import aiogram.filters as filters


TOKEN = "8433330109:AAFsypFpAuEIiWdjj_8Wevm7FwV9zDYq6tw"

bot = aiogram.Bot(token = TOKEN)
dispatcher = aiogram.Dispatcher()

@dispatcher.message(filters.CommandStart())
async def start_command(message: types.Message):
    
    await message.answer("Hello")


async def main():
    try:
        await dispatcher.start_polling(bot)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    asyncio.run(main())

