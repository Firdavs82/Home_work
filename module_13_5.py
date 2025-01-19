from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import asyncio

api = 'XXX'
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button2 = KeyboardButton(text="Рассчитать")
button = KeyboardButton(text="Информация")

kb.insert(button2)
kb.insert(button)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text= "Информация")
async def info(message):
    await message.answer('Данный бот помогает расчитать норму калорий в день для мужчин и женщин')

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup= kb)

@dp.message_handler(text=['Рассчитать '])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = float(data['age'])
    weight = float(data['weight'])
    growth = float(data['growth'])
    calories_man = 10 * weight + 6.25 * growth - 5 * age + 5
    calories_woman = 10 * weight + 6.25 * growth - 5 * age -161
    await message.answer(f'Норма калорий мужчин: {calories_man} ')
    await message.answer(f'Норма калорий женщин: {calories_woman} ')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)