import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

dp = Dispatcher()

# Команда /start
@dp.message(Command('start'))
async def start_command(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Мой дневник")],
        [types.KeyboardButton(text="Купить ботов")],
        [types.KeyboardButton(text="Портфолио")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('Привет! это мой бот-визитка', reply_markup=keyboard)

# Мой дневник (добавлена inline-кнопка с ссылкой)
@dp.message(F.text == 'Мой дневник')
async def about_me_handler(message: types.Message):
    text = 'Рад, что ты спросил держи мой тгк'
    kb = [
        [types.InlineKeyboardButton(text="Перейти в дневник", url="https://t.me/+O1AyPb6vyBgzMzZi")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(text, reply_markup=keyboard)

# Купить ботов (inline-кнопка с ссылкой)
@dp.message(F.text == 'Купить ботов')
async def shop_handler(message: types.Message):
    text = 'Тут ты можешь купить ботов'
    kb = [
        [types.InlineKeyboardButton(text="Перейти в магазин", url="https://t.me/Bot_ShopROBOT")],
    ]
    # Исправлено: использовалось неправильное название аргумента
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(text, reply_markup=keyboard)

# Портфолио
@dp.message(F.text == 'Портфолио')
async def portfolio_handler(message: types.Message) -> None:
    await message.answer('Работаю с Python Aiogram3 SQLite\n'
                         'Боты в работе:\n@FeniX1ROBOT\n@Bot_ShopROBOT\n'
                         'Готовые боты:\n@AskorbinROBot\n@stepashka1564Bot')

# Запуск бота
async def main():
    bot = Bot(token="8792022664:AAE-U-kISO_5cmiP34ZfwFxXNlWUmyVLYpE")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
