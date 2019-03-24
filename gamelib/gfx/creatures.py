import pygame
from pygame.locals import *


def draw_bug(surface, x, y, short_leg, eye_pos):
    bug_color = (255, 255, 255)
    eye_color = (78, 219, 214)
    pygame.draw.rect(surface, bug_color, Rect(x, y, 18, 5), 0)
    for leg in range(6):
        print(short_leg, leg)
        if leg + 1 == short_leg:
            pygame.draw.line(surface, bug_color, (x + leg * 3, y + 5), (x + leg * 3, y + 6), 1)
        else:
            pygame.draw.line(surface, bug_color, (x + leg * 3, y + 5), (x + leg * 3, y + 8), 1)

    pygame.draw.rect(surface, eye_color, Rect(x + 15 * eye_pos, y - 2, 5, 5), 0)
    if eye_pos == 0:
        tail_pos = 1
    else:
        tail_pos = 0
    pygame.draw.rect(surface, (0, 0, 0), Rect(x + 15 * tail_pos, y - 2, 3, 3), 0)
