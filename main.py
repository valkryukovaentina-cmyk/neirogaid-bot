import telebot
import requests

TOKEN = "AAHMVuHZzBgruVhOJifjiXy4c_Pzf8dUABI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Нажми чтобы оплатить /buy")

@bot.message_handler(commands=['buy'])
def buy(message):
    bot.send_message(message.chat.id, "Оплати по ссылке и нажми /paid")

@bot.message_handler(commands=['paid'])
def paid(message):
    bot.send_message(message.chat.id, "Спасибо за оплату! Вот твой гайд 👇")
    doc = open('guide.pdf', 'rb')
    bot.send_document(message.chat.id, doc)

bot.polling()
