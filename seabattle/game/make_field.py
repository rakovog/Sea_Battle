from seabattle.game.const import Konst


class Field:
    def __init__(self, size):
        k = Konst
        self.p = k.p
        self.size = size
        self.mas = [self.p] * self.size
        for i in range(self.size):
            self.mas[i] = [self.p] * self.size
        self.mas_b_1 = [self.p] * self.size
        for i in range(self.size):
            self.mas_b_1[i] = [self.p] * self.size
        list_1 = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k"]
        self.list = list_1[:self.size]
        self.mas_b = [self.p] * self.size
        for i in range(self.size):
            self.mas_b[i] = [self.p] * self.size
