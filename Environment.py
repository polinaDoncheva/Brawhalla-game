import pygame
from helper_functions import get_image_from_text, load_images
from constants import HEIGHT, WIDTH, BLACK, WHITE, OPTION_MENU_WIDTH, OPTION_MENU_HEIGHT, MAX_PLAYER_RESISTANCE, menu_font
from Button import Button


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, file_name, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load(file_name)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Landscape(pygame.sprite.Sprite):
    def __init__(self, name, obstacles, background_file_name, menu_x, menu_y):
        super().__init__()
        self.name = name
        self.obstacles = obstacles

        # handles game background
        self.background_img = pygame.image.load(background_file_name)
        self.background_img = pygame.transform.scale(self.background_img, (WIDTH, HEIGHT))

        # handles landscape options menu interface
        self.name_img = get_image_from_text(name, menu_font, BLACK)
        self.button_menu = Button(menu_x, menu_y, self.name_img, OPTION_MENU_WIDTH, OPTION_MENU_HEIGHT)

    def draw_background(self, screen):
        screen.blit(self.background_img, (0, 0))

    def draw_obstacles(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def draw_in_menu(self, screen):
        return self.button_menu.draw(screen)


class Attack(pygame.sprite.Sprite):
    def __init__(self, name, hit_range_front, hit_range_up, hit_range_down, damage, push_back, menu_x, menu_y):
        super().__init__()
        self.name = name
        self.hit_range_up = hit_range_up
        self.hit_range_down = hit_range_down
        self.hit_range_front = hit_range_front
        self.damage = damage
        self.push_back = push_back  # % of attacker's resistance; list if different values depending on the direction

        self.name_img = get_image_from_text(name, menu_font, WHITE)
        self.button_menu = Button(menu_x, menu_y, self.name_img, OPTION_MENU_WIDTH, OPTION_MENU_HEIGHT)

    def draw_in_menu(self, screen):
        return self.button_menu.draw(screen)

    def get_damage(self):
        return self.damage

    def get_push_back_distance(self, target):
        if target.resistance <= 0:
            return self.push_back * MAX_PLAYER_RESISTANCE
        else:
            return self.push_back * (MAX_PLAYER_RESISTANCE / target.resistance)

    def get_hit_rect(self, attacker, direction):
        # 1 right
        # -1 left
        # 2 up
        # -2 down
        if direction == 2:
            return pygame.Rect(attacker.rect.centerx, attacker.rect.y - self.hit_range_up, attacker.rect.width // 2, attacker.rect.height//2 - self.hit_range_up)
        elif direction == 1:
            return pygame.Rect(attacker.rect.centerx, attacker.rect.y, attacker.rect.width // 2 + 20, attacker.rect.height)
        elif direction == -1:
            return pygame.Rect(attacker.rect.x - 20, attacker.rect.y, attacker.rect.width // 2 + 20, attacker.rect.height)
        else:
            return pygame.Rect(attacker.rect.centerx, attacker.rect.y + attacker.rect.height//2, attacker.rect.width // 2, attacker.rect.height//2 + self.hit_range_up)


class Avatar(pygame.sprite.Sprite):
    def __init__(self, name, attacks, file_path, menu_x, menu_y, steps, size, scale, offset):
        super().__init__()
        self.name = name
        self.attacks = attacks

        sheet = pygame.image.load(file_path).convert_alpha()
        self.animation_list = load_images(sheet, steps, size, scale, offset)

        # handles landscape options menu interface
        self.name_img = get_image_from_text(name, menu_font, BLACK)
        self.button_menu = Button(menu_x, menu_y, self.name_img, OPTION_MENU_WIDTH, OPTION_MENU_HEIGHT)

    def draw_in_menu(self, screen):
        return self.button_menu.draw(screen)
