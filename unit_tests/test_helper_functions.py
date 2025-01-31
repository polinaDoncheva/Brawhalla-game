import unittest
import random

import pygame
from helper_functions import (
    get_image_from_text,
    load_images,
    random_choice_landscape,
)


class TestPygameFunctions(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def test_get_image_from_text(self):
        font = pygame.font.SysFont(None, 30)
        color = (255, 255, 255)
        text = "Hello"
        image = get_image_from_text(text, font, color)

    def test_load_images(self):
        sprite_sheet = pygame.image.load('assets/hoodie_girl.png')
        animation_steps = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        size = 32  # Example size
        scale = 2  # Example scale
        offset = (0, 0)  # Example offset
        animation_list = load_images(sprite_sheet, animation_steps, size, scale, offset)


    def test_random_choice_landscape(self):
        landscape1_type = 1
        landscape2_type = 2
        random.seed(123)  # Setting seed for reproducibility
        landscape_type = random_choice_landscape(landscape1_type, landscape2_type)
        self.assertIn(landscape_type, [1, 2])

    def tearDown(self):
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
