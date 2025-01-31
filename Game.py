import pygame
from helper_functions import load_images, random_choice_landscape
from constants import *
from Button import Button
from Environment import get_image_from_text, Obstacle, Landscape, Attack, Avatar
from Players import Right_Player, Left_Player


class Game:
    def __init__(self):
        self.run = True
        self.player1_score = 0
        self.player2_score = 0
        self.rounds_counter = 0
        self.game_over1 = 0
        self.game_over2 = 0
        self.game_over_cooldown = 3
        self.MAIN_MENU = True
        self.LANDSCAPE_MENU = [False, False]
        self.ATTACK_MENU = [False, False]
        self.AVATAR_MENU = [False, False]
        self.landscape_type = [-1, -1, -1]

        self.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Brawhalla Game")
        self.load_buttons()
        self.load_attacks()
        self.load_fighter_images()
        self.load_landscapes()
        self.create_players()

        self.left_attacks_list = []
        self.right_attacks_list = []
        self.has_player1_chosen = [False, False, False]    # avatar, landscape, attack
        self.has_player2_chosen = [False, False, False]

    def load_buttons(self):
        # load images
        reset_img = get_image_from_text('RESTART', menu_font, BLACK)
        start_img = get_image_from_text('START', menu_font, WHITE)
        game_over_img = get_image_from_text('GAME OVER!!!', menu_font, BLACK)
        exit_img = get_image_from_text('EXIT', menu_font, WHITE)
        first_wins_img = get_image_from_text('PLAYER 1 WINS!', menu_font, BLACK)
        second_wins_img = get_image_from_text('PLAYER 2 WINS!', menu_font, BLACK)
        go_to_menu_img = get_image_from_text('GO TO MAIN MENU!', menu_font, BLACK)

        choose_avatar_img = get_image_from_text('CHOOSE AVATAR', menu_font, BLACK)
        player1_img = get_image_from_text('PLAYER 1', menu_font, BLACK)
        player2_img = get_image_from_text('PLAYER 2 ', menu_font, BLACK)
        choose_landscape_img = get_image_from_text('CHOOSE LANDSCAPE', menu_font, BLACK)
        choose_attack_img = get_image_from_text(' CHOOSE ATTACK', menu_font, BLACK)


        self.reset_button = Button(100, 300, reset_img, 200, 100)
        self.start_button = Button(0, 0, start_img, 250, 100)
        self.game_over_button = Button(230, 80, game_over_img, 300, 100)
        self.exit_button = Button(550, 0, exit_img, 250, 100)
        self.first_wins_button = Button(250, 150, first_wins_img, 250, 100)
        self.second_wins_button = Button(250, 150, second_wins_img, 250, 100)
        self.go_to_menu_button = Button(350, 300, go_to_menu_img, 350, 100)
        self.choose_landscape1_button = Button(0, 500, choose_landscape_img, 350, 50)
        self.choose_landscape2_button = Button(480, 500, choose_landscape_img, 320, 50)
        self.choose_attack1_button = Button(0, 555, choose_attack_img, 280, 50)
        self.choose_attack2_button = Button(515, 555, choose_attack_img, 280, 50)
        self.player1_button = Button(0, 350, player1_img, 300, 50)
        self.player2_button = Button(480, 350, player2_img, 300, 50)
        self.choose_avatar1_button = Button(0, 445, choose_avatar_img, 280, 50)
        self.choose_avatar2_button = Button(515, 445, choose_avatar_img, 280, 50)

    def load_fighter_images(self):
        hoodie_girl = Avatar('HOODIE_GIRL', self.attacks[0], 'assets/hoodie_girl.png', 0, 200, HOODIE_GIRL_ANIMATION_STEPS, HOODIE_GIRL_SIZE, HOODIE_GIRL_SCALE, HOODIE_GIRL_OFFSET)
        knight_girl = Avatar('KNIGHT_GIRL', self.attacks[1], 'assets/knight_girl.png', 250, 200, KNIGHT_GIRL_ANIMATION_STEPS, KNIGHT_GIRL_SIZE, KNIGHT_GIRL_SCALE, KNIGHT_GIRL_OFFSET)
        sword_girl = Avatar('SWORD_GIRL', self.attacks[2], 'assets/sword_girl.png', 500, 200, SWORD_GIRL_ANIMATION_STEPS, SWORD_GIRL_SIZE, SWORD_GIRL_SCALE, SWORD_GIRL_OFFSET)
        self.avatars = []
        self.avatars.append(hoodie_girl)
        self.avatars.append(knight_girl)
        self.avatars.append(sword_girl)

    def load_landscapes(self):
        # load obstacles
        fight_arena_image = Obstacle('assets/elenart-suelo1.jpg', 150, 300, 500, 150)
        flying_obstacle = Obstacle('assets/Wooden_platform_sprite_for_video_game.png', 0, 200, 300, 100)

        self.obstacles1 = []
        self.obstacles1.append(fight_arena_image)
        self.obstacles1.append(flying_obstacle)

        # load landscapes
        landscape1 = Landscape('BLUE SKY', self.obstacles1, 'assets/blue_sky.png', 0, 200)
        landscape2 = Landscape('PINK SKY', self.obstacles1, 'assets/pink_sky.jpg', 300, 200)
        landscape3 = Landscape('ANIME SKY', self.obstacles1, 'assets/evening background game.png', 600, 200)

        self.landscapes = []
        self.landscapes.append(landscape1)
        self.landscapes.append(landscape2)
        self.landscapes.append(landscape3)
        self.landscape_main = Landscape('menu', [], 'assets/starfield.png', 0, 0)

    def load_attacks(self):
        hoodie_fist_attack = Attack('sword', 100, 100, 100, 2, 500, 0, 200)
        hoodie_second_attack = Attack('water ball', 100, 100, 100, 4, 200, 300, 200)

        knight_fist_attack = Attack('butter knife', 100, 100, 100, 1, 400, 0, 200)
        knight_second_attack = Attack('stabbing knife', 100, 100, 100, 5, 300, 300, 200)

        sword_fist_attack = Attack('mini sword', 100, 100, 100, 6, 500, 0, 200)
        sword_second_attack = Attack('pocket knife', 100, 100, 100, 3, 350, 300, 200)

        self.attacks = [[hoodie_fist_attack, hoodie_second_attack],
                        [knight_fist_attack, knight_second_attack],
                        [sword_fist_attack, sword_second_attack]]

    def create_players(self):
        self.right = Right_Player(500, 330, 100)
        self.left = Left_Player(160, 330, 100)

        self.right.target = self.left
        self.left.target = self.right

    def picked_credentials(self):
        for i in range(3):
            if not self.has_player1_chosen[i] or not self.has_player2_chosen[i]:
                return False
        return True

    def execute_main_menu(self):
        self.player1_button.draw(self.SCREEN)
        self.player2_button.draw(self.SCREEN)

        if self.choose_avatar1_button.draw(self.SCREEN):
            self.AVATAR_MENU[0] = True
            self.left.has_avatar = True
            self.MAIN_MENU = False
        if self.choose_avatar2_button.draw(self.SCREEN):
            self.AVATAR_MENU[1] = True
            self.right.has_avatar = True
            self.MAIN_MENU = False
        if self.start_button.draw(self.SCREEN):
            if self.picked_credentials():
                self.MAIN_MENU = False
        if self.exit_button.draw(self.SCREEN):
            self.run = False
        if self.choose_landscape1_button.draw(self.SCREEN):
            if self.has_player1_chosen[0]:
                self.LANDSCAPE_MENU[0] = True
                self.MAIN_MENU = False
        if self.choose_landscape2_button.draw(self.SCREEN):
            if self.has_player2_chosen[0]:
                self.LANDSCAPE_MENU[1] = True
                self.MAIN_MENU = False
        if self.choose_attack1_button.draw(self.SCREEN):
            if self.has_player1_chosen[0] and self.has_player1_chosen[1]:
                self.ATTACK_MENU[0] = True
                self.MAIN_MENU = False
        if self.choose_attack2_button.draw(self.SCREEN):
            if self.has_player2_chosen[0] and self.has_player2_chosen[1]:
                self.ATTACK_MENU[1] = True
                self.MAIN_MENU = False

    def draw_main_landscape(self):
        self.landscape_main.draw_background(self.SCREEN)

    def draw_game_landscape(self):
        if self.landscape_type[0] == -1:
            self.landscape_type[0] = random_choice_landscape(self.landscape_type[1], self.landscape_type[2])
        self.landscapes[self.landscape_type[0]].draw_background(self.SCREEN)
        self.left.obstacles = self.landscapes[self.landscape_type[0]].obstacles
        self.right.obstacles = self.landscapes[self.landscape_type[0]].obstacles

    def execute_landscape_menu(self, index):
        counter = 0
        for landscape in self.landscapes:
            if landscape.draw_in_menu(self.SCREEN):
                if index == 0:
                    self.has_player1_chosen[1] = True
                else:
                    self.has_player2_chosen[1] = True

                self.landscape_type[index + 1] = counter
                self.landscape_type[0] = -1
                self.LANDSCAPE_MENU[index] = False
                self.MAIN_MENU = True
            counter += 1

    def execute_attack_menu(self, index):
        counter = 0
        current_attacks = []
        if index == 0:
            current_attacks = self.left_attacks_list
        else:
            current_attacks = self.right_attacks_list

        for attack in current_attacks:
            if attack.draw_in_menu(self.SCREEN):
                if index == 0:
                    self.has_player1_chosen[2] = True
                else:
                    self.has_player2_chosen[2] = True

                if index == 0:
                    self.left.attacks = current_attacks
                else:
                    self.right.attacks = current_attacks
                self.ATTACK_MENU[index] = False
                self.MAIN_MENU = True
            counter += 1

    def execute_avatar_menu(self, index):
        counter = 0
        for avatar in self.avatars:
            if avatar.draw_in_menu(self.SCREEN):
                if index == 0:
                    self.has_player1_chosen[0] = True
                else:
                    self.has_player2_chosen[0] = True

                if index == 0:
                    self.left.fill_animation_list(self.avatars[counter].animation_list)
                    self.left_attacks_list = self.avatars[counter].attacks
                    self.left.has_avatar = True
                else:
                    self.right.fill_animation_list(self.avatars[counter].animation_list)
                    self.right_attacks_list = self.avatars[counter].attacks
                    self.right.has_avatar = True
                self.AVATAR_MENU[index] = False
                self.MAIN_MENU = True
            counter += 1

    def reset_game(self):
        self.reset_round()
        self.player1_score = 0
        self.player2_score = 0
        self.rounds_counter = 0

    def reset_round(self):
        self.left.reset()
        self.right.reset()
        self.game_over1 = 0
        self.game_over2 = 0
        self.game_over_cooldown = 0

    def execute_round_over(self):
        counter = 100
        if self.game_over_cooldown <= counter:
            if self.game_over1 == 1 or self.game_over2 == 2:
                self.second_wins_button.draw(self.SCREEN)
            elif self.game_over2 == 1 or self.game_over1 == 2:
                self.first_wins_button.draw(self.SCREEN)
        else:
            if self.game_over1 == 1 or self.game_over2 == 2:
                self.player2_score += 1
            elif self.game_over2 == 1 or self.game_over1 == 2:
                self.player1_score += 1
            self.reset_round()
            self.rounds_counter += 1

    def play(self):
        if self.landscape_type[0] == -1:
            self.landscape_type[0] = 0
        current_landscape = self.landscapes[self.landscape_type[0]]
        current_landscape.draw_obstacles(self.SCREEN)

        if self.game_over1 == 1 or self.game_over2 == 2:
            self.game_over1 = self.left.update(self.game_over1)

        if self.game_over2 == 1 or self.game_over1 == 2:
            self.game_over2 = self.right.update(self.game_over2)

        self.right.draw(self.SCREEN)
        self.left.draw(self.SCREEN)

        if not self.game_over1 and not self.game_over2:
            self.game_over1 = self.left.update(self.game_over1)
            self.game_over2 = self.right.update(self.game_over2)
            self.left.draw(self.SCREEN)
            self.right.draw(self.SCREEN)

        if self.game_over1 or self.game_over2:
            if self.rounds_counter == 2:
                self.game_over_button.draw(self.SCREEN)
                if self.player2_score < self.player1_score:
                    self.first_wins_button.draw(self.SCREEN)
                else:
                    self.second_wins_button.draw(self.SCREEN)
                if self.reset_button.draw(self.SCREEN):
                    self.reset_game()
                if self.go_to_menu_button.draw(self.SCREEN):
                    self.MAIN_MENU = True
                    self.reset_game()
            else:
                self.execute_round_over()

        return self.MAIN_MENU

    def run_game(self):
        if self.MAIN_MENU or self.LANDSCAPE_MENU[0] or self.LANDSCAPE_MENU[1] or self.ATTACK_MENU[0] or \
                self.ATTACK_MENU[1] or self.AVATAR_MENU[0] or self.AVATAR_MENU[1]:
            self.draw_main_landscape()
        else:
            self.draw_game_landscape()

        if self.game_over1 or self.game_over2:
            self.game_over_cooldown += 1
        if self.AVATAR_MENU[0]:
            self.execute_avatar_menu(0)
        elif self.AVATAR_MENU[1]:
            self.execute_avatar_menu(1)
        elif self.MAIN_MENU:
            self.execute_main_menu()
        elif self.LANDSCAPE_MENU[0]:
            self.execute_landscape_menu(0)
        elif self.LANDSCAPE_MENU[1]:
            self.execute_landscape_menu(1)
        elif self.ATTACK_MENU[0]:
            self.execute_attack_menu(0)
        elif self.ATTACK_MENU[1]:
            self.execute_attack_menu(1)
        else:
            self.MAIN_MANU = self.play()

        return self.run

