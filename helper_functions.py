import pygame
import random


def get_image_from_text(text, font, color):
    img = font.render(text, True, color)
    return img


def load_images(sprite_sheet, animation_steps, size, scale, offset):
    animation_list = []
    for y, animation in enumerate(animation_steps):
        temp_img_list = []

        for x in range(animation):
            temp_img = sprite_sheet.subsurface(x * size, y * size, size, size)

            temp_img_list.append(pygame.transform.scale(temp_img, (100, 100)))

        animation_list.append(temp_img_list)
    return animation_list


def random_choice_landscape(landscape1_type, landscape2_type):
    if landscape1_type != -1 and landscape2_type != -1:
        landscape_type = random.choice([landscape1_type, landscape2_type])
    elif landscape1_type != -1:
        landscape_type = landscape1_type
    elif landscape2_type != -1:
        landscape_type = landscape2_type
    else:
        landscape_type = 0
    return landscape_type
