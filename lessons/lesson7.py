# pip install aiogram
# pip install --force-reinstall -v "aiogram==2.23.1"

# отличие в том что он асинхронный
from aiogram import Bot, Dispatcher, executor, types
import webbrowser

bot  = Bot('5812171840:AAFO_WC0XpufzYFWsErDI9cibdfKBCkyzx8')
dp = Dispatcher(bot)

# @dp.message_handler(commands=['start'])
@dp.message_handler(content_types=['photo'])
async def start(message: types.Message):
    # дожидаться выполнения
    # await bot.send_message(message.chat.id, 'Hello')    
    # await message.answer('Hello')
    # await message.answer_audio()
    # await message.answer_video()
    # await message.answer_photo()
    
    # ответ
    await message.reply('Hello')    

@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://www.google.com/'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)
    
@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    # показать кнопки один раз
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.reply('Reply', reply_markup=markup)
    
@dp.message_handler(content_types=['text'])
async def site(message: types.Message):
    if message.text == 'Site':
        await message.answer('Site is opened!')

# постоянное выполнение
executor.start_polling(dp)