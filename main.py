import sys
import random
import pygame
from win32api import GetSystemMetrics
import random

pygame.init()
screen = pygame.display.set_mode([GetSystemMetrics(0), GetSystemMetrics(1)])
clock = pygame.time.Clock()
array_trail = []
running = True
teleport_flag = False
passed_levels_count = 0
maps = [[['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']],
        [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]]

random_map = random.randint(0, len(maps) - 1)
if random_map == 0 or random_map == 1:
    global_width_height = 40
else:
    global_width_height = 40

# background_photo = pygame.image.load("background_anton.png")

left_sprite = pygame.image.load("sprite_anton1_left.png")
right_sprite = pygame.image.load("sprite_anton1.png")

array_left_sprites = [pygame.image.load("sprite_anton2_left.png"), pygame.image.load("sprite_anton3_left.png"),
                      pygame.image.load("sprite_anton3_left.png"), pygame.image.load("sprite_anton4_left.png"),
                      pygame.image.load("sprite_anton5_left.png"), pygame.image.load("sprite_anton6_left.png"),
                      pygame.image.load("sprite_anton7_left.png")]

array_right_sprites = [pygame.image.load("sprite_anton2.png"), pygame.image.load("sprite_anton3.png"),
                       pygame.image.load("sprite_anton3.png"), pygame.image.load("sprite_anton4.png"),
                       pygame.image.load("sprite_anton5.png"), pygame.image.load("sprite_anton6.png"),
                       pygame.image.load("sprite_anton7.png")]


def check_collision(pos1, pos2):
    # pos1 => border

    w1 = abs(pos1[0] - pos1[2])
    h1 = abs(pos1[1] - pos1[3])
    w2 = abs(pos2[0] - pos2[2])
    h2 = abs(pos2[1] - pos2[3])

    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]

    collision_x = x1 + w1 >= x2 and x2 + w2 >= x1
    collision_y = y1 + h1 >= y2 and y2 + h2 >= y1
    return collision_x and collision_y


def generate_player_trail(x, y):
    global array_trail
    array_trail.append((x + random.randint(-2, 2), y + random.randint(-2, 2), 0))


def map_trailing(value, left_min, left_max, right_min, right_max):
    left_span = left_max - left_min
    right_span = right_max - right_min
    value_scaled = float(value - left_min) / float(left_span)
    return right_min + (value_scaled * right_span)


def draw_player_trail(player_size):
    global array_trail
    player_trail_live = 9

    for i in range(0, len(array_trail)):
        if i >= len(array_trail):
            break

        trail = array_trail[i]
        array_trail[i] = (trail[0], trail[1], trail[2] + 1)  # добавляем индекс
        if trail[2] > player_trail_live:
            array_trail.remove(array_trail[i])

        idx = trail[2]
        size = map_trailing(player_trail_live - idx, player_trail_live, 0, player_size * 0.9, 0)
        if size < 0:
            continue
        # от зеленого до белого
        color_v = int(map_trailing(idx, 0, player_trail_live, 0, 200))
        if color_v < 0:
            color_v = 0
        # прозрачность
        color_alpha = int(map_trailing(idx, 0, player_trail_live, 100, 0))
        color = (color_v, 255, color_v, color_alpha)

        center = (trail[0] - size / 2, trail[1] - size / 2)
        radius = size
        # я скопировал и в душе не ебу как оно меняет прозрачность цвета
        target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, (radius, radius, radius, radius))
        screen.blit(shape_surf, target_rect)


