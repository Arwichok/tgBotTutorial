import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.executor import Executor

from config import BOT_TOKEN, PROXY_AUTH, PROXY_URL, SKIP_UPDATES

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=BOT_TOKEN, 
    proxy=PROXY_URL, 
    proxy_auth=PROXY_AUTH
)
dp = Dispatcher(bot)
executor = Executor(dp, skip_updates=SKIP_UPDATES)
