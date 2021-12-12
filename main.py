import math
import sys
import random
import pygame


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()
scale_x = screen_width / 1920
clock = pygame.time.Clock()
array_trail = []
running = True
teleport_flag = False
passed_levels_count = 0
maps = [[['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']],
        [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']],
        [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]]

random_map = random.randint(0, len(maps) - 1)
global_width_height = int(40 * scale_x)


background_photo = pygame.image.load("background.png")
background_photo = pygame.transform.scale(background_photo, ((int(40 * scale_x)), int(40 * scale_x)))
walls_photo = pygame.image.load("water3.png")
walls_photo = pygame.transform.scale(walls_photo, ((int(40 * scale_x)), int(40 * scale_x)))
enemy_photo = pygame.image.load("mini_monster_slug.png")
enemy_photo = pygame.transform.scale(enemy_photo, ((int(40 * scale_x)), int(40 * scale_x)))
enemy_photo_right = pygame.image.load("mini_monster_slug_right.png")
enemy_photo_right = pygame.transform.scale(enemy_photo_right, ((int(40 * scale_x)), int(40 * scale_x)))


left_sprite = pygame.image.load("sprite_anton1_left.png")
left_sprite = pygame.transform.scale(left_sprite, ((int(22 * scale_x)), int(55 * scale_x)))
right_sprite = pygame.image.load("sprite_anton1.png")
right_sprite = pygame.transform.scale(right_sprite, ((int(22 * scale_x)), int(55 * scale_x)))

array_left_sprites = [pygame.image.load("sprite_anton2_left.png"), pygame.image.load("sprite_anton3_left.png"),
                      pygame.image.load("sprite_anton3_left.png"), pygame.image.load("sprite_anton4_left.png"),
                      pygame.image.load("sprite_anton5_left.png"), pygame.image.load("sprite_anton6_left.png"),
                      pygame.image.load("sprite_anton7_left.png")]

for k in range(len(array_left_sprites)):
    array_left_sprites[k] = pygame.transform.scale(array_left_sprites[k], ((int(22 * scale_x)), int(55 * scale_x)))

array_right_sprites = [pygame.image.load("sprite_anton2.png"), pygame.image.load("sprite_anton3.png"),
                       pygame.image.load("sprite_anton3.png"), pygame.image.load("sprite_anton4.png"),
                       pygame.image.load("sprite_anton5.png"), pygame.image.load("sprite_anton6.png"),
                       pygame.image.load("sprite_anton7.png")]

for z in range(len(array_left_sprites)):
    array_right_sprites[z] = pygame.transform.scale(array_right_sprites[z], ((int(22 * scale_x)), int(55 * scale_x)))


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
    if len(array_trail) == 0 or array_trail[len(array_trail) - 1][2] > 1:
        array_trail.append((x + random.randint(-3, 3), y + random.randint(-3, 3), 0))


def map_trailing(value, left_min, left_max, right_min, right_max):
    left_span = left_max - left_min
    right_span = right_max - right_min
    value_scaled = float(value - left_min) / float(left_span)
    return right_min + (value_scaled * right_span)


def draw_player_trail(player_size):
    global array_trail
    player_trail_live = 15

    for i in range(0, len(array_trail)):
        if i >= len(array_trail):
            break

        trail = array_trail[i]
        array_trail[i] = (trail[0], trail[1], trail[2] + 1)  # добавляем индекс
        if trail[2] > player_trail_live:
            array_trail.remove(array_trail[i])

        idx = trail[2]
        size = map_trailing(player_trail_live - idx, player_trail_live, 0, player_size * 0.4, 0)
        if size < 0:
            continue
        # от зеленого до белого
        color_v = int(map_trailing(idx, 0, player_trail_live, 255, 255))
        if color_v < 0:
            color_v = 0
        # прозрачность
        color_alpha = int(map_trailing(idx, 0, player_trail_live, 150, 0))
        color = (color_v, color_v, color_v, color_alpha)

        center = (trail[0], trail[1] - size / 2 + main_character.height/2 - 7)
        radius = size
        # я скопировал и в душе не ебу как оно меняет прозрачность цвета
        target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        # pygame.draw.rect(shape_surf, color, (radius, radius, radius, radius))
        pygame.draw.circle(shape_surf, color, (radius, radius), radius/2)
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
        self.speed = int(10 * scale_x)
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

        pos = self.position_x - self.width // 2, self.position_y - self.height // 2
        if self.dirY == 1 or self.dirY == -1:
            if self.dirX_last == 1:
                screen.blit(array_right_sprites[self.animation // 5],
                            pos)
            else:
                screen.blit(array_left_sprites[self.animation // 5],
                            (self.position_x - self.width // 2, self.position_y - self.height // 2))
        if self.dirX == 0 and self.dirY == 0:
            self.animation = 0
            if self.dirX_last == 1:
                screen.blit(right_sprite,
                            pos)
            elif self.dirX_last == -1:
                screen.blit(left_sprite,
                            pos)
            else:
                screen.blit(right_sprite,
                            pos)
        if self.dirX == 1:
            screen.blit(array_right_sprites[self.animation // 5], pos)
        if self.dirX == -1:
            screen.blit(array_left_sprites[self.animation // 5], pos)

    def move(self):
        is_colliding_x = False
        is_colliding_y = False
        is_colliding_xy = False
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
            new_player_pos_xy = (player_pos[0] + self.dirX * self.speed, player_pos[1] + self.dirY * self.speed,
                                 player_pos[2] + self.dirX * self.speed, player_pos[3] + self.dirY * self.speed)

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

            if new_player_pos_x_teleport[0] < 0 or new_player_pos_x_teleport[2] > screen_width:
                self.tp_check_x = False
            if new_player_pos_y_teleport[1] < 0 or new_player_pos_y_teleport[3] > screen_height:
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
            if is_colliding_xy is False and check_collision(border_pos, new_player_pos_xy) is True:
                is_colliding_xy = True
                if self.dirY == 1:
                    self.forset_y = 0
                if self.dirY == -1:
                    self.forset_y = 0

        if random_map == 0:
            if int(40 * scale_x) <= self.position_x <= int(120 * scale_x) and int(1040 * scale_x) <= self.position_y <= int(1200 * scale_x) and self.dirY == 1:
                is_colliding_y = True
        if random_map == 1:
            if int(800 * scale_x) <= self.position_x <= int(1200 * scale_x) and int(1040 * scale_x) <= self.position_y <= int(1200 * scale_x) and self.dirY == 1:
                is_colliding_y = True
        if random_map == 2:
            if int(800 * scale_x) <= self.position_x <= int(1200 * scale_x) and int(-200 * scale_x) <= self.position_y <= int(40 * scale_x) and self.dirY == -1:
                is_colliding_y = True

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

        if (self.dirX != 0 or self.dirY != 0) and not is_colliding_y and not is_colliding_x and not is_colliding_xy:
            generate_player_trail(self.position_x, self.position_y)


class Enemy:
    def __init__(self, x, y, width, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = width
        self.dirX = 0
        self.dirY = 0
        self.speed = speed
        self.moving = True

    def draw_object(self):
        if self.dirX == -1:
            screen.blit(enemy_photo, (self.x - self.width // 2, self.y - self.height // 2))
        else:
            screen.blit(enemy_photo_right, (self.x - self.width // 2, self.y - self.height // 2))

    def move(self):
        if random.randint(1, 50) == 1:
            self.dirX = random.randint(-1, 1)
            self.dirY = random.randint(-1, 1)

        is_colliding_x = False
        is_colliding_y = False
        is_colliding_xy = False
        forset_x = 0
        forset_y = 0
        for i in range(0, len(borders)):
            border = borders[i]
            border_pos = border.pos
            enemy_pos1 = (self.x - self.width // 2, self.y - self.height // 2, self.x +
                          self.width // 2, self.y + self.height // 2)

            # просчет куда попадет игрок отдельно по x и y
            new_enemy_pos_x = (enemy_pos1[0] + self.dirX * self.speed, enemy_pos1[1], enemy_pos1[2] +
                                self.dirX * self.speed, enemy_pos1[3])
            new_enemy_pos_y = (enemy_pos1[0], enemy_pos1[1] + self.dirY * self.speed, enemy_pos1[2],
                                enemy_pos1[3] + self.dirY * self.speed)
            new_enemy_pos_xy = (enemy_pos1[0] + self.dirX * self.speed, enemy_pos1[1] + self.dirY * self.speed,
                                 enemy_pos1[2] + self.dirX * self.speed, enemy_pos1[3] + self.dirY * self.speed)

            # проверяем если в будущем врежится в стенку по x и y отдельно
            if is_colliding_x is False and check_collision(border_pos, new_enemy_pos_x) is True:
                is_colliding_x = True
                if self.dirX == 1:
                    forset_x = abs(enemy_pos1[2] - border.pos[0]) - 1
                if self.dirX == -1:
                    forset_x = abs(enemy_pos1[0] - border.pos[2]) - 1
            if is_colliding_y is False and check_collision(border_pos, new_enemy_pos_y) is True:
                is_colliding_y = True
                if self.dirY == 1:
                    forset_y = abs(enemy_pos1[3] - border.pos[1]) - 1
                if self.dirY == -1:
                    forset_y = abs(enemy_pos1[1] - border.pos[3]) - 1
            if is_colliding_xy is False and check_collision(border_pos, new_enemy_pos_xy) is True:
                is_colliding_xy = True
                if self.dirY == 1:
                    forset_y = 0
                if self.dirY == -1:
                    forset_y = 0

        if random_map == 2:
            if int(800 * scale_x) <= self.x <= int(1200 * scale_x) and int(-200 * scale_x) <= self.y <= int(40 * scale_x):
                self.dirX *= -1
                self.dirY *= -1

        # forset_y , forset_x для прелигания к стенкам
        if is_colliding_x is False:
            self.x += self.dirX * self.speed
        else:
            if forset_x < self.speed:
                self.x += self.dirX * forset_x

        if is_colliding_y is False:
            self.y += self.dirY * self.speed
        else:
            if forset_y < self.speed:
                self.y += self.dirY * forset_y


class Enemies:
    def __init__(self, start_position, width, direction_x, direction_y, subsequence, speed):
        self.x = start_position[0]
        self.y = start_position[1]
        self.width = width
        self.height = width
        if self.x < direction_x[0]:
            self.dirX = 1
        elif self.x > direction_x[0]:
            self.dirX = -1
        else:
            self.dirX = 0

        if self.y < direction_y[0]:
            self.dirY = 1
        elif self.y > direction_y[0]:
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
        self.pos = ([self.x - self.width // 2, self.y - self.height // 2,
                     self.x + self.width // 2, self.y + self.height // 2])

    def draw_object(self):
        if self.dirX == -1:
            screen.blit(enemy_photo, (self.x - self.width // 2, self.y - self.height // 2))
        elif self.dirX == 1:
            screen.blit(enemy_photo_right, (self.x - self.width // 2, self.y - self.height // 2))

    def move(self):
        if self.subsequence[self.index_subsequence] == 'X':
            if not (self.destination_X_direction[self.destination_X_index] - self.speed <= self.x
                    <= self.destination_X_direction[self.destination_X_index] + self.speed):
                self.x += self.speed * self.dirX
            else:
                self.x += self.destination_X_direction[self.destination_X_index] - self.x
                self.destination_X_index += 1
                self.index_subsequence += 1
                if self.index_subsequence == len(self.subsequence):
                    self.index_subsequence = 0
                if self.destination_X_index == len(self.destination_X_direction):
                    self.destination_X_index = 0
                if self.x < self.destination_X_direction[self.destination_X_index]:
                    self.dirX = 1
                elif self.x > self.destination_X_direction[self.destination_X_index]:
                    self.dirX = -1
                else:
                    self.dirX = 0

        if self.subsequence[self.index_subsequence] == 'Y':
            if not (self.destination_Y_direction[self.destination_Y_index] - self.speed <= self.y
                    <= self.destination_Y_direction[self.destination_Y_index] + self.speed):
                self.y += self.speed * self.dirY
            else:
                self.y += self.destination_Y_direction[self.destination_Y_index] - self.y
                self.destination_Y_index += 1
                self.index_subsequence += 1
                if self.index_subsequence == len(self.subsequence):
                    self.index_subsequence = 0
                if self.destination_Y_index == len(self.destination_Y_direction):
                    self.destination_Y_index = 0
                if self.y < self.destination_Y_direction[self.destination_Y_index]:
                    self.dirY = 1
                elif self.y > self.destination_Y_direction[self.destination_Y_index]:
                    self.dirY = -1
                else:
                    self.dirY = 0

        if self.subsequence[self.index_subsequence] == 'X-Y':
            if not (self.destination_X_direction[self.destination_X_index] - self.speed <= self.x
                    <= self.destination_X_direction[self.destination_X_index] + self.speed):
                self.x += self.speed * self.dirX
            if not (self.destination_Y_direction[self.destination_Y_index] - self.speed <= self.y
                    <= self.destination_Y_direction[self.destination_Y_index] + self.speed):
                self.y += self.speed * self.dirY
            if (self.destination_X_direction[self.destination_X_index] - self.speed <= self.x
                    <= self.destination_X_direction[self.destination_X_index] + self.speed) and \
                    (self.destination_Y_direction[self.destination_Y_index] - self.speed <= self.y
                     <= self.destination_Y_direction[self.destination_Y_index] + self.speed):
                self.x += self.destination_X_direction[self.destination_X_index] - self.x
                self.y += self.destination_Y_direction[self.destination_Y_index] - self.y
                self.destination_Y_index += 1
                self.destination_X_index += 1
                self.index_subsequence += 1
                if self.index_subsequence == len(self.subsequence):
                    self.index_subsequence = 0
                if self.destination_Y_index == len(self.destination_Y_direction):
                    self.destination_Y_index = 0
                if self.destination_X_index == len(self.destination_X_direction):
                    self.destination_X_index = 0
                if self.y < self.destination_Y_direction[self.destination_Y_index]:
                    self.dirY = 1
                elif self.y > self.destination_Y_direction[self.destination_Y_index]:
                    self.dirY = -1
                else:
                    self.dirY = 0
                if self.x < self.destination_X_direction[self.destination_X_index]:
                    self.dirX = 1
                elif self.x > self.destination_X_direction[self.destination_X_index]:
                    self.dirX = -1
                else:
                    self.dirX = 0


def generate_enemies(speed_increase):
    if random_map == 0:
        array = [Enemies([int(200 * scale_x), int(80 * scale_x)], int(40 * scale_x), [int(500 * scale_x), int(200 * scale_x)], [int(80 * scale_x)], ['X'], int((5 + speed_increase) * scale_x)),
                 Enemies([int(1720 * scale_x), int(650 * scale_x)], int(40 * scale_x), [int(1600 * scale_x), int(1720 * scale_x)], [int(320 * scale_x), int(400 * scale_x), int(650 * scale_x)], ['Y', 'X', 'Y', 'X', 'Y'], int((5 + speed_increase) * scale_x)),
                 Enemies([int(200 * scale_x), int(200 * scale_x)], int(40 * scale_x), [int(320 * scale_x), int(440 * scale_x), int(600 * scale_x), int(200 * scale_x)], [int(650 * scale_x), int(200 * scale_x), int(650 * scale_x), int(200 * scale_x)], ['Y', 'X'], int((5 + speed_increase) * scale_x)),
                 Enemies([int(1180 * scale_x), int(610 * scale_x)], int(40 * scale_x), [int(1580 * scale_x), int(1180 * scale_x), int(1580 * scale_x), int(1180 * scale_x)], [int(720 * scale_x), int(840 * scale_x), int(1000 * scale_x), int(610 * scale_x)], ['Y', 'X'], int((5 + speed_increase) * scale_x)),
                 Enemies([int(200 * scale_x), int(1000 * scale_x)], int(40 * scale_x), [int(300 * scale_x), int(540 * scale_x), int(740 * scale_x), int(820 * scale_x), int(200 * scale_x)], [int(820 * scale_x), int(1000 * scale_x), int(670 * scale_x), int(1000 * scale_x)], ['X', 'X-Y', 'X-Y', 'X', 'Y', 'X', 'Y'], int((5 + speed_increase) * scale_x)),
                 Enemies([int(1480 * scale_x), int(150 * scale_x)], int(40 * scale_x), [int(1050 * scale_x), int(1350 * scale_x), int(1050 * scale_x), int(1480 * scale_x)], [int(360 * scale_x), int(480 * scale_x), int(150 * scale_x)], ['Y', 'X', 'X', 'Y', 'X', 'X', 'Y'], int((5 + speed_increase) * scale_x)),
                 ]
    elif random_map == 1:
        array = [Enemies([int(1760 * scale_x), int(1000 * scale_x)], int(40 * scale_x), [int(1460 * scale_x), int(1200 * scale_x), int(1500 * scale_x), int(1200 * scale_x), int(1460 * scale_x), int(1760 * scale_x)], [int(700 * scale_x), int(1000 * scale_x), int(700 * scale_x), int(1000 * scale_x)], ['X-Y', 'X', 'X-Y'], int((5 + speed_increase) * scale_x)),
                 Enemies([int(160 * scale_x), int(1000 * scale_x)], int(40 * scale_x), [int(460 * scale_x), int(720 * scale_x), int(420 * scale_x), int(720 * scale_x), int(460 * scale_x), int(160 * scale_x)], [int(700 * scale_x), int(1000 * scale_x), int(700 * scale_x), int(1000 * scale_x)], ['X-Y', 'X', 'X-Y'], int((5 + speed_increase) * scale_x)),
                 Enemies([int(760 * scale_x), int(400 * scale_x)], int(40 * scale_x), [int(1160 * scale_x), int(760 * scale_x)], [int(710 * scale_x), int(400 * scale_x)], ['X', 'Y'], int((5 + speed_increase) * scale_x)),
                 Enemies([int(1160 * scale_x), int(710 * scale_x)], int(40 * scale_x), [int(760 * scale_x), int(1160 * scale_x)], [int(400 * scale_x), int(710 * scale_x)], ['X', 'Y'], int((5 + speed_increase) * scale_x)),
                 Enemies([int(80 * scale_x), int(90 * scale_x)], int(40 * scale_x), [int(480 * scale_x), int(780 * scale_x), int(480 * scale_x), int(80 * scale_x)], [int(320 * scale_x), int(120 * scale_x), int(280 * scale_x), int(120 * scale_x), int(320 * scale_x), int(90 * scale_x)], ['Y', 'X', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'X', 'Y'], int((5 + speed_increase) * scale_x)),
                 Enemies([int(1840 * scale_x), int(90 * scale_x)], int(40 * scale_x), [int(1440 * scale_x), int(1140 * scale_x), int(1440 * scale_x), int(1840 * scale_x)], [int(320 * scale_x), int(120 * scale_x), int(280 * scale_x), int(120 * scale_x), int(320 * scale_x), int(90 * scale_x)], ['Y', 'X', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'X', 'Y'], int((5 + speed_increase) * scale_x)),
                 ]
    elif random_map == 2:
        array = []
        for i in range(20):
            array.append(Enemy(random.randint(int(80 * scale_x), int(1840 * scale_x)), random.randint(int(80 * scale_x), int(940 * scale_x)), int(40 * scale_x), int((5 + speed_increase) * scale_x)))
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
    for i in range(27):
        for j in range(48):
            if maps[random_map][i][j] == '1':
                array.append(BordersCreator([j * global_width_height + global_width_height // 2,
                                             i * global_width_height + global_width_height // 2],
                                            global_width_height, global_width_height))

    return array


if random_map == 0:
    main_character = CharacterCreator([int(1670 * scale_x), int(200 * scale_x)], int(24 * scale_x), int(54 * scale_x))
elif random_map == 1:
    main_character = CharacterCreator([int(960 * scale_x), int(100 * scale_x)], int(24 * scale_x), int(54 * scale_x))
elif random_map == 2:
    main_character = CharacterCreator([int(960 * scale_x), int(540 * scale_x)], int(24 * scale_x), int(54 * scale_x))
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


def background_draw():
    array = maps[random_map]
    for i1 in range(27):
        for j1 in range(48):
            if array[i1][j1] == '0':
                screen.blit(background_photo, (j1 * global_width_height, i1 * global_width_height))
            if array[i1][j1] == '1':
                screen.blit(walls_photo, (j1 * global_width_height, i1 * global_width_height))
                # pygame.draw.rect(screen, (255, 192, 203), [j1 * global_width_height // 2 + 1, i1 *
                #                                            global_width_height // 2 + 1, global_width_height // 2 - 1,
                #                                            global_width_height // 2 - 1], 0)


def finish(x, y):
    if len(enemies_array) == 0:
        if random_map == 0:
            if int(40 * scale_x) <= x <= int(120 * scale_x) and int(1040 * scale_x) <= y <= int(1200 * scale_x):
                return True
        if random_map == 1:
            if int(800 * scale_x) <= x <= int(1200 * scale_x) and int(1040 * scale_x) <= y <= int(1200 * scale_x):
                return True
        if random_map == 2:
            if int(800 * scale_x) <= x <= int(1200 * scale_x) and int(-200 * scale_x) <= y <= int(40 * scale_x):
                return True


while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            enemies_killed = []
            for index in range(len(enemies_array)):
                enemy_x = enemies_array[index].x
                enemy_y = enemies_array[index].y
                enemy_pos = (enemies_array[index].x - enemies_array[index].width // 2,
                             enemies_array[index].y - enemies_array[index].width // 2,
                             enemies_array[index].x + enemies_array[index].width // 2,
                             enemies_array[index].y + enemies_array[index].width // 2)
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

    # screen.fill([43, 237, 237])
    background_draw()
    main_character.draw_object()
    enemies_draw()
    if main_character.dirX != 0:
        main_character.dirX_last = main_character.dirX
    if finish(main_character.position_x, main_character.position_y):
        random_map = random.randint(0, len(maps) - 1)
        passed_levels_count += 1
        borders = generate_borders()
        enemies_array = generate_enemies(passed_levels_count * 2)
        if random_map == 0:
            main_character.position_x = int(1670 * scale_x)
            main_character.position_y = int(200 * scale_x)
        if random_map == 1:
            main_character.position_x = int(960 * scale_x)
            main_character.position_y = int(100 * scale_x)
        if random_map == 2:
            main_character.position_x = int(960 * scale_x)
            main_character.position_y = int(540 * scale_x)

    pygame.display.update()