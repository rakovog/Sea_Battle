from make_field import Field


class Player:
    def __init__(self, field):
        self.field = field
        self.mas = self.field.mas
        self.size = self.field.size
        self.list = self.field.list
        self.mas_b_1 = self.field.mas_b_1

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
            print('Ведите расположение ', col_ship, ' однопалубных кораблей')
            ship = input()
            ship_x = int(ship[1::]) - 1
            ship_y = self.get_ship_f(ship[0])
            while True:

                if self.mas[ship_x][ship_y] != "*":
                    print('Ведите расположение ', col_ship, ' однопалубных кораблей')
                    ship = input()
                    ship_x = int(ship[1::]) - 1
                    ship_y = self.get_ship_f(ship[0])
                else:
                    break
            self.mas[ship_y][ship_x] = "X"
            col_ship -= 1
            print(sep="  ")
            for i in range(self.size):
                print(self.list[i], "| ", *self.mas[i], end=" | ")
                print(*self.mas_b_1[i], end="  ")
                print("", sep="  ")
