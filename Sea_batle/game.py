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

    def attack_player(self):
        player_shot = True
        while player_shot:
            ship = input("Ведите место атаки| ")
            ship_y = int(ship[1::]) - 1
            ship_x = self.player.get_ship_f(ship[0])
            if self.mas_b_1[ship_x][ship_y] == "*":
                player_shot = False
            else:
                print("Вы уже стреляли в это место, хотите повторить? :-) ")

        # Проверка игрока
            if self.mas_b[ship_x][ship_y] == "X" or self.mas_b[ship_x][ship_y] == "+":
                self.mas_b_1[ship_x][ship_y] = "+"
                self.mas_b[ship_x][ship_y] = "+"
            else:
                self.mas_b_1[ship_x][ship_y] = "-"
                self.mas_b[ship_x][ship_y] = "-"

    def attack_bot(self):
        #   Бот атакует
        bot_shot = True
        while bot_shot == 1:
            ship = random.choice(self.list)
            ship_x = random.randrange(0, self.size)
            ship_y = self.player.get_ship_f(ship[0])

            # проверка, свободно ли поле:
            if self.mas[ship_y][ship_x] == "*" or self.mas[ship_y][ship_x] == "X":
                bot_shot = False
                if self.mas[ship_y][ship_x] == "X":
                    self.mas[ship_y][ship_x] = "+"
                else:
                    self.mas[ship_y][ship_x] = "-"

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

        if bot_win and i_win:
            print("Ничья")
            return False

        elif bot_win:
            print("Ты победил!")
            return False

        elif i_win:
            print("Ты проиграл!")
            return False

        else:
            return True

    def game(self):
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
