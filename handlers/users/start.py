import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import db, bot
from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Добавляем пользователей в базу
    try:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )
        await message.answer(f"Добро пожаловать! {name}\n\n"
                             f"🤖 Я бот который поможет ....\n\n"
                             f"🤝 Заказать похожего или совсем иного бота? Свяжитесь с разработчиком <a href='https://t.me/zufar_ik'>Zufar</a>")
        # Оповещаем админа
        count = await db.count_users()[0]
        msg = f"{message.from_user.full_name} добавлен в базу пользователей.\nВ базе есть {count} людей."
        await bot.send_message(chat_id=ADMINS[0], text=msg)


    except asyncpg.exceptions.UniqueViolationError:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} в базе имелся раньше")
        await message.answer(f"Добро пожаловать! {name}\n\n"
                             f"🤖 Я бот который поможет ....\n\n"
                             f"🤝 Заказать похожего или совсем иного бота? Свяжитесь с разработчиком <a href='https://t.me/zufar_ik'>Zufar</a>",)

