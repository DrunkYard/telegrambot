import telebot
import webbrowser

bot = telebot.TeleBot('5812171840:AAFO_WC0XpufzYFWsErDI9cibdfKBCkyzx8')

@bot.message_handler(commands=['site','website'])
def main(message):
    # открыть сайт через браузер по-умолчанию
    webbrowser.open('https://www.google.com/')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'hello {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['test'])
def main(message):
    bot.send_message(message.chat.id, 
                     '<b>Help</b> <em><u>Information</u></em>', 
                     parse_mode='html')

# необходимо описывать только после coomands, инчае будет игнор
@bot.message_handler()
def info(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, f'hello {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text == 'id':
        # bot.send_message(message.chat.id, f'your id = {message.id}')
        # ответ на сообщение
        bot.reply_to(message, f'your id = {message.id}')

# выполняться постоянно
# bot.infinity_polling()
bot.polling(none_stop=True)