import pygame
from constants import *
from Environment import Attack
from helper_functions import get_image_from_text

class Player:
    def __init__(self, x, y, right_side, controls, weapon_controls, resistance):
        super().__init__()

        self.animation_list = []
        self.action = 0  # 0-idle   1-run  2-jump   3-light_attack   4-heavy_attack  5-hit   6-death
        self.obstacles = []

        self.right_side = right_side
        self.start_resistance = resistance

        self.attacks = []
        self.weapon_controls = weapon_controls
        self.attack_speed = 0   # 0 - slow    1 - fast
        self.target = None
        self.image = None

        self.start_x = x
        self.start_y = y
        self.controls = controls

        self.dead_image = pygame.image.load('assets/chostt.jpg')
        self.dead_image = pygame.transform.scale(self.dead_image, (100, 100))
        self.dead_image.set_colorkey(WHITE)

        self.Y_GRAVITY = 1
        self.JUMP_HEIGHT = 15

        self.reset()

    def reset(self):
        self.has_avatar = False
        self.index = 0
        self.counter = 0
        self.action = 0

        self.attack_speed = 0  # 0 - slow    1 - fast
        self.attacking = False
        self.attack_cooldown = 0
        self.resistance = self.start_resistance

        if self.animation_list and self.obstacles and self.attacks:
            self.fill_animation_list(self.animation_list)
        if self.image:
            self.rect = self.image.get_rect()
            self.rect.x = self.start_x
            self.rect.y = self.start_y

        self.jump_count = 0
        self.Y_VELOCITY = 0
        self.jumping = False
        self.hit = False

    def fill_animation_list(self, animation_list):
        self.animation_list = animation_list
        if self.right_side:
            self.image = pygame.transform.flip(self.animation_list[self.index][0], True, False)
            self.direction = -1
        else:
            self.image = self.animation_list[self.index][0]
            self.direction = 1


        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.x = self.start_x
        self.rect.y = self.start_y

    def set_image(self):
        if self.direction == 1:
            self.image = self.animation_list[self.action][self.index]
        if self.direction == -1:
            self.image = pygame.transform.flip(self.animation_list[self.action][self.index], True, False)

    def handle_animation(self):
        walk_cooldown = 5
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.animation_list[self.action]):
                self.index = 0
                if self.action == 5 or self.action == 6:
                    self.attacking = False
                    self.attack_cooldown = 20
                if self.action == 8:
                    self.hit = False
                    self.attacking = False
                    self.attack_cooldown = 20

        self.set_image()

    def draw_resistance_bar(self, screen):
        ratio = self.resistance / 100
        x = 20
        y = 20
        #right side player
        if self.right_side:
            x = 580
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 204, 34))
        pygame.draw.rect(screen, RED, (x, y, 200, 30))
        pygame.draw.rect(screen, GREEN, (x, y, 200 * ratio, 30))

        resistance_img = get_image_from_text('resistance', menu_font, WHITE)
        resistance_img = pygame.transform.scale(resistance_img, (180, 40))
        rect = resistance_img.get_rect()
        rect.x = x + 12
        rect.y = y - 6
        screen.blit(resistance_img, rect)

    def draw_score(self, screen, score):
        if self.right_side:
            img = pygame.image

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_resistance_bar(screen)

    def player_input(self):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        self.counter += 1
        if self.hit:
            self.update_action(8)
        elif self.attacking:
            self.update_action(5 + self.attack_speed)
        elif not self.attacking:
            # check for attack
            if keys[self.weapon_controls[0]]:
               self.attack_speed = 0
               self.attacking = True
               self.attack(0)
            if keys[self.weapon_controls[1]]:
                self.attack_speed = 1
                self.attacking = True
                self.attack(1)

            # check for movement
            if keys[self.controls[1]] and self.rect.y <= HEIGHT - 70:  # DOWN
                dy += VEL
                self.update_action(0)
            if keys[self.controls[2]] and self.rect.x > 0:  # LEFT
                dx -= VEL
                self.direction = -1
                self.update_action(1)
            if keys[self.controls[3]] and self.rect.x <= WIDTH - 70:  # RIGHT
                dx += VEL
                self.direction = 1
                self.update_action(1)
            if keys[self.controls[4]] and self.jumping == False and self.jump_count < 2:  # JUMP
                self.Y_VELOCITY = -self.JUMP_HEIGHT
                self.jumping = True
                self.jump_count += 1
                self.update_action(2)
            if not keys[self.controls[4]]:
                self.jumping = False
            if not keys[self.controls[2]] and not keys[self.controls[3]] and not keys[self.controls[4]]:
                self.update_action(0)

        # gravity
        self.Y_VELOCITY += self.Y_GRAVITY
        if self.Y_VELOCITY > self.JUMP_HEIGHT:
            self.Y_VELOCITY = self.JUMP_HEIGHT
        dy += self.Y_VELOCITY

        for obstacle in self.obstacles:
            # collision in x
            if obstacle.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # collision in y
            if obstacle.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # jumping
                if self.Y_VELOCITY < 0:
                    dy = obstacle.rect.bottom - self.rect.top
                    self.Y_VELOCITY = 0
                # falling
                elif self.Y_VELOCITY >= 0:
                    dy = obstacle.rect.top - self.rect.bottom
                    self.Y_VELOCITY = 0
                    self.jump_count = 0

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.y < 0:
            self.rect.y = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.index = 0
        self.set_image()

    def attack(self, index):
        if self.attack_cooldown == 0:
            attacking_rect = self.attacks[index].get_hit_rect(self, self.direction)
            if attacking_rect.colliderect(self.target.rect):
                self.target.hit = True
                self.target.take_damage(self.attacks[index].get_damage(), self.attacks[index].get_push_back_distance(self.target), self.direction)

    def take_damage(self, damage, push_back, direction):
        self.resistance -= damage
        dx = push_back * direction
        if int(self.resistance/10) <= 0:
            self.resistance = 0
            self.rect.x += dx
        else:
            self.rect.x += (dx//int(self.resistance/10))

    def update(self, game_over):
        if not game_over:
            self.player_input()
            self.handle_animation()
        else:
            self.image = self.dead_image
            if self.rect.y > 50:
                self.rect.y -= 5

        if self.rect.y >= HEIGHT:
            game_over = 1
        if self.target.rect.x >= WIDTH or self.target.rect.x < 0:
            game_over = 2

        return game_over


class Right_Player(Player):
    def __init__(self, x, y,  resistance):
        controls = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_KP_ENTER)
        weapon_controls = (pygame.K_KP1, pygame.K_KP2)
        super().__init__(x, y, True, controls, weapon_controls, resistance)


class Left_Player(Player):
    def __init__(self, x, y, resistance):
        controls = (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE)
        weapon_controls = (pygame.K_1, pygame.K_2)
        super().__init__(x, y, False, controls, weapon_controls, resistance)