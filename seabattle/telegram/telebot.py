import telebot
import os

from seabattle import MyGame
from seabattle.printwrite.TelegramPrinterWriter import TelegramPrinterWriter

TELEBOT_TOKEN_ENV = "TELEBOT_TOKEN"

class TeleBot:
    def __init__(self):
        bot = telebot.TeleBot(os.environ[TELEBOT_TOKEN_ENV])
        self.chats = {}
        self.games = {}

        @bot.message_handler(commands=['startGame'])
        def start_game(m, res=False):
            self.chats[m.chat.id] = {"waiting": False, "last_message": None}
            pw = TelegramPrinterWriter(self, m.chat.id)
            pw.print('Привет! Давай поиграем в Морской бой.')
            size = int(pw.input("Введите размер игровго поля от 3 до 10| "))
            g = MyGame(size=size, pw=pw)
            g.game()

        @bot.message_handler(content_types=["text"])
        def create(message):
            if message.chat.id in self.chats and self.chats[message.chat.id]["waiting"]:
                self.chats[message.chat.id]["last_message"] = message.text
                self.chats[message.chat.id]["waiting"] = False

        self.bot = bot

    def start(self):
        self.bot.polling(none_stop=True, interval=0)

    def print(self, chat_id, *messages):
        text = ' '.join(list(map(str, messages)))
        self.bot.send_message(chat_id=chat_id, text=text)

    def input(self, chat_id, *messages):
        if messages is not None and messages != ():
            self.print(chat_id, *messages)
        self.chats[chat_id]["waiting"] = True
        while self.chats[chat_id]["waiting"]:
            pass
        return self.chats[chat_id]["last_message"]
