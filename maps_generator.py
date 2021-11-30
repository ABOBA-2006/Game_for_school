import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([960, 540])
array = []
running = True
global_width_height = 40

for i in range(1080 // global_width_height):
    array.append([])
    for j in range(1920 // global_width_height):
        array[i].append('0')


def draw_stick(x, y, width, height):
    pygame.draw.rect(screen, (0, 0, 0), [x, y, width, height], 0)


def draw_array():
    for i1 in range(1080 // global_width_height):
        draw_stick(0, i1 * global_width_height // 2, 1920, 1)
    for j1 in range(1920 // global_width_height):
        draw_stick(j1 * global_width_height // 2, 0, 1, 1080)


def drawing_way():
    for i1 in range(1080 // global_width_height):
        for j1 in range(1920 // global_width_height):
            if array[i1][j1] == '1':
                pygame.draw.rect(screen, (255, 192, 203), [j1 * global_width_height // 2 + 1, i1 *
                                                           global_width_height // 2 + 1, global_width_height // 2 - 1,
                                                           global_width_height // 2 - 1], 0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(array)
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            i2 = event.pos[1] // (global_width_height // 2)
            j2 = event.pos[0] // (global_width_height // 2)
            array[i2][j2] = '1'
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            i2 = event.pos[1] // (global_width_height // 2)
            j2 = event.pos[0] // (global_width_height // 2)
            array[i2][j2] = '0'

    screen.fill([99, 99, 99])
    draw_array()
    drawing_way()

    pygame.display.update()
