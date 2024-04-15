from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot  = Bot('5812171840:AAFO_WC0XpufzYFWsErDI9cibdfKBCkyzx8')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # для отправки данных на форму используется InlineKeyboardMarkup
    # для получения данных из формы используется ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть web страницу', web_app=WebAppInfo(url='https://drunkyard.github.io/site/')))
    await message.answer("Привет мой друг", reply_markup=markup)

# данные полученные из формы
@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    # получаем данные
    res = json.loads(message.web_app_data.data)    
    await message.answer(f"Name: {res['name']} Email: {res['email']} Phone: {res['phone']}")

executor.start_polling(dp)