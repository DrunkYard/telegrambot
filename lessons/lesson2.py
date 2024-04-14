import telebot
from telebot import types

bot = telebot.TeleBot('5812171840:AAFO_WC0XpufzYFWsErDI9cibdfKBCkyzx8')

# получить файл
# @bot.message_handler(content_types=['photo'])
# def main(message):
#     # добавление кнопок в сообщение
#     markup = types.InlineKeyboardMarkup()    
#     markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://www.google.com/'))
#     markup.add(types.InlineKeyboardButton('Удалить фото', callback_data='delete'))
#     markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit'))
#     bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)

# кнопки общие
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()    
    btn1 = types.KeyboardButton('Перейти на сайт 😁')
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn1)
    markup.row(btn2, btn3)
    
    # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    file = open('./iconbot.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_audio()
    # bot.send_video()
    

    # отработка событий
    bot.register_next_step_handler(message, on_click)

# отработка событий
def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is opened!')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Photo is deleted!')

@bot.message_handler(content_types=['photo'])
def main(message):
    markup = types.InlineKeyboardMarkup()    
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.google.com/')
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)

# отработка событий нажатия кнопки
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        # удалить предыдущее сообщение
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text',  callback.message.chat.id, callback.message.message_id)

bot.infinity_polling()