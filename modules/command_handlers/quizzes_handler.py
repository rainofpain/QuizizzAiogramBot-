import aiogram.filters as filters
import aiogram.types as types
import os

from ..callback_handlers import TypeCallback
from ..create_path import create_path
from config import dispatcher
from ..keyboards import test_keyboard


@dispatcher.message(filters.Command(commands = "quizzes"))
async def quizzes_command(message: types.Message):
    """
    Функція обробник хендлера команди /quizzes
    """
    json_filenames_list = os.listdir(create_path("static/json"))
    """
    Створюємо список у який ми зберігаємо усі назви json файлів з вказаної директорії
    """
    buttons_list = []
    """
    Створюємо порожній список у який ми будемо у подальшому зберігати кнопки
    """
    test_keyboard.inline_keyboard = []
    """
    Очищаємо список кнопок клавіатури шляхом його переприсвоєння, щоб кнопки не дублювались
    """
    
    for json_filename in json_filenames_list:
        """
        Очищаємо список кнопок клавіатури шляхом його переприсвоєння, щоб кнопки не дублювались
        """
        button = types.InlineKeyboardButton(text = json_filename, callback_data= TypeCallback(callback_type = "test", callback_filename = json_filename).pack())
        """
        Створюємо кнопку для клавіатури
        """
        buttons_list.append(button)
        """
        Додаємо кнопку до списку з кнопками
        """
    test_keyboard.inline_keyboard.append(buttons_list)
    """
    Додаємо кнопки до списку клавіатури
    """
    
    await message.answer(text = "Ось доступні тести: ", reply_markup = test_keyboard)
    """
    Відправляємо месседж до якого прикріплюємо заповнену кнопками клавіатуру
    """
