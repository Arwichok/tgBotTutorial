from os import getenv

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN')
PROXY_URL = getenv('PROXY_URL')
SKIP_UPDATES = bool(getenv('SKIP_UPDATES', True))
