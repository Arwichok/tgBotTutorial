from aiogram import types as ats
import aiogram.utils.markdown as md

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


@dp.message_handler(text='md')
async def md_test(msg: ats.Message):
    username = msg.from_user.username
    user_id = msg.from_user.id
    chat_id = msg.chat.id

    await msg.answer(
        f'Hello {md.hbold(username)}\n'
        f'Your id: {md.hcode(user_id)}\n'
        f'Chat id: {md.hcode(chat_id)}\n'

        f'''User mention {md.hlink(
            username,
            f'tg://user?id={user_id}'
        )}'''
    )


@dp.message_handler(is_reply=True)
async def test_is_reply(msg: ats.Message, reply):
    await msg.answer(f'Reply to {reply.text}')
