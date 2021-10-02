class Debris:
    def __init__(self, name, s, t) -> None:
        self.name = name
        self.s = s
        self.t = t
        
    def __repr__(self): 
        return "Name:  % s \nLine1: % s \nLine2: % s \n" % (self.name, self.s, self.t)