from aiogram import types as ats

from misc import dp


@dp.message_handler(
    commands=['start'],
    commands_prefix='/!'
)
async def cmd_start(msg: ats.Message):
    await msg.answer('Hello you send !start or /start')


@dp.message_handler(text='some')
@dp.message_handler(commands=['some'])
async def some_start(msg: ats.Message):
    await msg.answer('Hello from some')
