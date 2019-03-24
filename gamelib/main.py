import pygame

import sys

from gamelib.lib.util import init_pygame
from gamelib.lib.config import game_name, screen_size

# Globals.
game_state = 1
screen = init_pygame(game_name, screen_size)


def main():
    while game_state != -1:

        if game_state == 1:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
