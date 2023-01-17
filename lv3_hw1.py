from aiogram import Bot, Dispatcher, types, executor
import config
from random import randrange

bot = Bot(token = config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands = ["start"])
async def start(message: types.Message):
    await message.answer(f"Здраствуйте {message.from_user.full_name}Давай сыграем? Я загадал сифру от 1 до 3 угадывай")

    n = randrange(1,4)
    n = str(n)

    @dp.message_handler()
    async def echo_message(msg: types.Message):
        mess= msg.text

        if mess == n:
            await bot.send_message(msg.from_user.id, "Молодец ты угадал")
            
        else:
            await bot.send_message(msg.from_user.id, "Давай попробуй ещё раз")

executor.start_polling(dp)