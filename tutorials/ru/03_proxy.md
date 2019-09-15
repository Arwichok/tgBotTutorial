# Настраиваем Прокси

По дефолту мы можем использувать `http` прокси. Что бы использовать `socks`-прокси нужно установить `aiohttp_socks`

Если требуется использовать логин и пароль для прокси добавим авторизацию в код

#### bot/config.py
```py
from aiohttp import BasicAuth

...

PROXY_PASS = getenv('PROXY_PASS', '')
PROXY_LOGIN = getenv('PROXY_LOGIN', '')
PROXY_AUTH = BasicAuth(PROXY_LOGIN, PROXY_PASS)
```

#### bot/misc.py
```py
...

from config import BOT_TOKEN, PROXY_AUTH, PROXY_URL, ...

...
bot = Bot(
    token=BOT_TOKEN,
    proxy=PROXY_URL,
    proxy_auth=PROXY_AUTH
)
...
```

[Предыдущая часть](02_project) | [Следующая часть](04_filters)