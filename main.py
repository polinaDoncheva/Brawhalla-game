import pygame
from Game import Game
from constants import FPS
import time
pygame.init()
from Game import *
from Players import *

def main():
    game = Game()
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        run = game.run_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
