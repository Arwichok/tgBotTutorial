import ssl
from os import getenv

from dotenv import load_dotenv
from aiohttp import BasicAuth


load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN')
SKIP_UPDATES = bool(getenv('SKIP_UPDATES') or True)
BOT_OWNER = int(getenv('BOT_OWNER') or 0)

PROXY_URL = getenv('PROXY_URL')
PROXY_PASS = getenv('PROXY_PASS', '')
PROXY_LOGIN = getenv('PROXY_LOGIN', '')
PROXY_AUTH = BasicAuth(PROXY_LOGIN, PROXY_PASS)

USE_WEBHOOK = bool(getenv('USE_WEBHOOK') or False)
WEBHOOK_HOST = getenv('WEBHOOK_HOST')
WEBHOOK_PORT = int(getenv('WEBHOOK_PORT') or 8443)
WEBHOOK_PATH = getenv('WEBHOOK_PATH')
APP_PORT = int(getenv('APP_PORT') or WEBHOOK_PORT)
APP_HOST = getenv('APP_HOST', 'localhost')
SSL_CERT = getenv('SSL_CERT')
SSL_KEY = getenv('SSL_KEY')

WEBHOOK_URL = f'https://{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}'
WEBHOOK_SERVER = {
    'host': APP_HOST,
    'port': APP_PORT,
    'webhook_path': WEBHOOK_PATH,
}
if SSL_CERT and SSL_KEY:
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(SSL_CERT, SSL_KEY)
    WEBHOOK_SERVER['ssl_context'] = context
