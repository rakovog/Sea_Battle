from Sea_batle.make_field import Field
from Sea_batle.player import Player
import random


class Bot:
    def __init__(self, field, player):
        self.field = field
        self.mas_b = self.field.mas_b
        self.size = self.field.size
        self.list = self.field.list
        self.ship_b = random.choice(self.list)
        self.ship_b_l = random.randrange(0, self.size)
        self.ship_b_f = player.get_ship_f(self.ship_b[0])

    def xod_bot(self):
        col_ship = self.size * self.size // 3
        for b in range(col_ship):

            bot_set = True
            while bot_set == 1:
                for i in range(self.size):
                    for j in range(self.size):
                        if i == int(self.ship_b_f) and j == int(self.ship_b_l):
                            if self.mas_b[i][j] == "*":
                                bot_set = False
                                col_ship -= 1
            for i in range(self.size):
                for j in range(self.size):
                    if i == int(self.ship_b_f) and j == int(self.ship_b_l):
                        self.mas_b[i][j] = "X"
