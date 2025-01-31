import pygame

VEL = 3
WIDTH, HEIGHT = 800, 600
OPTION_MENU_WIDTH, OPTION_MENU_HEIGHT = 200, 100
FPS = 60
MAX_PLAYER_RESISTANCE = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

HOODIE_GIRL_ANIMATION_STEPS = [5, 8, 8, 6, 3, 3, 10, 5, 2]
HOODIE_GIRL_SIZE = 128
HOODIE_GIRL_SCALE = 10
HOODIE_GIRL_OFFSET = [0, 0]

KNIGHT_GIRL_ANIMATION_STEPS = [5, 8, 8, 5, 4, 6, 5, 4, 2]
KNIGHT_GIRL_SIZE = 128
KNIGHT_GIRL_SCALE = 10
KNIGHT_GIRL_OFFSET = [0, 0]

SWORD_GIRL_ANIMATION_STEPS = [6, 7, 6, 5, 2, 5, 5, 4, 3]
SWORD_GIRL_SIZE = 128
SWORD_GIRL_SCALE = 10
SWORD_GIRL_OFFSET = [0, 0]

pygame.init()
menu_font = pygame.font.SysFont('Bauhaus 93', 70)
