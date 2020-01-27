
class Physics():
    def __init__(self, gravity, air_resistance, friction_coefficient):
        self.gravity = gravity
        self.air_resistance = air_resistance
        self.friction = self.gravity * friction_coefficient