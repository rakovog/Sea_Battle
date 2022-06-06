from seabattle.telegram.telebot import TeleBot

# telebot = TeleBot()
# telebot.start()

from seabattle.game.game import MyGame

size = int(input("Введите размер игровго поля от 5 до 10| "))
g = MyGame(size=size)
g.game()
