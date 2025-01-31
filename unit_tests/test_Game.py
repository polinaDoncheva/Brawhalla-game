import unittest
import pygame
from Game import Game
from Environment import Button
from Players import Player, Right_Player, Left_Player


class TestGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = Game()

    def test_load_buttons(self):
        self.assertIsInstance(self.game.reset_button, Button)
        self.assertIsInstance(self.game.start_button, Button)
        self.assertIsInstance(self.game.exit_button, Button)
        self.assertIsInstance(self.game.first_wins_button, Button)
        self.assertIsInstance(self.game.second_wins_button, Button)
        self.assertIsInstance(self.game.go_to_menu_button, Button)
        self.assertIsInstance(self.game.choose_landscape1_button, Button)
        self.assertIsInstance(self.game.choose_landscape2_button, Button)
        self.assertIsInstance(self.game.choose_attack1_button, Button)
        self.assertIsInstance(self.game.choose_attack2_button, Button)
        self.assertIsInstance(self.game.player1_button, Button)
        self.assertIsInstance(self.game.player2_button, Button)
        self.assertIsInstance(self.game.choose_avatar1_button, Button)
        self.assertIsInstance(self.game.choose_avatar2_button, Button)

    def test_load_fighter_images(self):
        self.assertIsInstance(self.game.avatars[0].attacks[0], pygame.sprite.Sprite)
        self.assertIsInstance(self.game.avatars[1].attacks[0], pygame.sprite.Sprite)

    def test_load_landscapes(self):
        self.assertIsInstance(self.game.obstacles1[0], pygame.sprite.Sprite)
        self.assertIsInstance(self.game.obstacles1[1], pygame.sprite.Sprite)
        self.assertIsInstance(self.game.landscapes[0].obstacles[0], pygame.sprite.Sprite)
        self.assertIsInstance(self.game.landscapes[1].obstacles[0], pygame.sprite.Sprite)
        self.assertIsInstance(self.game.landscapes[2].obstacles[0], pygame.sprite.Sprite)

    def test_load_attacks(self):
        self.assertIsInstance(self.game.attacks[0], pygame.sprite.Sprite)
        self.assertIsInstance(self.game.attacks[1], pygame.sprite.Sprite)

    def test_create_players(self):
        self.assertIsInstance(self.game.left, Player)

        self.assertIsInstance(self.game.right, Player)


    def test_execute_main_menu(self):
        self.game.MAIN_MENU = True

    def test_execute_landscape_menu(self):
        self.game.LANDSCAPE_MENU[0] = True

    def test_execute_attack_menu(self):
        self.game.ATTACK_MENU[0] = True

    def test_execute_avatar_menu(self):
        self.game.AVATAR_MENU[0] = True

    def test_reset_game(self):
        self.game.reset_game()
        self.assertEqual(self.game.rounds_counter, 0)
        self.assertEqual(self.game.player1_score, 0)
        self.assertEqual(self.game.player2_score, 0)

    def test_reset_round(self):
        self.game.reset_round()
        self.assertEqual(self.game.game_over1, 0)
        self.assertEqual(self.game.game_over2, 0)
        self.assertEqual(self.game.game_over_cooldown, 0)

    def test_execute_game_over(self):
        self.game.game_over_cooldown = 3
        self.assertFalse(self.game.execute_game_over())

    def test_run_game(self):
        self.assertTrue(self.game.run_game())

if __name__ == '__main__':
    unittest.main()