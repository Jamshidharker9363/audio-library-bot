from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp
import requests
import asyncio


@dp.callback_query_handler(text="Sheyx_Muhammad_Sodiq_toliq_sura")
async def verse_answer(call: CallbackQuery, state: FSMContext,):
    await call.message.answer("Sura raqamini kiritng!")
    await call.answer(cache_time=1)
    await call.message.delete()
    await state.set_state("sura1")
@dp.message_handler(state="sura1")
async def get_sura(message: Message, state: FSMContext):
    try:
        msg = int(message.text)
        tafsir = 'uzb-muhammadsodikmu'
        url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{msg}.json"
        r = requests.get(url_sura)
        data = r.json()
        for start, verse in enumerate(data['chapter']):
            await message.answer(text=f"{start + 1}-oyat\n{verse['text']}")
            await asyncio.sleep(2)
        await state.finish()
    except Exception as err:
        await message.answer("Kiritishdagi hatolik iltimos qaytadan urinib ko'ring !")
        await state.finish()

@dp.callback_query_handler(text='Sheyx_Muhammad_Sodiq_oyat')
async def getSura(call:CallbackQuery,state: FSMContext):
    await call.message.delete()
    await call.message.answer("Sura raqamini kiriting !")
    await call.answer(cache_time=1)
    await state.set_state('sura')
@dp.message_handler(state='sura')
async def suraniOlish (message: Message, state:FSMContext):
    sura = message.text
    await state.update_data(
        {"sura": sura}
    )
    await message.answer("Iltimos oyat raqamini kiriting !")
    await state.set_state('oyat')
@dp.message_handler(state='oyat')
async def oyatniolish(message: Message, state: FSMContext):
    try:
        oyat = message.text
        await state.update_data(
            {"oyat": oyat}
        )

        malumot = await state.get_data()
        sura = malumot.get('sura')
        oyat = malumot.get('oyat')

        tafsir = 'uzb-muhammadsodikmu'
        url_sura1 = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"
        r = requests.get(url_sura1)
        malumot = r.json()
        await message.answer(text=f"{malumot['text']}")
        await state.finish()
    except:
        await message.answer("Kiritishda xatolik yuz berdi. Iltimos qaytadan urinib ko'ring !")
        await state.finish()
# Alouddin Mansur tafsiri


@dp.callback_query_handler(text="Sheyx_Al_Mansur_toliq_sura")
async def verse_answer(call: CallbackQuery, state: FSMContext,):
    await call.message.answer("Sura raqamini kiritng!")
    await call.answer(cache_time=1)
    await call.message.delete()
    await state.set_state("sura2")
@dp.message_handler(state="sura2")
async def get_sura(message: Message, state: FSMContext):
    try:
        msg = int(message.text)
        tafsir = "uzb-alauddinmansour"
        url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{msg}.json"
        r = requests.get(url_sura)
        data = r.json()
        for start, verse in enumerate(data['chapter']):
            await message.answer(text=f"{start + 1}-oyat\n{verse['text']}")
            await asyncio.sleep(2)
        await state.finish()
    except:
        await message.answer("Son kiritishda hatolik yuz berdi. Iltimos qaytadan urinib ko'ring .")
        await state.finish()

@dp.callback_query_handler(text='Sheyx_Al_Mansur_oyat')
async def getSura(call:CallbackQuery,state: FSMContext):
    await call.message.delete()
    await call.message.answer("Sura raqamini kiriting !")
    await call.answer(cache_time=1)
    await state.set_state('sura')
@dp.message_handler(state='sura')
async def suraniOlish (message: Message, state:FSMContext):
    sura = message.text
    await state.update_data(
        {"sura": sura}
    )
    await message.answer("Iltimos oyat raqamini kiriting !")
    await state.set_state('oyat')
@dp.message_handler(state='oyat')
async def oyatniolish(message: Message, state: FSMContext):
    try:
        oyat = message.text
        await state.update_data(
            {"oyat": oyat}
        )

        malumot = await state.get_data()
        sura = malumot.get('sura')
        oyat = malumot.get('oyat')
        tafsir = "uzb-alauddinmansour"
        url_sura1 = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"
        r = requests.get(url_sura1)
        malumot = r.json()
        await message.answer(text=f"{malumot['text']}")
        await state.finish()
    except:
        await message.answer("Son kiritishda xatolik yuz berdi! Iltimos qaytadan urinib ko'ring.")
        await state.finish()

