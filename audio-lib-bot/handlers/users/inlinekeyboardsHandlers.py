from aiogram.types import Message
from loader import dp
from keyboards.inline.inlineKeyboards import tugmalar1, tugmalar2, tugmalar3, tugmalar4, tugmalar5, tugmalar6, \
    tugmalar7, tugmalar8, tugmalar9


@dp.message_handler(text_contains="Mahmud Xalil Al-Husariy")
async def celectcatogory1(message: Message):
    await message.answer(f"kerakli bo'limni tanlang !", reply_markup=tugmalar1)

@dp.message_handler(text_contains="Mishari Rashid Al-Afasiy")
async def celectcatogory2(message: Message):
    await message.answer(f"kerakli bo'limni tanlang !", reply_markup=tugmalar2)

@dp.message_handler(text_contains="Abdurahmon As-Sudays")
async def celectcatogory3(message: Message):
    await message.answer(f"kerakli bo'limni tanlang !", reply_markup=tugmalar3)

@dp.message_handler(text_contains="Saad Al-G'omidiy")
async def celectcatogory4(message: Message):
    await message.answer(f"kerakli bo'limni tanlang !", reply_markup=tugmalar4)

@dp.message_handler(text_contains="Maher Al-Muayqli")
async def celectcatogory5(message: Message):
    await message.answer(f"kerakli bo'limni tanlang !", reply_markup=tugmalar5)

@dp.message_handler(text_contains="Sheyx Muhammad Sodiq")
async def celectcatogory5(message: Message):
    await message.answer(f"kerakli bo'limni tanlang !", reply_markup=tugmalar6)

@dp.message_handler(text_contains="Sheyx Al-Mansur")
async def celectcatogory5(message: Message):
    await message.answer(f"kerakli bo'limni tanlang !", reply_markup=tugmalar7)

@dp.message_handler(text_contains="🇷🇺 Rus tilida | на русском")
async def celectcatogory5(message: Message):
    await message.answer(f"kerakli bo'limni tanlang !", reply_markup=tugmalar8)

@dp.message_handler(text_contains="🇬🇧 Ingliz tilida | In English")
async def celectcatogory5(message: Message):
    await message.answer(f"kerakli bo'limni tanlang !", reply_markup=tugmalar9)