from make_field import Field


class Player:
    def __init__(self, field):
        self.field = field
        self.mas = self.field.mas
        self.size = self.field.size
        self.list = self.field.list
        self.mas_b_1 = self.field.mas_b_1
        self.ship = None
        self.ship_l = None
        self.ship_f = None

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

    def xod_player(self):
        col_ship = self.size * self.size // 3
        for b in range(col_ship):
            player_set = True
            while player_set:

                print('Ведите расположение ', col_ship, ' однопалубных кораблей')
                self.ship = input()
                self.ship_l = int(self.ship[1::]) - 1
                self.ship_f = self.get_ship_f(self.ship[0])
                for i in range(self.size):
                    for j in range(self.size):
                        if i == int(self.ship_f) and j == int(self.ship_l):
                            if self.mas[i][j] == "*":
                                player_set = False
                                col_ship -= 1
                            else:
                                print("Поле занято, повторите ввод")
            for i in range(self.size):
                for j in range(self.size):
                    if i == int(self.ship_f) and j == int(self.ship_l):
                        self.mas[i][j] = "X"
            print(sep="  ")
            for i in range(self.size):
                print(self.list[i], "| ", *self.mas[i], end=" | ")
                print(*self.mas_b_1[i], end="  ")
                print("", sep="  ")
