import aiogram.filters as filters
import aiogram.types as types

from config import dispatcher


@dispatcher.message(filters.CommandStart())
async def start_command(message: types.Message):
    """
    Функція обробник хендлера команди /start
    """
    await message.answer(
        "Вітаю!"
        "\nЯ Quizizz бот"
        "\n\nОсь список моїх команд, якими ти можеш користуватись:"
        "\n - /quizzes - отримати усі доступні тести"
        "\n - /join - приєднатися до тесту по коду"
    )
    """
    Месседж для користувача з функціями бота
    """