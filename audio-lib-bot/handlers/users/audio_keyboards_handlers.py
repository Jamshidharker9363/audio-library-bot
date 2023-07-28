from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext

from keyboards.default.menuKeyboards import menu
from states.state import get_state
from aiogram.types import Message
from loader import dp, bot
from keyboards.default.audio_keyboard import qorikeyboards, surakeyboards
from  data.data import qorilar, name_sura, name_qori


@dp.message_handler(Text("🕋🎧Audio Quran"))
async def start_command(message: Message, state: FSMContext):
    tugmalar = await qorikeyboards()
    text = "Qorilardan birini tanlashinggiz mumkin !\n"
    text += "Bosh sahifaga o'tish uchun /restart buyrug'ini bering"
    await message.answer(text, reply_markup=tugmalar)
    await state.set_state(get_state.qori)


@dp.message_handler(Text(equals=name_qori))
async def get_sura_command(message: Message, state: FSMContext):
    index = name_qori.index(message.text)
    tugmalar1 = await surakeyboards()
    await message.answer("Surani tanlang!", reply_markup=tugmalar1)
    qori_name = message.text
    await state.update_data(
        {
            "qori_ismi": qori_name,
            'index': index
        }
    )
    await state.set_state(get_state.sura)


@dp.message_handler(Text(equals=name_sura), state=get_state.sura)
async def send_audio_sura(message: Message, state: FSMContext):
    userid = message.from_user.id
    data = await state.get_data()
    get_qori_name = data['index']
    from_chat_id = '@bazaaudioquran'
    qori = qorilar[get_qori_name]
    for sura in qori:
        if sura['sura_name'] == message.text:
            await bot.forward_message(chat_id=userid, from_chat_id=from_chat_id, message_id=sura['sura_link'])
            break
    if message.text == '♻️Qorini almashtirish♻️':
        tugmalar = await qorikeyboards()
        await message.answer("Qorilardan birini tanlang", reply_markup=tugmalar)
        await state.set_state(get_state.qori)
    else:
        await message.answer("Bosh safifaga o'tish uchun /restart buyrug'ini bering")

@dp.message_handler(Text(equals=name_qori), state=get_state.qori)
async def change_qori_command(message: Message, state: FSMContext):
    index = name_qori.index(message.text)
    tugmalar1 = await surakeyboards()
    await message.answer("Surani tanlang!", reply_markup=tugmalar1)
    qori_name = message.text
    await state.update_data(
        {
            "qori_ismi": qori_name,
            'index': index
        }
    )
    await state.set_state(get_state.sura)


@dp.message_handler(Command('start'), state=get_state.sura)
async def resite_sura(message: Message, state: FSMContext):
    await message.answer("Kerakli bo'limni tanlang !", reply_markup=menu)
    await state.finish()

@dp.message_handler(Command('start'), state=get_state.qori)
async def resite_s(message: Message, state: FSMContext):
    await message.answer("Kerakli bo'limni tanlang !", reply_markup=menu)
    await state.finish()

@dp.message_handler(Command('restart'), state=get_state.sura)
async def resite_q(message: Message, state: FSMContext):
    await message.answer("Kerakli bo'limni tanlang !", reply_markup=menu)
    await state.finish()

@dp.message_handler(Command('restart'), state=get_state.qori)
async def resite_qori(message: Message, state: FSMContext):
    await message.answer("Kerakli bo'limni tanlang !", reply_markup=menu)
    await state.finish()

@dp.message_handler(Command('help'), state=get_state.qori)
async def resite_help(message: Message):
    text = "————————————————————————\n\n"
    text += "<b>Assalomu aleykum va raxmatullohi va barokatuh 😊</b>\n"
    text += "<b>@quranaudiolibrarybot ga hush kelibsiz !</b>\n\n"
    text += "➖➖➖➖➖➖➖➖➖➖\n\n"
    text += "<b>Bu bot orqali siz ko'plab qorilarni qiroatlari,</b>\n"
    text += "<b>O'zbek , Rus, Ingliz tilidagi tarjimalarini topishinggiz mumkin.</b>\n\n"
    text += "➖➖➖➖➖➖➖➖➖➖\n\n"
    text += "<b>Manfaatli bo'lgan bo'lsa dostlaringgizga ulashing.</b>\n"
    text += "<b>O'zinggizga kerakli bo'limni tanlashinggiz mumkin.</b>"
    await message.answer(text)

@dp.message_handler(Command('help'), state=get_state.sura)
async def resite_help(message: Message):
    text = "————————————————————————\n\n"
    text += "<b>Assalomu aleykum va raxmatullohi va barokatuh 😊</b>\n"
    text += "<b>@quranaudiolibrarybot ga hush kelibsiz !</b>\n\n"
    text += "➖➖➖➖➖➖➖➖➖➖\n\n"
    text += "<b>Bu bot orqali siz ko'plab qorilarni qiroatlari,</b>\n"
    text += "<b>O'zbek , Rus, Ingliz tilidagi tarjimalarini topishinggiz mumkin.</b>\n\n"
    text += "➖➖➖➖➖➖➖➖➖➖\n\n"
    text += "<b>Manfaatli bo'lgan bo'lsa dostlaringgizga ulashing.</b>\n"
    text += "<b>O'zinggizga kerakli bo'limni tanlashinggiz mumkin.</b>"
    await message.answer(text)
