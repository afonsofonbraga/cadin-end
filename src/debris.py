class Debris:
    def __init__(self, name, s, t) -> None:
        self.name = name
        self.s = s
        self.t = t
        
    # def __repr__(self):
    #     # return "Debri" + self.name
    #     # print("Line 1" + self.s)
    #     # print("Line 2" + self.t)
    #     return f'Debri {self.name}'

    def __repr__(self): 
        return "Name:% s \n Line1:% s \n Line2:% s \r\n" % (self.name, self.s, self.t) 