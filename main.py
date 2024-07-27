import telebot
from telebot import types   # pip install telebot

bot = telebot.TeleBot('token')
url_req = input(f'Введите URL: ')

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Играть в кликер', web_app=types.WebAppInfo(url=url_req)))
    bot.send_message(message.chat.id, 'Тап, тап, тап!!!', reply_markup=markup)

bot.infinity_polling()