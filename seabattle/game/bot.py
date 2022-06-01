from seabattle.game.player import Player
from seabattle.game.konst import Konst
import random


class Bot:
    def __init__(self, field, printer):
        k = Konst
        self.s = k.s
        self.p = k.p
        self.printer = printer
        self.field = field
        self.mas_b = self.field.mas_b
        self.size = self.field.size
        self.list = self.field.list

    def generate(self):
        return random.randrange(0, self.size), random.randrange(0, self.size)

    def xod_bot(self):
        col_ship = self.size * self.size // 3
        for b in range(col_ship):
            ship_x, ship_y = self.generate()
            while Player(self.field, self.printer).check(self.size, self.mas_b, ship_x, ship_y):
                if self.mas_b[ship_x][ship_y] != self.p:
                    ship_x, ship_y = self.generate()
                else:
                    ship_x, ship_y = self.generate()
            self.mas_b[ship_x][ship_y] = self.s
