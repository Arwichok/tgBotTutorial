# Создаём проект

По мере создания бота нам прийдется разделить код на части, что-бы не тулить всё в один файл, в этой части я покажу пример, а делать вам так же или нет это ваш выбор.

Здесь мы используем библиотеку `dotenv`
поэтому скачаем и добавим её в `requirements.txt`

### Файловая структура проекта
```bash
bot/
    hanlders/
        messages.py
    __main__.py
    misc.py
    config.py
.gitignore
.env
env
venv/
requirements.txt
```

#### `.env` and `env`:
```txt
BOT_TOKEN=<TOKEN>
SKIP_UPDATES=True

PROXY_URL=http://ip:port
```
в `.env` введите настоящие данные

#### `bot/config.py`
```py
from os import getenv

import dotenv


dotenv.load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN')
SKIP_UPDATES = bool(getenv('SKIP_UPDATES', True))

PROXY_URL = getenv('PROXY_URL')
```

#### `bot/misc.py`
```py
import logging

from aiogram import Bot, Dispatcher
from aiogram.executor import Executor

from config import BOT_TOKEN, PROXY_URL, SKIP_UPDATES


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)
executor = Executor(dp, skip_updates=SKIP_UPDATES)
```

#### `bot/handlers/messages.py`
```py
from misc import dp


@dp.message_handler()
async def echo(msg):
    await msg.answer(msg.text)
```


#### `bot/__main__.py`
```py
from misc import executor
from handlers import (
    messages
)


executor.start_polling()
```

## Запуск бота

    $ python bot



[Предыдущая часть](01_echo) | [Следующая часть](03_proxy)