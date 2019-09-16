# Formatting

# Contents

- [Formatting](#formatting)
- [Contents](#contents)
- [Bot Formatting](#bot-formatting)

BotsApi позволяет форматировать текст в разные стили, бибилиотека добавляет свои методы для прощего форматирования

# Bot Formatting

```py
...
from aiogram.utils.markdown as md
from aiogram.types import ParseMode as pm
...

bot = Bot(BOT_TOKEN, parse_mode=pm.HTML)
...

@dp.message_handler(text='md')
async def md_test(msg: ats.Message):
    username = msg.from_user.username
    user_id = msg.from_user.id
    chat_id = msg.chat.id

    await msg.answer(
        f'Hello {md.hbold(username)}\n'
        f'Your id: {md.hcode(user_id)}\n'
        f'Chat id: {md.hcode(chat_id)}\n'
        f'''User mention {md.hlink(
            username,
            f'tg://user?id={user_id}'
        )}'''
    )
```

| Type | Markdown | HTML | Example |
|-|-|-|-|
 **Bold**            | `bold`   | `hbold`   | `('Bold')`
 _Italic_            | `italic` | `hitalic` | `('Italic')`
 [URL](https://t.me) | `link`   | `hlink`   | `('URL', 'https://t.me')`
 Mention             | `link`   | `hlink`   | `('Username', 'tg://user?=12345')`
 `Inline-code`       | `pre`    | `hpre`    | `('Inline-code')`
 ```Code```          | `code`   | `hcode`   | `('Code')`