class CharacterCreator:
    def __init__(self, start_position, width, height):
        self.position_x = start_position[0]
        self.position_y = start_position[1]
        self.width = width
        self.height = height
        self.dirX = 0  # направление по x
        self.dirY = 0  # направление по y
        self.dirX_last = 1
        self.speed = 8
        self.forset_x = 0
        self.forset_y = 0
        self.tp_check_x = True
        self.tp_check_y = True
        self.animation = 0

    def draw_object(self):
        draw_player_trail(self.width)
        self.animation += 1
        if self.animation >= 30:
            self.animation = 0

        if self.dirY == 1 or self.dirY == -1:
            if self.dirX_last == 1:
                screen.blit(array_right_sprites[self.animation // 5],
                            (self.position_x - self.width // 2, self.position_y - self.height // 2))
            else:
                screen.blit(array_left_sprites[self.animation // 5],
                            (self.position_x - self.width // 2, self.position_y - self.height // 2))
        if self.dirX == 0 and self.dirY == 0:
            self.animation = 0
            if self.dirX_last == 1:
                screen.blit(right_sprite,
                            (self.position_x - self.width // 2, self.position_y - self.height // 2))
            elif self.dirX_last == -1:
                screen.blit(left_sprite,
                            (self.position_x - self.width // 2, self.position_y - self.height // 2))
            else:
                screen.blit(right_sprite,
                            (self.position_x - self.width // 2, self.position_y - self.height // 2))
        if self.dirX == 1:
            screen.blit(array_right_sprites[self.animation // 5], (self.position_x - self.width // 2, self.position_y - self.height // 2))
        if self.dirX == -1:
            screen.blit(array_left_sprites[self.animation // 5], (self.position_x - self.width // 2, self.position_y - self.height // 2))
        # square = pygame.Rect(self.position_x - self.width // 2, self.position_y - self.width // 2,
        #                      self.width, self.width)
        # pygame.draw.rect(screen, (28, 217, 34), square, 0)
        # screen.blit(main_character_photo, (self.position_x - self.width // 2, self.position_y - self.width // 2))

    def move(self):
        is_colliding_x = False
        is_colliding_y = False
        self.tp_check_y = True
        self.tp_check_x = True
        for i in range(0, len(borders)):
            border = borders[i]
            border_pos = border.pos
            player_pos = (self.position_x - self.width // 2, self.position_y - self.height // 2, self.position_x +
                          self.width // 2, self.position_y + self.height // 2)

            # просчет куда попадет игрок отдельно по x и y
            new_player_pos_x = (player_pos[0] + self.dirX * self.speed, player_pos[1], player_pos[2] +
                                self.dirX * self.speed, player_pos[3])
            new_player_pos_y = (player_pos[0], player_pos[1] + self.dirY * self.speed, player_pos[2],
                                player_pos[3] + self.dirY * self.speed)

            teleport_x = self.position_x + self.dirX * self.speed * 7
            teleport_y = self.position_y + self.dirY * self.speed * 7

            player_pos_teleport = (teleport_x - self.width // 2, teleport_y - self.width // 2, teleport_x +
                                   self.width // 2, teleport_y + self.width // 2)

            new_player_pos_x_teleport = (player_pos_teleport[0] + self.dirX * self.speed, player_pos_teleport[1],
                                         player_pos_teleport[2] + self.dirX * self.speed, player_pos_teleport[3])
            new_player_pos_y_teleport = (player_pos_teleport[0], player_pos_teleport[1] + self.dirY * self.speed,
                                         player_pos_teleport[2], player_pos_teleport[3] + self.dirY * self.speed)

            if check_collision(border_pos, new_player_pos_x_teleport):
                self.tp_check_x = False
            if check_collision(border_pos, new_player_pos_y_teleport):
                self.tp_check_y = False

            if new_player_pos_x_teleport[0] < 0 or new_player_pos_x_teleport[2] > GetSystemMetrics(0):
                self.tp_check_x = False
            if new_player_pos_y_teleport[1] < 0 or new_player_pos_y_teleport[3] > GetSystemMetrics(1):
                self.tp_check_y = False

            # проверяем если в будущем игрок врежитсся в стенку по x и y отдельно
            if is_colliding_x is False and check_collision(border_pos, new_player_pos_x) is True:
                is_colliding_x = True
                if self.dirX == 1:
                    self.forset_x = abs(player_pos[2] - border.pos[0]) - 1
                if self.dirX == -1:
                    self.forset_x = abs(player_pos[0] - border.pos[2]) - 1
            if is_colliding_y is False and check_collision(border_pos, new_player_pos_y) is True:
                is_colliding_y = True
                if self.dirY == 1:
                    self.forset_y = abs(player_pos[3] - border.pos[1]) - 1
                if self.dirY == -1:
                    self.forset_y = abs(player_pos[1] - border.pos[3]) - 1

        # forset_y , forset_x для прелигания к стенкам
        if is_colliding_x is False:
            self.position_x += self.dirX * self.speed
        else:
            if self.forset_x < self.speed:
                self.position_x += self.dirX * self.forset_x

        if is_colliding_y is False:
            self.position_y += self.dirY * self.speed
        else:
            if self.forset_y < self.speed:
                self.position_y += self.dirY * self.forset_y

        generate_player_trail(self.position_x, self.position_y)


class Enemies:
    def __init__(self, start_position, width, direction_x, direction_y, subsequence, speed):
        self.position_x = start_position[0]
        self.position_y = start_position[1]
        self.width = width
        self.height = width
        if self.position_x < direction_x[0]:
            self.dirX = 1
        elif self.position_x > direction_x[0]:
            self.dirX = -1
        else:
            self.dirX = 0

        if self.position_y < direction_y[0]:
            self.dirY = 1
        elif self.position_y > direction_y[0]:
            self.dirY = -1
        else:
            self.dirY = 0
        self.destination_X_direction = direction_x
        self.destination_Y_direction = direction_y
        self.destination_X_index = 0
        self.destination_Y_index = 0
        self.subsequence = subsequence
        self.index_subsequence = 0
        self.speed = speed
        self.pos = ([self.position_x - self.width // 2, self.position_y - self.height // 2,
                     self.position_x + self.width // 2, self.position_y + self.height // 2])

    def draw_object(self):

        rectangle = pygame.Rect(self.position_x - self.width // 2, self.position_y - self.height // 2,
                                self.width, self.height)
        pygame.draw.rect(screen, (255, 0, 0), rectangle, 0)

    def move(self):
        if self.subsequence[self.index_subsequence] == 'X':
            if not (self.destination_X_direction[self.destination_X_index] - self.speed <= self.position_x
                    <= self.destination_X_direction[self.destination_X_index] + self.speed):
                self.position_x += self.speed * self.dirX
            else:
                self.position_x += self.destination_X_direction[self.destination_X_index] - self.position_x
                self.destination_X_index += 1
                self.index_subsequence += 1
                if self.index_subsequence == len(self.subsequence):
                    self.index_subsequence = 0
                if self.destination_X_index == len(self.destination_X_direction):
                    self.destination_X_index = 0
                if self.position_x < self.destination_X_direction[self.destination_X_index]:
                    self.dirX = 1
                elif self.position_x > self.destination_X_direction[self.destination_X_index]:
                    self.dirX = -1
                else:
                    self.dirX = 0

        if self.subsequence[self.index_subsequence] == 'Y':
            if not (self.destination_Y_direction[self.destination_Y_index] - self.speed <= self.position_y
                    <= self.destination_Y_direction[self.destination_Y_index] + self.speed):
                self.position_y += self.speed * self.dirY
            else:
                self.position_y += self.destination_Y_direction[self.destination_Y_index] - self.position_y
                self.destination_Y_index += 1
                self.index_subsequence += 1
                if self.index_subsequence == len(self.subsequence):
                    self.index_subsequence = 0
                if self.destination_Y_index == len(self.destination_Y_direction):
                    self.destination_Y_index = 0
                if self.position_y < self.destination_Y_direction[self.destination_Y_index]:
                    self.dirY = 1
                elif self.position_y > self.destination_Y_direction[self.destination_Y_index]:
                    self.dirY = -1
                else:
                    self.dirY = 0

        if self.subsequence[self.index_subsequence] == 'X-Y':
            if not (self.destination_X_direction[self.destination_X_index] - self.speed <= self.position_x
                    <= self.destination_X_direction[self.destination_X_index] + self.speed):
                self.position_x += self.speed * self.dirX
            if not (self.destination_Y_direction[self.destination_Y_index] - self.speed <= self.position_y
                    <= self.destination_Y_direction[self.destination_Y_index] + self.speed):
                self.position_y += self.speed * self.dirY
            if (self.destination_X_direction[self.destination_X_index] - self.speed <= self.position_x
                    <= self.destination_X_direction[self.destination_X_index] + self.speed) and \
                    (self.destination_Y_direction[self.destination_Y_index] - self.speed <= self.position_y
                     <= self.destination_Y_direction[self.destination_Y_index] + self.speed):
                self.position_x += self.destination_X_direction[self.destination_X_index] - self.position_x
                self.position_y += self.destination_Y_direction[self.destination_Y_index] - self.position_y
                self.destination_Y_index += 1
                self.destination_X_index += 1
                self.index_subsequence += 1
                if self.index_subsequence == len(self.subsequence):
                    self.index_subsequence = 0
                if self.destination_Y_index == len(self.destination_Y_direction):
                    self.destination_Y_index = 0
                if self.destination_X_index == len(self.destination_X_direction):
                    self.destination_X_index = 0
                if self.position_y < self.destination_Y_direction[self.destination_Y_index]:
                    self.dirY = 1
                elif self.position_y > self.destination_Y_direction[self.destination_Y_index]:
                    self.dirY = -1
                else:
                    self.dirY = 0
                if self.position_x < self.destination_X_direction[self.destination_X_index]:
                    self.dirX = 1
                elif self.position_x > self.destination_X_direction[self.destination_X_index]:
                    self.dirX = -1
                else:
                    self.dirX = 0


def generate_enemies(speed_increase):
    if random_map == 0:
        array = [Enemies([200, 80], 40, [500, 200], [80], ['X'], 5 + speed_increase),
                 Enemies([1720, 650], 40, [1600, 1720], [320, 400, 650], ['Y', 'X', 'Y', 'X', 'Y'], 5 + speed_increase),
                 Enemies([200, 200], 40, [320, 440, 600, 200], [650, 200, 650, 200], ['Y', 'X'], 5 + speed_increase),
                 Enemies([1180, 610], 40, [1580, 1180, 1580, 1180], [720, 840, 1000, 610], ['Y', 'X'], 5 + speed_increase),
                 Enemies([200, 1000], 40, [300, 540, 740, 820, 200], [820, 1000, 670, 1000], ['X', 'X-Y', 'X-Y', 'X', 'Y', 'X', 'Y'], 5 + speed_increase),
                 Enemies([1480, 150], 40, [1050, 1350, 1050, 1480], [360, 480, 150], ['Y', 'X', 'X', 'Y', 'X', 'X', 'Y'], 5 + speed_increase),
                 ]
    elif random_map == 1:
        array = [Enemies([1760, 1000], 40, [1460, 1200, 1500, 1200, 1460, 1760], [700, 1000, 700, 1000], ['X-Y', 'X', 'X-Y'], 5 + speed_increase),
                 Enemies([160, 1000], 40, [460, 720, 420, 720, 460, 160], [700, 1000, 700, 1000], ['X-Y', 'X', 'X-Y'], 5 + speed_increase),
                 Enemies([760, 400], 40, [1160, 760], [710, 400], ['X', 'Y'], 5 + speed_increase),
                 Enemies([1160, 710], 40, [760, 1160], [400, 710], ['X', 'Y'], 5 + speed_increase),
                 Enemies([80, 90], 40, [480, 780, 480, 80], [320, 120, 280, 120, 320, 90], ['Y', 'X', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'X', 'Y'], 5 + speed_increase),
                 Enemies([1840, 90], 40, [1440, 1140, 1440, 1840], [320, 120, 280, 120, 320, 90], ['Y', 'X', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'X', 'Y'], 5 + speed_increase),
                 ]

    else:
        array = []
    return array


class BordersCreator:
    def __init__(self, start_position, width, height):
        self.position_x = start_position[0]
        self.position_y = start_position[1]
        self.width = width
        self.height = height
        self.pos = ([self.position_x - self.width // 2, self.position_y - self.height // 2,
                     self.position_x + self.width // 2, self.position_y + self.height // 2])

    def draw_object(self):
        rectangle = pygame.Rect(self.position_x - self.width // 2, self.position_y - self.height // 2,
                                self.width, self.height)
        pygame.draw.rect(screen, (59, 59, 59), rectangle, 0)


def generate_borders():
    array = []
    for i in range(GetSystemMetrics(1) // global_width_height):
        for j in range(GetSystemMetrics(0) // global_width_height):
            if maps[random_map][i][j] == '1':
                array.append(BordersCreator([j * global_width_height + global_width_height // 2,
                                             i * global_width_height + global_width_height // 2],
                                            global_width_height, global_width_height))

    return array


if random_map == 0:
    main_character = CharacterCreator([1670, 200], 24, 54)
elif random_map == 1:
    main_character = CharacterCreator([960, 100], 24, 54)
else:
    main_character = None
borders = generate_borders()
enemies_array = generate_enemies(passed_levels_count)


def draw_background():
    screen.blit(background_photo, (0, 0))


def border_draw():
    for border in borders:
        border.draw_object()


def enemies_draw():
    for enemies in enemies_array:
        enemies.draw_object()


def finish(x, y):
    if len(enemies_array) == 0:
        if random_map == 0:
            if 40 <= x <= 120 and 1040 <= y <= 1200:
                return True
        if random_map == 1:
            if 800 <= x <= 1200 and 1040 <= y <= 1200:
                return True


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            enemies_killed = []
            for index in range(len(enemies_array)):
                enemy_x = enemies_array[index].position_x
                enemy_y = enemies_array[index].position_y
                enemy_pos = (enemies_array[index].position_x - enemies_array[index].width // 2,
                             enemies_array[index].position_y - enemies_array[index].width // 2,
                             enemies_array[index].position_x + enemies_array[index].width // 2,
                             enemies_array[index].position_y + enemies_array[index].width // 2)
                main_character_pos = (main_character.position_x - main_character.width // 2 - 10,
                                      main_character.position_y - main_character.width // 2 - 10,
                                      main_character.position_x + main_character.width // 2 + 10,
                                      main_character.position_y + main_character.width // 2 + 10)
                if check_collision(enemy_pos, main_character_pos):
                    enemies_killed.append(index)
            k = 0
            for index in range(len(enemies_killed)):
                enemies_array.pop(enemies_killed[index - k])
                k += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    if (keys[pygame.K_w] and keys[pygame.K_s]) or (keys[pygame.K_w] is False and keys[pygame.K_s] is False):
        main_character.dirY = 0
    else:
        if keys[pygame.K_w]:
            main_character.dirY = -1
        elif keys[pygame.K_s]:
            main_character.dirY = 1

    if (keys[pygame.K_a] and keys[pygame.K_d]) or (keys[pygame.K_a] is False and keys[pygame.K_d] is False):
        main_character.dirX = 0
    else:
        if keys[pygame.K_a]:
            main_character.dirX = -1
        elif keys[pygame.K_d]:
            main_character.dirX = 1

    if keys[pygame.K_SPACE] and teleport_flag is False:
        teleport_flag = True
        if main_character.dirX != 0:
            if main_character.tp_check_x is True:
                main_character.position_x += main_character.dirX * main_character.speed * 7
        if main_character.dirY != 0:
            if main_character.tp_check_y is True:
                main_character.position_y += main_character.dirY * main_character.speed * 7

    if teleport_flag is True and keys[pygame.K_SPACE] is False:
        teleport_flag = False

    main_character.move()
    for enemies1 in enemies_array:
        enemies1.move()

    screen.fill([99, 99, 99])
    # screen.blit(main_character_photo, (self.position_x - self.width // 2, self.position_y - self.width // 2))
    main_character.draw_object()
    border_draw()
    enemies_draw()
    if main_character.dirX != 0:
        main_character.dirX_last = main_character.dirX
    if finish(main_character.position_x, main_character.position_y):
        random_map = random.randint(0, len(maps) - 1)
        passed_levels_count += 1
        borders = generate_borders()
        enemies_array = generate_enemies(passed_levels_count * 2)
        if random_map == 0:
            main_character.position_x = 1670
            main_character.position_y = 200
        if random_map == 1:
            main_character.position_x = 960
            main_character.position_y = 100

    pygame.display.update()
