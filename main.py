import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message) -> None:
    kb = [
        [types.KeyboardButton(text="Обо мне")],

        [
            types.KeyboardButton(text="Что смотрел"),
            types.KeyboardButton(text="Портфолио")
        ],
        [
            types.KeyboardButton(text="О тебе")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('Привет! это мой бот-визитка', reply_markup=keyboard)



@dp.message(F.text == 'Обо мне')
async def about_me_handler(message: types.Message) -> None:
    await message.answer('Рад, что ты спросил держи мой тгк\nhttps://t.me/+O1AyPb6vyBgzMzZi')

@dp.message(F.text == 'Что смотрел')
async def about_me_handler(message: types.Message) -> None:
    await message.answer('Рад, что ты спросил держи мой профиль на кинопоиск\nhttps://www.kinopoisk.ru/user/158986273/')


@dp.message(F.text == 'Портфолио')
async def portfolio_handler(message: types.Message) -> None:
    await message.answer('Работаю с Python Aiogram3 SQLite\nБоты в работе:\n@AskorbinROBot')


@dp.message(F.text == 'О тебе')
async def about_you_handler(message: types.Message) -> None:
    await message.answer(f'А тебя зовут {message.from_user.full_name}!')


async def main() -> None:
    token = "8758193390:AAFYGdpHf0M9T-i1yGT2PNJ4xt_M9Tllodo"
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
