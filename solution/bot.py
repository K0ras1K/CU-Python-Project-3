from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()


bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
front_url = os.getenv("FRONT_DASHBOARD_URL")

bot = Bot(token=bot_token)

router = Router()

@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Я бот прогноза погоды. Я могу предоставить прогноз погоды для указанных городов. "
        "Введите команду в формате: `/weather <start-city> : <end-city>` и выберите диапазон прогноза.")

# Обработчик команды /help
@router.message(Command('help'))
async def send_help(message: types.Message):
    await message.reply(
        "Список доступных команд:\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать справочную информацию\n"
        "/weather <start-city> : <end-city> - Узнать прогноз погоды для указанного маршрута\n\n"
        "После ввода команды `Weather`, выберите прогноз на день, 7 дней или 10 дней для каждого города."
    )

# Обработчик команды Weather
@router.message(lambda message: message.text.lower().startswith("/weather"))
async def weather_command(message: types.Message):
    # Извлечение городов из команды
    try:
        start_city, end_city = message.text.split(":")[0].split(" ")[1].strip(), message.text.split(":")[1].strip()
    except ValueError:
        await message.reply("Пожалуйста, укажите команду в формате: `Weather <start-city> : <end-city>`")
        return
    
    # Создание кнопок для выбора прогноза
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=f"{start_city} 1 день", callback_data=f"forecast_{start_city}_1"),
            InlineKeyboardButton(text=f"{start_city} 7 дней", callback_data=f"forecast_{start_city}_7"),
            InlineKeyboardButton(text=f"{start_city} 10 дней", callback_data=f"forecast_{start_city}_10"),
        ],
        [
            InlineKeyboardButton(text=f"{end_city} 1 день", callback_data=f"forecast_{end_city}_1"),
            InlineKeyboardButton(text=f"{end_city} 7 дней", callback_data=f"forecast_{end_city}_7"),
            InlineKeyboardButton(text=f"{end_city} 10 дней", callback_data=f"forecast_{end_city}_10")
        ]
    ])
    await message.reply("Выберите диапазон прогноза:", reply_markup=keyboard)

# Обработчик нажатий на кнопки прогноза
@router.callback_query(lambda c: c.data.startswith("forecast"))
async def process_forecast_callback(callback_query: types.CallbackQuery):
    # Извлечение данных из callback_data
    _, city, days = callback_query.data.split("_")
    
    # Формирование ссылки на прогноз
    forecast_url = f"{front_url}?city={city}&days={days}"
    response_text = f"Прогноз на {days} дней для города {city}: {forecast_url}"
    
    # Отправка ссылки пользователю
    await bot.send_message(callback_query.from_user.id, response_text)

# Error handling for invalid routes or API failures
@router.error()
async def handle_errors(update, error):
    await bot.send_message(update.message.chat.id, "Ошибка! Проверьте данные и попробуйте снова.")

async def main():
    bot.delete_webhook(drop_pending_updates=True)
    
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())