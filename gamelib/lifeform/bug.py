from gamelib.lib.cycle import loop_in_range, keep_in_range
from gamelib.gfx.creatures import draw_bug


class Bug(object):
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        self.leg_up = 1
        self.eye_pos = 1

    def update(self):
        self.leg_up = loop_in_range(self.leg_up, 1, 6, 1)
        self.x = keep_in_range(self.x, self.contraints[0], self.contraints[1])
        self.y = keep_in_range(self.y, self.contraints[2], self.contraints[3])

    def draw(self):
        draw_bug(self.screen, self.x, self.y, self.leg_up, self.eye_pos)

    def constrain(self, constaints):
        self.contraints = constaints
