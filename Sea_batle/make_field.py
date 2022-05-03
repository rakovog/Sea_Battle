class Field:
    def __init__(self, size):
        self.size = size
        self.mas=["*"] * self.size
        for i in range(self.size):
            self.mas[i] = ["*"] * self.size
        self.mas_b_1 = ["*"] * self.size
        for i in range(self.size):
            self.mas_b_1[i] = ["*"] * self.size
        list_1 = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k"]
        self.list = list_1[:self.size]
        self.mas_b = ["*"] * self.size
        for i in range(self.size):
            self.mas_b[i] = ["*"] * self.size




