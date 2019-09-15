# Фильтры обновлений

Фильтры помогают регистрировать функции на разные типы получаемых сообщений к примеру на текст и комманду отвечают разные функции. Здесь расмотрим встроенные фильтры и создадим свой.

## Contents

- [Text](#text)
- [ID](#id)
- [RegExp](#RegExp)
- [Tags](#Tags)
- [AdminFilter](#adminfilter)
- [Content Types](#content-types)
- [Commands](#Commands)
  - [Command Classes](#command-classes)
  - [Commands prefix](#commands-prefix)
  - [Regexp command](#regexp-commands)
  - [DeepLink](#deeplink)
- [MyFilter](#my-filter)
- [Two registrators](#two-registrators)


>`echo` в коде мы удалим, так как функции проверяются по порядку очереди регистрации, если хендлер зарегистрирован без аргументов первым, то все сообщения будут отправлятся в него, если последним, тогда будет на всё что не отвечает фильтрам в предидущих.

Так же для типизации будем использовать типы от либы.


## Text
#### bot/hanlders/messages.py
```py
from aiogram import types as ats

from misc import dp


@dp.message_handler(text='1')
async def one(msg: ats.Message):
    await msg.answer('You send 1')


@dp.message_handler(text_startswith='t')
async def two(msg: ats.Message):
    await msg.answer(f'Text startswith: t | {msg.text}')
```

Для текста есть такие встроенные фильтры:
- `text` - проверка на соответсвие текста
- `text_startswith` - если текст начинается с такого отрезка
- `text_endsiwith` - если текст оканчивается на это
- `text_contains` - если в тексте присутсвует часть

## ID

Для проверки id от получателя используем `user_id` и `chat_id`:

```py
@dp.message_handler(text='admin', user_id=(123456,))
async def user_id_test(msg: ats.Message):
    # Отправит сообщение только пользователю с id 123456
    await msg.answer('Hello Admin')
```

## RegExp
Для проверки текста сообщения по регулярному выражению используется `regexp`

```py
@dp.message_handler(regexp='(^cat|puss)')
async def regexp_test(msg: ats.Message, regexp):
    await msg.answer(f'Your cat\'s is {regexp[0]}')
```

## Tags

`hashtags`, `cashtags` - позваляют получать уведомление на присутсвие тегов в тексте с префиксом `#`, `$`

```py
@dp.message_handler(hashtags=['lom'])
async def hashtag_test(msg: ats.Message):
    await msg.answer('Hashtag Lom')
```


## Commands

Для команд у нас будет `commands.py`, создадим файл для этого и добавим в импорт `bot/__main__.py`

Комманды будем писать в отдельном модуле `commands`    
Создадим `bot/handlers/commands.py`


```py
# `bot/__main__.py`
from handlers import (
    messages,
    commands
)
```

```py
# `bot/hanlders/commands.py`
from aiogram import types as ats

from misc import dp


@dp.message_handler(commands=['start'], commands_prefix='!/')
async def cmd_start(msg: ats.Message):
    await msg.answer('Hello you send /start or !start')
```

Комманды можно вводить несколько на один хендлер.

По умолчанию `commands_prefix='/'`, но вы можете изменить если комманды могут конфликтовать с другими ботами в чатах или по желанию.




## Two registrators

Если вы хотите зарегистрировать один хендлер на несколько разных фильтров тогда нужно регистрировать его два раза, так как если сделать `(commands=['some'], text='some')`, от так никода не сработает, для решения этой проблемы можем использовать:

```py
@dp.message_handler(text='some')
@dp.message_handler(commands=['some'])
async def some_start(msg: ats.Message):
    await msg.answer('Hello from some')
```


# TODO 
- Создание простых функций фильтров
  - передача True
  - Передача Dict
- создание фильтра от фабрики фильтров
