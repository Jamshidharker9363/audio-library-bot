from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
           KeyboardButton(text='🕋🎧Audio Quran'),
           KeyboardButton(text='🕌Tafsir')
        ],
        [
            KeyboardButton(text='⛑ help'),
            KeyboardButton(text='📞 ☎️Admin bilan aloqa')
        ],
    ],
    resize_keyboard=True
)

tafsirmenu = ReplyKeyboardMarkup(
    keyboard = [
        [
           KeyboardButton(text='Sheyx Al-Mansur'),
        ],
        [
            KeyboardButton(text='Sheyx Muhammad Sodiq')
        ],
        [
            KeyboardButton(text="🇬🇧 Ingliz tilida | In English "),
            KeyboardButton(text='🇷🇺 Rus tilida | на русском')
        ],
        [
            KeyboardButton(text="🔝Bosh sahifa")
        ],
    ],
    resize_keyboard=True
)
