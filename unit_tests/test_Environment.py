import unittest
from unittest.mock import MagicMock

import pygame

from Environment import Landscape, Attack, Obstacle


class TestLandscape(unittest.TestCase):
    def setUp(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.background_file_name = 'assets/evening background game.png'
        self.menu_x = 100
        self.menu_y = 100
        self.obstacle_mock = Obstacle(self.background_file_name, 150, 150, 50, 50)
        self.obstacles = [self.obstacle_mock]
        self.landscape = Landscape("Test Landscape", self.obstacles, self.background_file_name, self.menu_x,
                                   self.menu_y)

    def test_draw_background(self):
        screen_mock = MagicMock()
        self.landscape.draw_background(screen_mock)
        screen_mock.blit.assert_called_once()

    def test_draw_obstacles(self):
        self.obstacles[0].draw(self.screen)

    def test_draw_in_menu(self):
        screen_mock = self.screen
        self.assertFalse(self.landscape.draw_in_menu(screen_mock))


class TestAttack(unittest.TestCase):
    def setUp(self):
        self.name = "Test Attack"
        self.hit_range_front = 100
        self.hit_range_up = 50
        self.hit_range_down = 50
        self.damage = 10
        self.push_back = 0.5
        self.menu_x = 100
        self.menu_y = 100
        self.attack = Attack(self.name, self.hit_range_front, self.hit_range_up, self.hit_range_down, self.damage,
                             self.push_back, self.menu_x, self.menu_y)

    def test_get_damage(self):
        self.assertEqual(self.attack.get_damage(), self.damage)

    def test_get_push_back_distance(self):
        target_mock = MagicMock()
        target_mock.resistance = 50
        self.assertEqual(self.attack.get_push_back_distance(target_mock),
                         self.push_back * (100 / target_mock.resistance))

    def test_get_hit_rect(self):
        attacker_mock = MagicMock()
        attacker_mock.rect.centerx = 100
        attacker_mock.rect.y = 200
        attacker_mock.rect.width = 50
        attacker_mock.rect.height = 100
        direction = 1  # Right
        hit_rect = self.attack.get_hit_rect(attacker_mock, direction)
        self.assertEqual(hit_rect, pygame.Rect(100, 200, 45, 100))


if __name__ == '__main__':
    unittest.main()
