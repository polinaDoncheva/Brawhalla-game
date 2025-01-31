import unittest
import pygame
from Players import Player, Right_Player, Left_Player
from Environment import Attack, Avatar
from constants import *

class TestPlayer(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.controls = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_KP_ENTER)
        self.weapon_controls = (pygame.K_KP1, pygame.K_KP2)
        self.resistance = 100

    def test_initialization(self):
        # Test Player initialization
        player = Player(100, 100, True, self.controls, self.weapon_controls, self.resistance)
        self.assertEqual(player.start_x, 100)
        self.assertEqual(player.start_y, 100)
        self.assertEqual(player.right_side, True)
        self.assertEqual(player.controls, self.controls)
        self.assertEqual(player.weapon_controls, self.weapon_controls)
        self.assertEqual(player.start_resistance, self.resistance)

    def test_reset(self):
        # Test Player reset method
        player = Player(100, 100, True, self.controls, self.weapon_controls, self.resistance)
        player.reset()
        self.assertFalse(player.has_avatar)
        self.assertEqual(player.index, 0)
        self.assertEqual(player.counter, 0)
        self.assertEqual(player.action, 0)
        self.assertEqual(player.attack_speed, 0)
        self.assertFalse(player.attacking)
        self.assertEqual(player.attack_cooldown, 0)


    def test_take_damage(self):
        hoodie_fist_attack = Attack('sword', 100, 100, 100, 2, 500, 0, 200)
        player = Player(100, 100, True, self.controls, self.weapon_controls, self.resistance)
        avatar_mock = Avatar('HOODIE_GIRL', [hoodie_fist_attack, ], 'assets/hoodie_girl.png', 0, 200, HOODIE_GIRL_ANIMATION_STEPS, HOODIE_GIRL_SIZE, HOODIE_GIRL_SCALE, HOODIE_GIRL_OFFSET)
        player.fill_animation_list(avatar_mock.animation_list)

        #self.resistance -= damage
        #dx = push_back * direction
        #if int(self.resistance / 10) <= 0:
        #    self.resistance = 0
        #    self.rect.x += dx
        #else:
        #    self.rect.x += (dx // int(self.resistance / 10))

        direction_mock = -1
        if player.right_side:
            direction_mock = 1

        resistance_mock = (player.resistance - hoodie_fist_attack.damage)
        dx_mock = hoodie_fist_attack.push_back * direction_mock
        if int(resistance_mock / 10) <= 0:
            resistance_mock = 0
            take_damage_mock = player.rect.x + dx_mock
        else:
            take_damage_mock = player.rect.x + (dx_mock // int(resistance_mock / 10))

        player.take_damage(hoodie_fist_attack.damage, hoodie_fist_attack.push_back, direction_mock)
        self.assertEqual(player.rect.x, take_damage_mock)

    def tearDown(self):
        pygame.quit()

class TestRightPlayer(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.controls = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_KP_ENTER)
        self.weapon_controls = (pygame.K_KP1, pygame.K_KP2)
        self.resistance = 100

    def test_right_player_initialization(self):
        # Test Right_Player initialization
        right_player = Right_Player(200, 200, self.resistance)
        self.assertEqual(right_player.start_x, 200)
        self.assertEqual(right_player.start_y, 200)
        self.assertTrue(right_player.right_side)
        self.assertEqual(right_player.controls, (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_KP_ENTER))
        self.assertEqual(right_player.weapon_controls, (pygame.K_KP1, pygame.K_KP2))
        self.assertEqual(right_player.start_resistance, self.resistance)


    def tearDown(self):
        pygame.quit()

class TestLeftPlayer(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.controls = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_KP_ENTER)
        self.weapon_controls = (pygame.K_KP1, pygame.K_KP2)
        self.resistance = 100

    def test_left_player_initialization(self):
        # Test Left_Player initialization
        left_player = Left_Player(300, 300, self.resistance)
        self.assertEqual(left_player.start_x, 300)
        self.assertEqual(left_player.start_y, 300)
        self.assertFalse(left_player.right_side)
        self.assertEqual(left_player.controls, (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE))
        self.assertEqual(left_player.weapon_controls, (pygame.K_1, pygame.K_2))
        self.assertEqual(left_player.start_resistance, self.resistance)


    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()