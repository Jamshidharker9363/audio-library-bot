from aiogram.dispatcher.filters import  Command, Text
from aiogram.types import Message
from keyboards.default.menuKeyboards import menu, tafsirmenu
from loader import dp


@dp.message_handler(Text("🕌Tafsir"))
async def tafsir_menu(message: Message):
    await message.answer("Kimning tafsiri kerak !", reply_markup=tafsirmenu)

@dp.message_handler(Text("🔝Bosh sahifa"))
async def tafsir_menu(message: Message):
    text = "Bosh sahifaga o'tdinggiz !\n"
    text += "Kerakli bo'limni tanlashinggiz mumkin ."
    await message.answer(text, reply_markup=menu)

@dp.message_handler(Text("📞 ☎️Admin bilan aloqa"))
async def admin_aloqa(message: Message):
    text = "————————————————————————\n\n"
    text += "<b>Assalomu aleykum va raxmatullohi va barokatuh 😊</b> \n"
    text += "<b>@alquronuzBot ga hush kelibsiz !</b>\n\n"
    text += "➖➖➖➖➖➖➖➖➖➖\n\n"
    text += "<b>Taklif va muammolar bo'lsaadmin bilan bog'laning </b>\n"
    text += "<b>Bog'laninish uchun admin @Jamshidharker9363</b>\n\n"
    text += "➖➖➖➖➖➖➖➖➖➖\n\n"
    text += "<b>Bizning ijtimoiy tarmoqlar !</b>\n"
    text += "https://taplink.cc/jamshidharker9363"
    await message.answer(text, reply_markup=menu, disable_web_page_preview=True)

@dp.message_handler(Text("⛑ help"))
async def help_button_command(message: Message):
    text = "————————————————————————\n\n"
    text += "<b>Assalomu aleykum va raxmatullohi va barokatuh 😊</b>\n"
    text += "<b>@alquronuzBot ga hush kelibsiz !</b>\n\n"
    text += "➖➖➖➖➖➖➖➖➖➖\n\n"
    text += "<b>Bu bot orqali siz ko'plab qorilarni qiroatlari,</b>\n"
    text += "<b>O'zbek , Rus, Ingliz tilidagi tarjimalarini topishinggiz mumkin.</b>\n\n"
    text += "➖➖➖➖➖➖➖➖➖➖\n\n"
    text += "<b>Manfaatli bo'lgan bo'lsa dostlaringgizga ulashing.</b>\n"
    text += "<b>O'zinggizga kerakli bo'limni tanlashinggiz mumkin.</b>"
    await message.answer(text)

@dp.message_handler(Command('help'))
async def help_command(message: Message):
    text = "————————————————————————\n\n"
    text += "<b>Assalomu aleykum va raxmatullohi va barokatuh 😊</b>\n"
    text += "<b>@alquronuzBot ga hush kelibsiz !</b>\n\n"
    text += "➖➖➖➖➖➖➖➖➖➖\n\n"
    text += "<b>Bu bot orqali siz ko'plab qorilarni qiroatlari,</b>\n"
    text += "<b>O'zbek , Rus, Ingliz tilidagi tarjimalarini topishinggiz mumkin.</b>\n\n"
    text += "➖➖➖➖➖➖➖➖➖➖\n\n"
    text += "<b>Manfaatli bo'lgan bo'lsa dostlaringgizga ulashing.</b>\n"
    text += "<b>O'zinggizga kerakli bo'limni tanlashinggiz mumkin.</b>"
    await message.answer(text)

