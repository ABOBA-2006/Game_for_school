import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([1040, 680])
clock = pygame.time.Clock()
array_of_borders = []


def create_background():
    square = pygame.Rect(0, 0, 1040, 680)
    pygame.draw.rect(screen, (99, 99, 99), square, 0)


class CharacterCreator:
    def __init__(self, start_position, width):
        self.position_x = start_position[0]
        self.position_y = start_position[1]
        self.position_x_last = self.position_x
        self.position_y_last = self.position_y
        self.width = width
        self.check_left = False
        self.check_right = False
        self.check_top = False
        self.check_bottom = False

    def draw_object(self):
        square = pygame.Rect(self.position_x - self.width // 2, self.position_y - self.width // 2,
                             self.width, self.width)
        pygame.draw.rect(screen, (28, 217, 34), square, 0)

    def move(self, direction):
        for i in range(0, len(array_of_borders)):
            if self.check_left is False:
                if array_of_borders[i][0] <= self.position_x - self.width // 2 <= array_of_borders[i][2]:     # left
                    if array_of_borders[i][1] <= self.position_y <= array_of_borders[i][3]:
                        self.check_left = True
                        return
            if self.check_right is False:
                if array_of_borders[i][0] <= self.position_x + self.width // 2 <= array_of_borders[i][2]:     # right
                    if array_of_borders[i][1] <= self.position_y <= array_of_borders[i][3]:
                        self.check_right = True
                        return
            if self.check_bottom is False:
                if array_of_borders[i][0] <= self.position_x <= array_of_borders[i][2]:
                    if array_of_borders[i][1] <= self.position_y + self.width // 2 <= array_of_borders[i][3]:   # bottom
                        self.check_bottom = True
                        return
            if self.check_top is False:
                if array_of_borders[i][0] <= self.position_x <= array_of_borders[i][2]:
                    if array_of_borders[i][1] <= self.position_y - self.width // 2 <= array_of_borders[i][3]:    # top
                        self.check_top = True
                        return
        if direction == 'top' and self.check_top is False:
            self.position_y -= 5
            self.check_bottom = False
            self.check_left = False
            self.check_right = False
        if direction == 'bottom' and self.check_bottom is False:
            self.position_y += 5
            self.check_top = False
            self.check_left = False
            self.check_right = False
        if direction == 'left' and self.check_left is False:
            self.position_x -= 5
            self.check_bottom = False
            self.check_top = False
            self.check_right = False
        if direction == 'right' and self.check_right is False:
            self.position_x += 5
            self.check_bottom = False
            self.check_left = False
            self.check_top = False


class BordersCreator:
    def __init__(self, start_position, width, height):
        self.position_x = start_position[0]
        self.position_y = start_position[1]
        self.width = width
        self.height = height
        array_of_borders.append([self.position_x - self.width // 2, self.position_y - self.height // 2,
                                 self.position_x + self.width // 2, self.position_y + self.height // 2])

    def draw_object(self):
        rectangle = pygame.Rect(self.position_x - self.width // 2, self.position_y - self.height // 2,
                                self.width, self.height)
        pygame.draw.rect(screen, (59, 59, 59), rectangle, 0)


main_character = CharacterCreator([520, 340], 50)

first_border = BordersCreator([25, 340], 50, 680)
second_border = BordersCreator([1015, 340], 50, 680)
third_border = BordersCreator([520, 25], 1040, 50)
forth_border = BordersCreator([520, 655], 1040, 50)

while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            main_character.move('top')
        elif keys[pygame.K_s]:
            main_character.move('bottom')
        elif keys[pygame.K_a]:
            main_character.move('left')
        elif keys[pygame.K_d]:
            main_character.move('right')

    create_background()
    main_character.draw_object()
    first_border.draw_object()
    second_border.draw_object()
    third_border.draw_object()
    forth_border.draw_object()
    pygame.display.flip()
