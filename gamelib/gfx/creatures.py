import pygame
from pygame.locals import *


def draw_bug(surface, x, y):
    bug_color = (255, 255, 255)
    eye_color = (111, 111, 255)
    pygame.draw.rect(surface, bug_color, Rect(x, y, 20, 5), 0)
    for leg in range(6):
        pygame.draw.line(surface, bug_color, (x + leg * 3, y + 5), (x + leg * 3, y + 8), 1)

    pygame.draw.rect(surface, eye_color, Rect(x + 15, y - 2, 4, 4), 0)
