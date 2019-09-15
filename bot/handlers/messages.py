from aiogram import types as ats

from misc import dp


@dp.message_handler(text='1')
async def one(msg: ats.Message):
    await msg.answer('You send 1')


@dp.message_handler(text_startswith='t')
async def two(msg: ats.Message):
    await msg.answer(f'Text startswith: t | {msg.text}')


@dp.message_handler(text='admin', user_id=(329398814,))
async def user_id_test(msg: ats):
    await msg.answer('hello 329398814')


@dp.message_handler(regexp='(^cat|puss)')
async def regexp_test(msg: ats.Message, regexp):
    await msg.answer(f'Your cat\'s is {regexp[0]}')


@dp.message_handler(hashtags=['lom'])
async def hashtag_test(msg: ats.Message):
    await msg.answer('Hashtag Lom')