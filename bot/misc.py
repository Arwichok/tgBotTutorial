import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.executor import Executor

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
executor = Executor(dp)
