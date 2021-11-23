import sys
import random
import pygame

pygame.init()
screen = pygame.display.set_mode([1040, 680])
clock = pygame.time.Clock()
array_of_borders = []
array_trail = []
running = True
teleport_flag = False
main_character_photo = pygame.image.load("main_character.png")


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
        size = map_trailing(player_trail_live - idx, player_trail_live, 0, player_size*0.9, 0)
        if size < 0:
            continue
        # от зеленого до белого
        color_v = int(map_trailing(idx, 0, player_trail_live, 0, 200))
        if color_v < 0:
            color_v = 0
        # прозрачность
        color_alpha = int(map_trailing(idx, 0, player_trail_live, 100, 0))
        color = (color_v, 255, color_v, color_alpha)

        center = (trail[0]-size/2, trail[1]-size/2)
        radius = size
        # я скопировал и в душе не ебу как оно меняет прозрачность цвета
        target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, (radius, radius, radius, radius))
        screen.blit(shape_surf, target_rect)


class CharacterCreator:
    def __init__(self, start_position, width):
        self.position_x = start_position[0]
        self.position_y = start_position[1]
        self.width = width
        self.dirX = 0  # направление по x
        self.dirY = 0  # направление по y
        self.speed = 8
        self.forset_x = 0
        self.forset_y = 0
        self.tp_check_x = True
        self.tp_check_y = True

    def draw_object(self):
        draw_player_trail(self.width)
        square = pygame.Rect(self.position_x - self.width // 2, self.position_y - self.width // 2,
                             self.width, self.width)
        pygame.draw.rect(screen, (28, 217, 34), square, 0)
        # screen.blit(main_character_photo, (self.position_x - self.width // 2, self.position_y - self.width // 2))

    def move(self):
        is_colliding_x = False
        is_colliding_y = False
        self.tp_check_y = True
        self.tp_check_x = True
        for i in range(0, len(borders)):
            border = borders[i]
            border_pos = border.pos
            player_pos = (self.position_x - self.width // 2, self.position_y - self.width // 2, self.position_x +
                          self.width // 2, self.position_y + self.width // 2)

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

            # проверяем если в будущем игрок врежитсся в стенку по x и y отдельно
            if is_colliding_x is False and check_collision(border_pos, new_player_pos_x) is True:
                is_colliding_x = True
                if self.dirX == 1:
                    self.forset_x = abs(player_pos[2]-border.pos[0])-1
                if self.dirX == -1:
                    self.forset_x = abs(player_pos[0] - border.pos[2]) - 1
            if is_colliding_y is False and check_collision(border_pos, new_player_pos_y) is True:
                is_colliding_y = True
                if self.dirY == 1:
                    self.forset_y = abs(player_pos[3]-border.pos[1]) - 1
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


main_character = CharacterCreator([973, 210], 40)
borders = generate_borders()


def border_draw():
    for border in borders:
        border.draw_object()


def finish(x, y):
    if 20 <= x <= 100 and 660 <= y <= 900:
        return True


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
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
        if main_character.tp_check_x is True and main_character.tp_check_y is True:
            main_character.position_x += main_character.dirX * main_character.speed * 7
            main_character.position_y += main_character.dirY * main_character.speed * 7
    if teleport_flag is True and keys[pygame.K_SPACE] is False:
        teleport_flag = False

    main_character.move()

    screen.fill([99, 99, 99])
    main_character.draw_object()
    border_draw()
    if finish(main_character.position_x, main_character.position_y):
        running = False

    pygame.display.update()
