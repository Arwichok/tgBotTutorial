# Echobot

В этом розделе мы создадим элементарного эхо бота. создадим файл `echo.py` и запишем туда этот код:

#### `echo.py`
```py
import logging
from aiogram import Bot, Dispatcher, executor

BOT_TOKEN = ''
logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(msg):
    await msg.answer(msg.text)


executor.start_polling(dp, skip_updates=True)
```

В переменную BOT_TOKEN вставим токен бота.

> Если у вас заблокирован https://api.telegram.org/ воспользуйтесь прокси добавив его в вызов `Bot(BOT_TOKEN, proxy='http://address:port')`, подробней будет далее в туториале


### Запускаем бота
    (venv) $ python echo.py
    INFO:aiogram:Bot: MyEverBestBot [@MyEverBestBot]
    WARNING:aiogram:Updates were skipped successfully.
    INFO:aiogram.dispatcher.dispatcher:Start polling.

Что бы остановить бота нажимаем клавиши `Ctrl+C`

    ^CINFO:aiogram.dispatcher.dispatcher:Stop polling...
    WARNING:aiogram:Goodbye!


### Что здесь происходит


Устанавливаем уровень логирования, что-бы видеть что происходит в программе через консоль:

```py
logging.basicConfig(level=logging.INFO)
```

Создаём обьекты бота и дисптачера, один для управления ботом, другой для работы с обновлениям:
```py
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
```

Регистрируем функцию `echo` что бы она срабатывала на все сообщения.
```py
@dp.message_handler()
async def echo(msg):
```

Зарегистрировать можно без декоратора:
```py
dp.register_message_handler(echo)
```

Функция отвечает тому пользователю кто написал, тот же текст:
```py
    await msg.answer(msg.text)
```

Запускаем бота с пропуском всех сообщений что были до запуска:

```py
executor.start_polling(dp, skip_updates=True)
```

[Предыдущая часть](00_welcome.md) | [Следующая часть](02_project.md)