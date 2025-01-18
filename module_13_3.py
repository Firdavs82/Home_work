from aiogram  import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7829054183:AAFw5-4PRDW8pFjauaqVDEe7oTBQuXZGoko"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text= ['Привет'])
async def text_message(message):
    await message.answer('Введите команду /start, чтобы начать общаться')

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)