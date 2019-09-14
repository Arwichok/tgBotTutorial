from os import getenv

from dotenv import load_dotenv
from aiohttp import BasicAuth

load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN')
SKIP_UPDATES = bool(getenv('SKIP_UPDATES', True))

PROXY_URL = getenv('PROXY_URL')
PROXY_PASS = getenv('PROXY_PASS', '')
PROXY_LOGIN = getenv('PROXY_LOGIN', '')
PROXY_AUTH = BasicAuth(PROXY_LOGIN, PROXY_PASS)
