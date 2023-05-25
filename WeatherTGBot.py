from aiogram import Bot, Dispatcher, executor, types
import python_weather
import asyncio

# bot init
bot = Bot(token='6017418872:AAE3ntnQ9K76sdiYSywgg76N-vBlRKOh_dk')
dp = Dispatcher(bot)
client = python_weather.Client(unit=python_weather.METRIC)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет! Я погодный бот. Просто напиши мне название города и я расскажу тебе о погоде.')

# @dp.message_handler(commands=['Привет'])
# async def start_command(message: types.Message):
#   await message.reply('Привет! Я погодный бот. Просто напиши мне название города и я расскажу тебе о погоде.')

# Обработчик текстовых сообщений
@dp.message_handler()
async def get_weather(message: types.Message):
    town = message.text
    weather = await client.get(town)

    if weather.current:
        resp_msg = f"Погода в городе {town}:\n"
        resp_msg += f"Текущая температура: {weather.current.temperature}°C\n"
        resp_msg += f"Ощущается как: {weather.current.feels_like}°C\n"
        resp_msg += f"Скорость ветра: {weather.current.wind_speed} м/c\n"
        resp_msg += f"Влажность: {weather.current.humidity}%"
    else:
        resp_msg = f"Не удалось получить информацию о погоде для города {town}."

    await message.answer(resp_msg)

# Обработчик команды /stop
@dp.message_handler(commands=['stop'])
async def stop_command(message: types.Message):
    await message.reply('Бот остановлен.')
    await bot.close()
    await dp.storage.close()
    await dp.storage.wait_closed()
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
# Запуск бота
# async def on_startup(dp):
#    await bot.send_message(chat_id='YOUR_CHAT_ID', text='Бот запущен')

# if __name__ == "__main__":
#    executor.start_polling(dp, skip_updates=True)
