import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.executor import Executor
from aiogram.types import ParseMode as pm

from config import BOT_TOKEN, PROXY_AUTH, PROXY_URL, SKIP_UPDATES

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=BOT_TOKEN, 
    proxy=PROXY_URL, 
    proxy_auth=PROXY_AUTH,
    parse_mode=pm.HTML
)
dp = Dispatcher(bot)
executor = Executor(dp, skip_updates=SKIP_UPDATES)
