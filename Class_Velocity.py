
class Velocity():
    def __init__(self, v_x, v_y, time, rules):
        self.rules = rules
        self.v_x = v_x
        self.v_y = -1*v_y
        self.time = time
    def instantaneous_velocity(self):
        inst_v_y = -1 * self.v_y +self.rules.gravity * self.time
        inst_v_x = self.v_x - self.rules.air_resistance
        return inst_v_x, inst_v_y