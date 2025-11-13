import aiogram
import dotenv
import os


dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = aiogram.Bot(token = TOKEN)
dispatcher = aiogram.Dispatcher()


mentors_ids = []