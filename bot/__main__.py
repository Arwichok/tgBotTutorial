from aiogram import Dispatcher

from misc import executor
import filters
from handlers import (
    messages,
    commands,
)
from config import (
    USE_WEBHOOK,
    WEBHOOK_SERVER, 
    WEBHOOK_URL, 
    SSL_CERT
)


async def rm_webhook(dp: Dispatcher):
    await dp.bot.delete_webhook()


async def set_webhook(dp: Dispatcher):
    cert = open(SSL_CERT, 'rb') if SSL_CERT else None
    await dp.bot.set_webhook(WEBHOOK_URL, certificate=cert)


executor.on_startup(set_webhook, polling=False)
executor.on_startup(rm_webhook, webhook=False)
executor.on_shutdown(rm_webhook, polling=False)

if USE_WEBHOOK:
    executor.start_webhook(**WEBHOOK_SERVER)
else:
    executor.start_polling()
