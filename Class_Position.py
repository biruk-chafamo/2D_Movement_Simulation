class Position():
    def __init__(self, x, y, time, velocity, rules):
        self.rules = rules
        self.y = y
        self.x = x
        self.time = time
        self.initial_velocity = velocity
    def instantaneous_position(self):
        instantaneous_y_position = self.y + self.initial_velocity.v_y * self.time + 0.5 * (self.rules.gravity * (self.time) ** 2)
        instantaneous_x_position = self.x + self.initial_velocity.v_x * self.time
        return instantaneous_x_position, instantaneous_y_position