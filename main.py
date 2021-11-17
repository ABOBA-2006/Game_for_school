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
        self.speed = 4

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
            self.position_y -= self.speed
            self.check_bottom = False
            self.check_left = False
            self.check_right = False
        if self.direction == 'bottom' and self.check_bottom is False:
            self.position_y += self.speed
            self.check_top = False
            self.check_left = False
            self.check_right = False
        if self.direction == 'left' and self.check_left is False:
            self.position_x -= self.speed
            self.check_bottom = False
            self.check_top = False
            self.check_right = False
        if self.direction == 'right' and self.check_right is False:
            self.position_x += self.speed
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


def generate_borders():
    array = [BordersCreator([10, 340], 20, 680),
             BordersCreator([1030, 340], 20, 680),
             BordersCreator([520, 10], 1040, 20),
             BordersCreator([580, 670], 920, 20),
             BordersCreator([120, 150], 20, 300),
             BordersCreator([120, 550], 20, 260),
             BordersCreator([380, 150], 520, 20),
             BordersCreator([220, 430], 200, 20),
             BordersCreator([320, 482.5], 20, 125),
             BordersCreator([510, 555], 400, 20),
             BordersCreator([700, 420], 20, 260),
             BordersCreator([510, 300], 400, 20),
             BordersCreator([510, 365], 20, 130),
             BordersCreator([915, 150], 250, 20),
             BordersCreator([915, 240], 20, 200),
             BordersCreator([915, 450], 250, 20),
             BordersCreator([915, 555], 250, 20)
             ]
    return array


borders = generate_borders()


def border_draw():
    for border in borders:
        border.draw_object()


def finish(x, y):
    if 20 <= x <= 100 and 660 <= y <= 900:
        return True


while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if not (keys[pygame.K_w] and keys[pygame.K_s]):
        if keys[pygame.K_w]:
            main_character.change_direction('top')
            main_character.move()
        elif keys[pygame.K_s]:
            main_character.change_direction('bottom')
            main_character.move()

    if not (keys[pygame.K_a] and keys[pygame.K_d]):
        if keys[pygame.K_a]:
            main_character.change_direction('left')
            main_character.move()
        elif keys[pygame.K_d]:
            main_character.change_direction('right')
            main_character.move()

    screen.fill([99, 99, 99])
    main_character.draw_object()
    border_draw()
    if finish(main_character.position_x, main_character.position_y):
        running = False
    pygame.display.update()

