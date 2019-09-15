import re

from aiogram import types as ats, filters

from misc import dp


@dp.message_handler(commands=['help'])
async def cmd_help(msg: ats.Message):
    await msg.answer('Hello, i MyEverBestBot')


@dp.message_handler(filters.CommandPrivacy())
async def cmd_privacy(msg: ats.Message):
    await msg.answer('Privacy')

@dp.message_handler(commands=['test'], commands_prefix='/!')
async def cmd_test(msg: ats.Message):
    await msg.answer('Test')


@dp.message_handler(regexp_commands=[r'r_(\d+)'])
async def cmd_r(msg: ats.Message, regexp_command):
    await msg.answer(f'ref is {regexp_command[1]}')


@dp.message_handler(
    filters.CommandStart(re.compile(r'u(\d+)')))
async def cmd_start(msg: ats.Message, deep_link):
    await msg.answer(f'Deep link u is {deep_link[1]}')


@dp.message_handler(text='some')
@dp.message_handler(commands=['some'])
async def some_start(msg: ats.Message):
    await msg.answer('Hello from some')
