class Debris:
    def init(self, name, s, t) -> None:
        self.name = name
        self.s = s
        self.t = t

    # def repr(self):
    #     # return "Debri" + self.name
    #     # print("Line 1" + self.s)
    #     # print("Line 2" + self.t)
    #     return f'Debri {self.name}'

    def repr(self): 
        return "Name:% s \n Line1:% s \n Line2:% s \n" % (self.name, self.s, self.t)
