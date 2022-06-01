from seabattle.game.konst import Konst


class Player:
    def __init__(self, field, printer):
        k = Konst
        self.s = k.s
        self.p = k.p
        self.pw = printer
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

    def check(self, size, mas, ship_x, ship_y):
        self.size = size
        self.mas = mas
        self.ship_y = ship_y
        self.ship_x = ship_x
        if 0 <= self.ship_x <= self.size - 1 and 0 <= self.ship_y <= self.size - 1:
            if (self.ship_x == 0 or self.mas[self.ship_x - 1][self.ship_y] != self.p) and (
                    self.ship_x == self.size - 1 or \
                    self.mas[self.ship_x + 1][
                        self.ship_y] != self.p) and (
                    self.ship_y == 0 or self.mas[self.ship_x][
                self.ship_y - 1] != self.p) and (self.ship_y == self.size - 1 or self.mas[self.ship_x][
                self.ship_y + 1] != self.p) and (self.ship_x == 0 or self.ship_y == 0 or self.mas[self.ship_x - 1][
                self.ship_y - 1] != self.p) and (self.ship_x == self.size - 1 or self.ship_y == self.size - 1 or \
                                                 self.mas[self.ship_x + 1][
                                                     self.ship_y + 1] != self.p) and (
                    self.ship_y == 0 or self.ship_x == self.size - 1 or \
                    self.mas[self.ship_x + 1][
                        self.ship_y - 1] != self.p) and (self.ship_y == self.size - 1 or self.ship_x == 0 or \
                                                         self.mas[self.ship_x - 1][
                                                             self.ship_y + 1] != self.p):
                return False
        else:
            return True

    def generate(self):
        ship = self.pw.input()
        return int(ship[1::]) - 1, self.get_ship_f(ship[0])

    def xod_player(self):
        col_ship = self.size * self.size // 3
        for b in range(col_ship):
            self.pw.print('Ведите расположение ', col_ship, ' однопалубных кораблей')
            ship_x, ship_y = self.generate()
            while self.check(self.size, self.mas, ship_x, ship_y):

                if self.mas[ship_y][ship_x] != self.p:
                    self.pw.print("Поле занято, повторите ввод:")
                    self.pw.print('Ведите расположение ', col_ship, ' однопалубных кораблей')
                    ship_x, ship_y = self.generate()
                else:
                    self.pw.print("Корабли слишком близко")
                    self.pw.print('Ведите расположение ', col_ship, ' однопалубных кораблей')
                    ship_x, ship_y = self.generate()
            self.mas[ship_y][ship_x] = self.s
            col_ship -= 1
            for i in range(self.size):
                self.pw.print(self.list[i], "| ",
                              ' '.join(list(map(str, self.mas[i]))), " | ",
                              ' '.join(list(map(str, self.mas_b_1[i]))))
