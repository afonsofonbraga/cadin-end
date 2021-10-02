class Debris:
    def __init__(self, name, pos, vel) -> None:
        self.name = name
        self.pos1 = pos[0]
        self.pos2 = pos[1]
        self.pos3 = pos[2]
        self.vel1 = vel[0]
        self.vel2 = vel[1]
        self.vel3 = vel[2]

    def __repr__(self):
        return "Name:  % s \nPosition: % s \nVelocity: % s \n" % (self.name, str(self.pos1) + str(self.pos2) + str(self.pos3), str(self.vel1) + str(self.vel2) + str(self.vel3))