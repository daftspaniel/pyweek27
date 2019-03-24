from gamelib.lib.config import game_name, screen_size
from gamelib.state.game import gameplay_main
from gamelib.lib.util import init_pygame

# Globals.
game_state = 1
screen = init_pygame(game_name, screen_size)


def main():
    while game_state != -1:

        if game_state == 1:
            gameplay_main(screen)
