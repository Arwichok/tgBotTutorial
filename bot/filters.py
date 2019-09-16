from aiogram.dispatcher.filters import BoundFilter
from aiogram import types as ats

from misc import dp


class IsReply(BoundFilter):
    key = 'is_reply'

    def __init__(self, is_reply):
        self.is_reply = is_reply

    async def check(self, msg: ats.Message):
        if msg.reply_to_message:
            return {'reply': msg.reply_to_message}


dp.filters_factory.bind(IsReply)
