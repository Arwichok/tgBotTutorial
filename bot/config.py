import ssl
from os import getenv as g

from dotenv import load_dotenv
from aiohttp import BasicAuth


load_dotenv()

BOT_TOKEN = g('BOT_TOKEN')
SKIP_UPDATES = bool(g('SKIP_UPDATES') or True)
BOT_OWNER = int(g('BOT_OWNER') or 0)

PROXY_URL = g('PROXY_URL')
PROXY_PASS = g('PROXY_PASS', '')
PROXY_LOGIN = g('PROXY_LOGIN', '')
PROXY_AUTH = BasicAuth(PROXY_LOGIN, PROXY_PASS)

USE_WEBHOOK = bool(g('USE_WEBHOOK') or False)
WEBHOOK_HOST = g('WEBHOOK_HOST')
WEBHOOK_PORT = int(g('WEBHOOK_PORT') or 8443)
WEBHOOK_PATH = g('WEBHOOK_PATH')
APP_PORT = int(g('APP_PORT') or WEBHOOK_PORT)
APP_HOST = g('APP_HOST', 'localhost')
SSL_CERT = g('SSL_CERT')
SSL_KEY = g('SSL_KEY')

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
