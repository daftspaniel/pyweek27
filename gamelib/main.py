import pygame

import sys

from gamelib.lib.util import init_pygame
from gamelib.lib.config import game_name, screen_size
from gamelib.lifeform.bug import Bug

from pygame.locals import *
from gamelib.lib.util import *

# Globals.
game_state = 1
screen = init_pygame(game_name, screen_size)

p1 = Bug(screen)


def main():
    while game_state != -1:

        if game_state == 1:

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == ANIMEVENT:
                    screen.fill(pygame.Color("black"))
                    p1.draw()
                elif event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_d] == 1:
                        p1.x += 1
                        p1.eye_pos = 1
                        p1.update()
                    elif keystate[K_a] == 1:
                        p1.x -= 1
                        p1.eye_pos = 0
                        p1.update()
                    if keystate[K_w] == 1:
                        p1.y -= 1
                        p1.update()
                    elif keystate[K_s] == 1:
                        p1.y += 1
                        p1.update()
