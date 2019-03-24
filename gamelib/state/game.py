import sys
from gamelib.lifeform.bug import Bug

from pygame.locals import *
from gamelib.lib.util import *

HORIZON = 100


def gameplay_main(screen):
    game_state = 1
    p1 = Bug(screen, 25, HORIZON + 15)
    p1.constrain((20, 780, HORIZON+15, 480))
    while game_state == 1:

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == ANIMEVENT:
                screen.fill(pygame.Color("black"))
                draw_background(screen)
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


def draw_background(screen):
    pygame.draw.polygon(screen, Color(2, 56, 2), [(0, HORIZON), (115, HORIZON - 15), (230, HORIZON)])
    pygame.draw.polygon(screen, Color(2, 50, 2), [(134, HORIZON), (215, HORIZON - 15), (630, HORIZON)])
    pygame.draw.polygon(screen, Color(2, 56, 2), [(534, HORIZON), (565, HORIZON - 15), (640, HORIZON)])
    pygame.draw.polygon(screen, Color(2, 56, 2), [(634, HORIZON), (666, HORIZON - 15), (796, HORIZON)])
    pygame.draw.line(screen, Color(2, 50, 44), (0, 500), (800, 500), 2)
