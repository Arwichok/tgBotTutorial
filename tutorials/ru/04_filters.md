# Filters


Фильтры помогают регистрировать функции на разные типы получаемых сообщений к примеру на текст и комманду отвечают разные функции. Здесь расмотрим встроенные фильтры и создадим свой.

# Contents

- [Filters](#filters)
- [Contents](#contents)
- [Text](#text)
  - [ID](#id)
  - [RegExp](#regexp)
  - [Tags](#tags)
- [Commands](#commands)
  - [Command Classes](#command-classes)
  - [Commands prefix](#commands-prefix)
  - [RegExp Commands](#regexp-commands)
  - [DeepLink](#deeplink)
- [Two registrators](#two-registrators)
- [MyFilter](#myfilter)
  - [Castom](#castom)
  - [Factory](#factory)
  - [Pass data](#pass-data)




>`echo` в коде мы удалим, так как функции проверяются по порядку очереди регистрации, если хендлер зарегистрирован без аргументов первым, то все сообщения будут отправляться в него, если последним, тогда будет на всё что не отвечает фильтрам в предыдущих.

Так же для типизации будем использовать типы от либы.


# Text
```py
# bot/hanlders/messages.py
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


# Commands

Для команд у нас будет `commands.py`, создадим файл для этого и добавим в импорт `bot/__main__.py`

Комманды будем писать в отдельном модуле `commands`    
Создадим `bot/handlers/commands.py`

add `commands`

```py
# `bot/__main__.py`
from handlers import (
    messages,
    commands
)
```

```py
@dp.message_handler(commands=['help'])
async def start(msg: ats.Message):
    await msg.answer('Hello i TestBot')
```

## Command Classes

```py
from aiogram import filters
...
@dp.message_handler(filters.CommandSettings())
async def start(msg: ats.Message):
    await msg.answer('Settings')
```

`start` == **CommandStart**  
`help` == **CommandHelp**  
`settings` == **CommandSettings**  
`privacy` == **CommandPrivacy**  

## Commands prefix

```py
@dp.message(commands=['test'], commands_prefix='/!')
async def help(msg: ats.Message):
    # answer when message is /test or !test
    await msg.answer('Test')
```

## RegExp Commands

```py
@dp.message_handler(regexp_commands=[r'r_(\d+)'])
async def r_(msg: ats.Message, regexp_command):
    await msg.answer(f'ref is {regexp_command[1]}')
```

## DeepLink
Теперь можно делать ссылки типа    
https://t.me/MyEverBestBot?start=u34

```py
@dp.message_handler(filters.CommandStart(re.compile(r'u(\d+)')))
async def cmd_start(msg: ats.Message, deep_link):
    await msg.answer(f'Deep link u is {deep_link[1]}')
```

# Two registrators

Регистрация двух взаимоисключающих фильтров на один хендлер

```py
@dp.message_handler(text='some')
@dp.message_handler(commands=['some'])
async def some_start(msg: ats.Message):
    await msg.answer('Hello from some')
```


# MyFilter

## Castom
```py
@dp.message_handler(lambda m: m.text == 'foo')
```

## Factory

```py
from aiogram.filter import BoundFilter
from aiogram import types as ats

from misc import bot, dp

class MyFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin
    
    async def check(self, msg: ats.Message):
        member = await bot.get_chat_member(
            msg.chat.id,
            msg.from_user.id)
        return member.is_admin()

dp.filters_factory.bind(MyFilter)

...

@dp.message_handler(is_admin=True)
async def is_admin(msg: ats.Message):
    await msg.answer('Answer if check() return True')
```

## Pass data

```py
async def my_filter(msg: ats.Message):
    # do something here
    return {'foo': 'bar'}


@dp.message_handler(my_filter)
async def test_my_filter(msg: ats.Message, foo):
    await msg.answer(f'foo is {foo}')
```

[Предыдущая часть](03_proxy.md)