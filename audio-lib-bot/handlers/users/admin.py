import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Command

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(Command("allusers"), user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        try:
            await bot.send_message(chat_id=user_id, text="botda yangilanish bo'ldi iltimos /start buyrug'ini bosing!")
            await asyncio.sleep(0.05)
        except Exception as err:
            db.delete_block_user(user_id)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")