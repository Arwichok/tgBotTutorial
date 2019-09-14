import logging
from aiogram import Bot, Dispatcher, executor

BOT_TOKEN = ''
logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN, proxy='')
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(msg):
    await msg.answer(msg.text)


executor.start_polling(dp, skip_updates=True)
