from gamelib.lib.cycle import loop_in_range
from gamelib.gfx.creatures import draw_bug

class Bug(object):
    def __init__(self, screen):
        self.screen = screen
        self.x = 10
        self.y = 10

        self.leg_up = 1
        self.eye_pos = 1

    def update(self):
        self.leg_up = loop_in_range(self.leg_up, 1,6, 1)

    def draw(self):
        draw_bug(self.screen, self.x, self.y, self.leg_up, self.eye_pos)
