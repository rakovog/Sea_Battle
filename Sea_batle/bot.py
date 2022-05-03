from Sea_batle.make_field import Field
from Sea_batle.player import Player
import random


class Bot:
    def __init__(self, field, player):
        self.field = field
        self.mas_b = self.field.mas_b
        self.size = self.field.size
        self.list = self.field.list

    def xod_bot(self):
        col_ship = self.size * self.size // 3
        for b in range(col_ship):
            ship_x = random.randrange(0, self.size)
            ship_y = random.randrange(0, self.size)
            while True:
                if self.mas_b[ship_x][ship_y] != "*":
                    ship_x = random.randrange(0, self.size)
                    ship_y = random.randrange(0, self.size)
                else:
                    break
            self.mas_b[ship_x][ship_y] = "X"
