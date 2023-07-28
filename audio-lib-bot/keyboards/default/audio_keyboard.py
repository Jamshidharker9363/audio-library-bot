from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.data import name_sura, name_qori

async def surakeyboards():
    keyboard =ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for item in name_sura:
        s = item
        tugma = KeyboardButton(s)
        keyboard.insert(tugma)
    return keyboard


async def qorikeyboards():
    keybordqori = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    for qori in name_qori:
        t = qori
        tugmaqori = KeyboardButton(t)
        keybordqori.insert(tugmaqori)
    return keybordqori


