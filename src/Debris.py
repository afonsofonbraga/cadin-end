class Debris:
    def __init__(self, name, pos, vel) -> None:
        self.name = name
        self.position = pos
        self.velocity = vel

    def __repr__(self): 
        return "Name:  % s \nPosition: % s \nVelocity: % s \n" % (self.name, self.position, self.velocity)