# Inglizcha tafsir 'eng-abdulhye'

@dp.callback_query_handler(text="english:toliq")
async def verse_answer(call: CallbackQuery, state: FSMContext,):
    await call.message.answer("Enter the Sura number!")
    await call.answer(cache_time=1)
    await call.message.delete()
    await state.set_state("sura3")
@dp.message_handler(state="sura3")
async def get_sura(message: Message, state: FSMContext):
    try:
        msg = int(message.text)
        tafsir = 'eng-abdulhye'
        url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{msg}.json"
        r = requests.get(url_sura)
        data = r.json()
        for start, verse in enumerate(data['chapter']):
            await message.answer(text=f"{start + 1}-Verse\n{verse['text']}")
            await asyncio.sleep(2)
        await state.finish()
    except:
        await message.answer("There was an error entering the number! Please try again.")
        await state.finish()

@dp.callback_query_handler(text='english:oyat')
async def getSura(call:CallbackQuery,state: FSMContext):
    await call.message.delete()
    await call.message.answer("Enter the Sura number!")
    await call.answer(cache_time=2)
    await state.set_state('suraenglish')
@dp.message_handler(state='suraenglish')
async def suraniOlish1 (message: Message, state:FSMContext):
    sura = message.text
    await state.update_data(
        {"sura": sura}
    )
    await message.answer("Please enter the verse number!")
    await state.set_state('oyatenglish')
@dp.message_handler(state='oyatenglish')
async def oyatniolish1(message: Message, state: FSMContext):
    try:
        oyat = message.text
        await state.update_data(
            {"oyat": oyat}
        )

        malumot = await state.get_data()
        sura = malumot.get('sura')
        oyat = malumot.get('oyat')
        tafsir1 = 'eng-abdulhye'
        url_sura1 = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir1}/{sura}/{oyat}.json"
        r = requests.get(url_sura1)
        malumot = r.json()
        await message.answer(text=f"{malumot['text']}")
        await state.finish()
    except:
        await message.answer("There was an error entering the number! Please try again.")
        await state.finish()

# ruskiy tafsir https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/rus-ministryofawqaf.json
# rus-ministryofawqaf

@dp.callback_query_handler(text="ruskiy:toliq")
async def verse_answer(call: CallbackQuery, state: FSMContext,):
    await call.message.answer("Введите номер суры!")
    await call.answer(cache_time=1)
    await call.message.delete()
    await state.set_state("sura4")
@dp.message_handler(state="sura4")
async def get_sura(message: Message, state: FSMContext):
    try:
        msg = int(message.text)
        tafsir = 'rus-ministryofawqaf'
        url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{msg}.json"
        r = requests.get(url_sura)
        data = r.json()
        for start, verse in enumerate(data['chapter']):
            await message.answer(text=f"{start + 1}-стих\n{verse['text']}")
            await asyncio.sleep(2)
        await state.finish()
    except:
        await message.answer("Произошла ошибка при вводе номера! Пожалуйста, попробуйте еще раз.")
        await state.finish()

@dp.callback_query_handler(text='ruskiy:oyat')
async def getSura(call:CallbackQuery,state: FSMContext):
    await call.message.delete()
    await call.message.answer("Введите номер суры!")
    await call.answer(cache_time=1)
    await state.set_state('suraruskiy')
@dp.message_handler(state='suraruskiy')
async def suraniOlish2 (message: Message, state:FSMContext):
    sura = message.text
    await state.update_data(
        {"sura": sura}
    )
    await message.answer("Пожалуйста, введите номер стиха!")
    await state.set_state('oyatruskiy')
@dp.message_handler(state='oyatruskiy')
async def oyatniolish2(message: Message, state: FSMContext):
    try:
        oyat = message.text
        await state.update_data(
            {"oyat": oyat}
        )
        malumot = await state.get_data()
        sura = malumot.get('sura')
        oyat = malumot.get('oyat')
        tafsir2 = 'rus-ministryofawqaf'
        url_sura1 = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir2}/{sura}/{oyat}.json"
        res = requests.get(url_sura1)
        malumot1 = res.json()
        await message.answer(text=f"{malumot1['text']}")
        await state.finish()
    except:
        await message.answer("Произошла ошибка при вводе номера! Пожалуйста, попробуйте еще раз.")
        await state.finish()