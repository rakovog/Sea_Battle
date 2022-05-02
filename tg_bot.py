import telebot
from telebot import types
import Sea_batle

bot = telebot.TeleBot("5120454206:AAFKcjd453_KjA7K2PrbgdjSIooqzk3vlFI")


@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Давай поиграем в Морской бой.')

@bot.message_handler(content_types=["text"])
def create(message):
    bot.send_message(message.chat.id, 'Введите размер игровго поля от 3 до 10| ')


@bot.message_handler(content_types=['size'])
def handle_size(message):
    p = Sea_batle.Player(message.size)
    p.player().Xod_player()

bot.polling(none_stop=True, interval=0)
