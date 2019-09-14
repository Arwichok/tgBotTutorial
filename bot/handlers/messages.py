from misc import dp


@dp.message_handler()
async def echo(msg):
    await msg.answer(msg.text)
