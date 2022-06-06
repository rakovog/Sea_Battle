from seabattle.game.const import *


class Field:
    def __init__(self, size):
        self.size = size
        self.mas = [FIELD_EMPTY] * self.size
        for i in range(self.size):
            self.mas[i] = [FIELD_EMPTY] * self.size
        self.mas_b_1 = [FIELD_EMPTY] * self.size
        for i in range(self.size):
            self.mas_b_1[i] = [FIELD_EMPTY] * self.size
        list_1 = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k"]
        self.list = list_1[:self.size]
        self.mas_b = [FIELD_EMPTY] * self.size
        for i in range(self.size):
            self.mas_b[i] = [FIELD_EMPTY] * self.size
