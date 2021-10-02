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
        return "Name:  % s \nPosition: % s \nVelocity: % s \n" % (self.name, str(pos1) + str(pos2) + str(pos3), str(vel1) + str(vel2) + str(vel3))