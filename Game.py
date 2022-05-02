from Sea_batle.make_field import Field
from Sea_batle.Player import player
from Sea_batle.Bot import bot
import random


class My_game:
    def __init__(self, q):
        self.q = q
        self.mas = player(self.q).mas
        self.mas_b = bot(self.q).mas_b
        self.a = Field(self.q).a
        self.list = Field(self.q).list
        self.mas_b_1 = player(self.q).mas_b_1
        self.ship_b = bot(self.q).ship_b_l
        self.ship_b_l = bot(self.q).ship_b_l
        self.ship_b_f = bot(self.q).ship_b_f

    def attack_player(self):
        player_shot = True
        while player_shot == True:
            ship = input("Ведите место атаки| ")
            ship_l = int(ship[1::]) - 1
            ship_f = player(self.q).get_ship_f(ship[0])
            for i in range(self.a):
                for j in range(self.a):
                    if i == int(ship_f) and j == int(ship_l):
                        if self.mas_b_1[i][j] == "*":
                            player_shot = False
                        else:
                            print("Вы уже стреляли в это место, хотите повторить? :-) ")

        # Проверка игрока
        for i in range(self.a):
            for j in range(self.a):
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
        while bot_shot == True:
            ship_b = random.choice(self.list)
            ship_b_l = random.randrange(0, self.a)
            ship_b_f = player(self.q).get_ship_f(ship_b[0])

            # проверка, свободно ли поле:
            for i in range(self.a):
                for j in range(self.a):
                    if i == int(ship_b_f) and j == int(ship_b_l):
                        if self.mas[i][j] == "*" or self.mas[i][j] == "X":
                            bot_shot = False
        for i in range(self.a):
            for j in range(self.a):
                if i == int(ship_b_f) and j == int(ship_b_l):
                    if self.mas[i][j] == "X":
                        self.mas[i][j] = "+"
                    else:
                        self.mas[i][j] = "-"

    def good_field(self):
        print(sep="  ")
        for i in range(self.a):
            print(self.list[i], "| ", *self.mas[i], end=" | ")
            print(*self.mas_b_1[i], end="  ")
            print("", sep="  ")

    def hwo_win(self):
        bot_win = True
        for i in range(self.a):
            for j in range(self.a):
                if self.mas_b[i][j] == "X":
                    bot_win = False

        i_win = True
        for i in range(self.a):
            for j in range(self.a):
                if self.mas[i][j] == "X":
                    i_win = False

        if bot_win == True and i_win == True:
            print("Ничья")

        elif bot_win == True:
            print("Ты победил!")

        elif i_win == True:
            print("Ты проиграл!")

    def game(self):
        p = player(self.q)
        self.mas = p.mas
        p.Xod_player()
        b = bot(self.q)
        b.Xod_bot()
        bot_win = False
        i_win = False
        while bot_win == False and i_win == False:
            g = My_game(self.q)
            g.attack_player()
            g.attack_bot()
            g.good_field()
            g.hwo_win()
