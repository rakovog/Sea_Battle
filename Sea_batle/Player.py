from make_field import Field


class player:

    def get_ship_f(self, ship_f):
        self.ship_f = ship_f
        if self.ship_f == "a":
            return 0
        elif self.ship_f == "b":
            return 1
        elif self.ship_f == "c":
            return 2
        elif self.ship_f == "d":
            return 3
        elif self.ship_f == "e":
            return 4
        elif self.ship_f == "f":
            return 5
        elif self.ship_f == "g":
            return 6
        elif self.ship_f == "i":
            return 7
        elif self.ship_f == "j":
            return 8
        elif self.ship_f == "k":
            return 9

    def Xod_player(self):
        s = self.a * self.a // 3
        for b in range(s):
            player_set = True
            while player_set == True:


                message_to_return = f'Ведите расположение {s} однопалубных кораблей"/n'
                print(message_to_return)
                self.ship = input()
                self.ship_l = int(self.ship[1::]) - 1
                self.ship_f = self.get_ship_f(self.ship[0])
                for i in range(self.a):
                    for j in range(self.a):
                        if i == int(self.ship_f) and j == int(self.ship_l):
                            if self.mas[i][j] == "*":
                                player_set = False
                                s -= 1
                            else:
                                print("Поле занято, повторите ввод")
            for i in range(self.a):
                for j in range(self.a):
                    if i == int(self.ship_f) and j == int(self.ship_l):
                        self.mas[i][j] = "X"
            print(sep="  ")
            for i in range(self.a):
                print(self.list[i], "| ", *self.mas[i], end=" | ")
                print(*self.mas_b_1[i], end="  ")
                print("", sep="  ")

    def __init__(self, field):
        self.field = field
        self.mas = self.field.mas
        self.q = self.field.a
        self.a = self.field.a
        self.list = self.field.list
        self.mas_b_1 = self.field.mas_b_1
