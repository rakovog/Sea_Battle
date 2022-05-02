class Field:
    def __init__(self, a):
        self.a = a
        self.s = self.a * self.a // 3
        self.mas=["*"] * self.a
        for i in range(self.a):
            self.mas[i] = ["*"] * self.a
        self.mas_b_1 = ["*"] * self.a
        for i in range(self.a):
            self.mas_b_1[i] = ["*"] * self.a
        list_1 = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k"]
        self.list = list_1[:self.a]
        self.mas_b = ["*"] * self.a
        for i in range(self.a):
            self.mas_b[i] = ["*"] * self.a




