# Начало

В этом туториале мы научимся делать бота на библиотеке Aiogram в Python 3

----------------
#### Установка Python

Для работы с библиотекой aiogram требуется наличие Python 3.7, если версия младше или вообще нету нужно установить отсносительно вашей ОС, скачать можете на сайте python https://www.python.org/downloads/

Проверить версию можно через команду в терминале `python3 -V`, если python 3 один тогда `python -V`

    $ python3
    Python 3.7.4

#### Создадим папку проекта

    $ mkdir project
    $ cd project

#### Виртуальная среда

Для работы с пакетамы питона поставим виртуальную среду:

    $ python -m venv venv

и запустим:

    $ source venv/bin/activate
    (venv) $ _

#### Скачиваем python .gitignore

Если будете работать с `git` скачаем .gitignore
[отсюда](https://www.gitignore.io/api/python) и сохраним как  `.gitignore`

Или можете через терминал

    $ wget -O .gitignore https://www.gitignore.io/api/python


#### Устананавливаем aiogram, uvloop, ujson

Установим **aiogram**:

    (venv) $ pip install -U aiogram

Либа часто обновляется поэтому можете установить прямо с гита dev версию:

    (venv) $ pip install git+https://github.com/aiogram/aiogram.git

Автор рекомендует для скорости работы установить `uvloop` и `ujson`:

    (venv) $ pip install -U uvloop ujson


Создадим и запишемм в файл `requirements.txt`:
```
aiogram<3
uvloop
ujson
```

#### Создаём бота в  [@BotFather](https://t.me/BotFather)

Что-бы создать токен бота нам понадобится обратится к боту [@BotFather](https://t.me/BotFather):

Будем отправлять боту такие сообщения по очереди:
1. Комманду **/newbot**
2. Название бота
3. Домен бота который должен заканчиватся на `bot`

Мы получим токен бота

Пример: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`

Желательно никому не передавать этот токен, если уж произошла утечка то его можно изменить в настройках [@BotFather](https://t.me/BotFather)

Написать /mybots

`@mybot > API Token > Revoke current token`

#### Ссылки

Подробней почитать о создании ботов (en) https://core.telegram.org/bots/api

~~[Документация по aiogram](https://aiogram.readthedocs.io/en/latest/)~~ )

Я в телеграмме [@Arwichok](https://t.me/arwichok)

Русский чат по aiogram [@aiogram_ru](https://t.me/aiogram_ru)


[Следующая часть](01_echo.md)