from Sea_batle.make_field import Field
from Sea_batle.player import Player
from Sea_batle.bot import Bot
import random


class MyGame:
    def __init__(self, size):
        self.size = size
        self.field_player = Field(self.size)
        self.field_bot = Field(self.size)

        self.player = Player(self.field_player)
        self.bot = Bot(self.field_bot, self.player)

        self.mas = self.player.mas
        self.mas_b = self.bot.mas_b

        self.list = self.field_player.list
        self.mas_b_1 = self.player.mas_b_1
        self.ship_b = self.bot.ship_b_l
        self.ship_b_l = self.bot.ship_b_l
        self.ship_b_f = self.bot.ship_b_f

    def attack_player(self):
        player_shot = True
        while player_shot == 1:
            ship = input("Ведите место атаки| ")
            ship_l = int(ship[1::]) - 1
            ship_f = self.player.get_ship_f(ship[0])
            for i in range(self.size):
                for j in range(self.size):
                    if i == int(ship_f) and j == int(ship_l):
                        if self.mas_b_1[i][j] == "*":
                            player_shot = False
                        else:
                            print("Вы уже стреляли в это место, хотите повторить? :-) ")

        # Проверка игрока
        for i in range(self.size):
            for j in range(self.size):
                if i == int(ship_f) and j == int(ship_l):
                    if self.mas_b[i][j] == "X" or self.mas_b[i][j] == "+":
                        self.mas_b_1[i][j] = "+"
                        self.mas_b[i][j] = "+"
                    else:

                        self.mas_b_1[i][j] = "-"
                        self.mas_b[i][j] = "-"

    def attack_bot(self):
        #   Бот атакует
        bot_shot = True
        while bot_shot == 1:
            ship_b = random.choice(self.list)
            ship_b_l = random.randrange(0, self.size)
            ship_b_f = self.player.get_ship_f(ship_b[0])

            # проверка, свободно ли поле:
            for i in range(self.size):
                for j in range(self.size):
                    if i == int(ship_b_f) and j == int(ship_b_l):
                        if self.mas[i][j] == "*" or self.mas[i][j] == "X":
                            bot_shot = False
        for i in range(self.size):
            for j in range(self.size):
                if i == int(ship_b_f) and j == int(ship_b_l):
                    if self.mas[i][j] == "X":
                        self.mas[i][j] = "+"
                    else:
                        self.mas[i][j] = "-"

    def good_field(self):
        print(sep="  ")
        for i in range(self.size):
            print(self.list[i], "| ", *self.mas[i], end=" | ")
            print(*self.mas_b_1[i], end="  ")
            print("", sep="  ")

    def hwo_win(self):
        bot_win = True
        for i in range(self.size):
            for j in range(self.size):
                if self.mas_b[i][j] == "X":
                    bot_win = False

        i_win = True
        for i in range(self.size):
            for j in range(self.size):
                if self.mas[i][j] == "X":
                    i_win = False

        if bot_win == 1 and i_win == 1:
            print("Ничья")

        elif bot_win == 1:
            print("Ты победил!")

        elif i_win == 1:
            print("Ты проиграл!")

    def game(self):
        p = self.player
        self.mas = p.mas
        p.xod_player()
        b = self.bot
        self.mas_b = b.mas_b
        b.xod_bot()
        bot_win = False
        i_win = False
        while bot_win == 2 and i_win == 2:
            self.attack_player()
            self.attack_bot()
            self.good_field()
            self.hwo_win()
