class Tle:
    def init(self, name, s, t) -> None:
        self.name = name
        self.s = s
        self.t = t

    def repr(self):
        return "Name:% s \n Line1:% s \n Line2:% s \n" % (self.name, self.s, self.t)
