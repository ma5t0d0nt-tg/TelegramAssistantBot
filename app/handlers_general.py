import pprint

from aiogram import F, Router
from aiogram.types import Message, TelegramObject, ChatFullInfo, BotCommand, ReactionTypeEmoji
from aiogram.filters import CommandStart, Command
from aiogram.enums.parse_mode import ParseMode

import configparser

from typing import Callable
import sys
import json

from config.parser_config_admin import get_status_bot, set_active_bot, set_inactive_bot, get_owner_user_id

router = Router()


@router.message(Command("start"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        await message.reply(text=f"Здравствуйте, {message.from_user.first_name}.\n"
                                 f"Я бот, предназаченный для автоматических ответов в личных чатах Telegram Messenger.")


@router.message(Command("author"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        await message.reply(text=f"Ссылка на автора данного бота\nhttps://t.me/m/KPzniy-vOTcy")


@router.message(Command("pic"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        await message.reply(
            text=f"Ссылка на аватар бота: https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi2.wp.com"
                 f"%2Fuangonline.com%2Fwp-content%2Fuploads%2F2018%2F09%2Fbisnis-berbasis-tekno.jpg%3Ffit%3D1200"
                 f"%252C794%26ssl%3D1&lr=11256&pos=0&rpt=simage&text=telegram%20bot%20assistant%20pic")


@router.message(Command("description"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        await message.reply(text="Этот бот работает как менеджер чатов для личных переписок с его создателем. "
                                 "Чтобы использовать чат-бота, используйте команду /author. Вам ответит чат-бот.")


# пасхалка
@router.message(Command("this_en"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        this_text = """
        <blockquote><i>The Zen of Python, by Tim Peters
        
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!</i></blockquote>
        """
        await message.reply(text=this_text, parse_mode=ParseMode.HTML)


# пасхалка
@router.message(Command("this_ru"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        this_text = """
        <blockquote><i>Красивое лучше, чем уродливое.
        
Явное лучше, чем неявное.
Простое лучше, чем сложное.
Сложное лучше, чем запутанное.
Плоское лучше, чем вложенное.
Разреженное лучше, чем плотное.
Читаемость имеет значение.
Особые случаи не настолько особые, чтобы нарушать правила.
При этом практичность важнее безупречности.
Ошибки никогда не должны замалчиваться.
Если они не замалчиваются явно.
Встретив двусмысленность, отбрось искушение угадать.
Должен существовать один и, желательно, только один очевидный способ сделать это.
Хотя он поначалу может быть и не очевиден, если вы не голландец.
Сейчас лучше, чем никогда.
Хотя никогда зачастую лучше, чем прямо сейчас.
Если реализацию сложно объяснить, то это плохая идея.
Если реализацию легко объяснить, то идея, возможно хороша.
Пространства имён - отличная штука! Будем делать их больше!
        </i></blockquote>
        """
        await message.reply(text=this_text, parse_mode=ParseMode.HTML)
