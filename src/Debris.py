class Debris:
    def __init__(self, name, pos, vel) -> None:
        self.name = name
        self.longitude = pos[0]
        self.latitude = pos[1]
        self.altitude = pos[2]
        self.vel1 = vel[0]
        self.vel2 = vel[1]
        self.vel3 = vel[2]

    def __repr__(self):
        return "Name:  % s \nPosition: % s \nVelocity: % s \n" % (self.name, str(self.longitude) + str(self.latitude) + str(self.altitude), str(self.vel1) + str(self.vel2) + str(self.vel3))