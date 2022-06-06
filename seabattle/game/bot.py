from seabattle.game.const import *
from seabattle.game.check import check
import random


class Bot:
    def __init__(self, field, printer):
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
            # TODO
            while check(self.size, self.mas_b, ship_x, ship_y):
                if self.mas_b[ship_x][ship_y] != FIELD_EMPTY:
                    ship_x, ship_y = self.generate()
                else:
                    ship_x, ship_y = self.generate()
            self.mas_b[ship_x][ship_y] = FIELD_SHIP
