from Sea_batle.make_field import Field
from Sea_batle.Player import player
import random
class bot:
    def __init__(self,q):
        self.q=q
        self.mas_b=Field(self.q).mas_b
        self.a=Field(self.q).a
        self.list=Field(self.q).list
        self.ship_b = random.choice(self.list)
        self.ship_b_l = random.randrange(0, self.a)
        self.ship_b_f = player(self.q).get_ship_f(self.ship_b[0])
    def Xod_bot(self):

        bot_set = True
        while bot_set == True:
            for i in range(self.a):
                for j in range(self.a):
                    if i == int(self.ship_b_f) and j == int(self.ship_b_l):
                        if self.mas_b[i][j] == "*":
                            bot_set = False
        for i in range(self.a):
            for j in range(self.a):
                if i == int(self.ship_b_f) and j == int(self.ship_b_l):
                    self.mas_b[i][j] = "X"

