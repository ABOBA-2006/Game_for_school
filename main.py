import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([1040, 680])
clock = pygame.time.Clock()
array_of_borders = []
running = True


class CharacterCreator:
    def __init__(self, start_position, width):
        self.position_x = start_position[0]
        self.position_y = start_position[1]
        self.width = width
        self.check_left = False
        self.check_right = False
        self.check_top = False
        self.check_bottom = False
        self.direction = None

    def draw_object(self):
        square = pygame.Rect(self.position_x - self.width // 2, self.position_y - self.width // 2,
                             self.width, self.width)
        pygame.draw.rect(screen, (28, 217, 34), square, 0)

    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        for i in range(0, len(array_of_borders)):
            if array_of_borders[i][0] <= self.position_x - self.width // 2 <= array_of_borders[i][2]:     # left
                if array_of_borders[i][1] <= self.position_y <= array_of_borders[i][3]:
                    self.check_left = True
            if array_of_borders[i][0] <= self.position_x + self.width // 2 <= array_of_borders[i][2]:     # right
                if array_of_borders[i][1] <= self.position_y <= array_of_borders[i][3]:
                    self.check_right = True
            if array_of_borders[i][0] <= self.position_x <= array_of_borders[i][2]:
                if array_of_borders[i][1] <= self.position_y + self.width // 2 <= array_of_borders[i][3]:   # bottom
                    self.check_bottom = True
            if array_of_borders[i][0] <= self.position_x <= array_of_borders[i][2]:
                if array_of_borders[i][1] <= self.position_y - self.width // 2 <= array_of_borders[i][3]:    # top
                    self.check_top = True
        if self.direction == 'top' and self.check_top is False:
            self.position_y -= 5
            self.check_bottom = False
            self.check_left = False
            self.check_right = False
        if self.direction == 'bottom' and self.check_bottom is False:
            self.position_y += 5
            self.check_top = False
            self.check_left = False
            self.check_right = False
        if self.direction == 'left' and self.check_left is False:
            self.position_x -= 5
            self.check_bottom = False
            self.check_top = False
            self.check_right = False
        if self.direction == 'right' and self.check_right is False:
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


main_character = CharacterCreator([973, 210], 40)


def borders():
    first_border = BordersCreator([10, 340], 20, 680)
    second_border = BordersCreator([1030, 340], 20, 680)
    third_border = BordersCreator([520, 10], 1040, 20)
    forth_border = BordersCreator([580, 670], 920, 20)

    fifth_border = BordersCreator([120, 150], 20, 300)
    sixth_border = BordersCreator([120, 550], 20, 260)
    seventh_border = BordersCreator([380, 150], 520, 20)
    eights_border = BordersCreator([220, 430], 200, 20)
    ninth_border = BordersCreator([320, 482.5], 20, 125)
    tenth_border = BordersCreator([510, 555], 400, 20)
    eleventh_border = BordersCreator([700, 420], 20, 260)
    twelves_border = BordersCreator([510, 300], 400, 20)
    thirteenth_border = BordersCreator([510, 365], 20, 130)

    fourteenth_border = BordersCreator([915, 150], 250, 20)
    fifteenth_border = BordersCreator([915, 240], 20, 200)
    sixteenth_border = BordersCreator([915, 450], 250, 20)
    seventeenth_border = BordersCreator([915, 555], 250, 20)

    first_border.draw_object()
    second_border.draw_object()
    third_border.draw_object()
    forth_border.draw_object()
    fifth_border.draw_object()
    sixth_border.draw_object()
    seventh_border.draw_object()
    eights_border.draw_object()
    ninth_border.draw_object()
    tenth_border.draw_object()
    eleventh_border.draw_object()
    twelves_border.draw_object()
    thirteenth_border.draw_object()
    fourteenth_border.draw_object()
    fifteenth_border.draw_object()
    sixteenth_border.draw_object()
    sixteenth_border.draw_object()
    seventeenth_border.draw_object()


def finish(x, y):
    if 20 <= x <= 100 and 660 <= y <= 900:
        return True


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        main_character.change_direction('top')
        main_character.move()
    elif keys[pygame.K_s]:
        main_character.change_direction('bottom')
        main_character.move()
    elif keys[pygame.K_a]:
        main_character.change_direction('left')
        main_character.move()
    elif keys[pygame.K_d]:
        main_character.change_direction('right')
        main_character.move()

    screen.fill([99, 99, 99])
    main_character.draw_object()
    borders()
    if finish(main_character.position_x, main_character.position_y):
        running = False
    pygame.display.flip()
