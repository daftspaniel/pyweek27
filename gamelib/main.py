import pygame

import sys

from gamelib.lib.util import init_pygame
from gamelib.lib.config import game_name, screen_size

from gamelib.gfx.creatures import draw_bug

# Globals.
game_state = 1
screen = init_pygame(game_name, screen_size)


def main():
    while game_state != -1:

        if game_state == 1:

            draw_bug(screen, 10, 10)
            draw_bug(screen, 101, 101)
            draw_bug(screen, 10, 101)
            draw_bug(screen, 101, 10)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
