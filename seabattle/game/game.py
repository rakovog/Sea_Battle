from seabattle.game.const import *
from seabattle.game.make_field import Field
from seabattle.game.player import Player
from seabattle.game.bot import Bot
import random

from seabattle.printwrite.ConsolePrinterWriter import ConsolePrinterWriter

# TODO replace consts
class MyGame:
    def __init__(self, size=3, pw=ConsolePrinterWriter()):
        self.pw = pw
        self.size = size
        self.field_player = Field(self.size)
        self.field_bot = Field(self.size)
        self.player = Player(self.field_player, self.pw)
        self.bot = Bot(self.field_bot, self.pw)

        self.mas = self.player.mas
        self.mas_b = self.bot.mas_b

        self.list = self.field_player.list
        self.mas_b_1 = self.player.mas_b_1

    def attack_player(self):
        player_shot = True
        while player_shot:
            ship = self.pw.input("Ведите место атаки| ")
            ship_y = int(ship[1::]) - 1
            ship_x = self.player.get_ship_f(ship[0])
            if self.mas_b_1[ship_x][ship_y] == FIELD_EMPTY:
                player_shot = False
            else:
                self.pw.print("Вы уже стреляли в это место, хотите повторить? :-) ")

            # Проверка игрока
            if self.mas_b[ship_x][ship_y] == self.s or self.mas_b[ship_x][ship_y] == self.a:
                self.mas_b_1[ship_x][ship_y] = self.a
                self.mas_b[ship_x][ship_y] = self.a
            else:
                self.mas_b_1[ship_x][ship_y] = self.m
                self.mas_b[ship_x][ship_y] = self.m

    def attack_bot(self):
        #   Бот атакует
        bot_shot = True
        while bot_shot == 1:
            ship = random.choice(self.list)
            ship_x = random.randrange(0, self.size)
            ship_y = self.player.get_ship_f(ship[0])

            # проверка, свободно ли поле:
            if self.mas[ship_y][ship_x] == FIELD_EMPTY or self.mas[ship_y][ship_x] == self.s:
                bot_shot = False
                if self.mas[ship_y][ship_x] == self.s:
                    self.mas[ship_y][ship_x] = self.a
                else:
                    self.mas[ship_y][ship_x] = self.m

    def good_field(self):
        for i in range(self.size):
            self.pw.print(self.list[i], "| ",
                          ' '.join(list(map(str, self.mas[i]))), " | ",
                          ' '.join(list(map(str, self.mas_b_1[i]))))

    def hwo_win(self):
        bot_win = True
        for i in range(self.size):
            for j in range(self.size):
                if self.mas_b[i][j] == self.s:
                    bot_win = False

        i_win = True
        for i in range(self.size):
            for j in range(self.size):
                if self.mas[i][j] == self.s:
                    i_win = False

        if bot_win and i_win:
            self.pw.print("Ничья")
            return False

        elif bot_win:
            self.pw.print("Ты победил!")
            return False

        elif i_win:
            self.pw.print("Ты проиграл!")
            return False

        else:
            return True

    def game(self):
        self.pw.print("%s это корабль" % FIELD_SHIP)
        self.pw.print("%s это промах" % FIELD_SHIP_MISS)
        self.pw.print("%s это попадение" % FIELD_SHIP_HIT)
        p = self.player
        self.mas = p.mas
        p.xod_player()
        b = self.bot
        self.mas_b = b.mas_b
        b.xod_bot()
        while self.hwo_win():
            self.attack_player()
            self.attack_bot()
            self.good_field()
