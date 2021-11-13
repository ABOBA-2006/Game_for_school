import pygame
pygame.init()
screen = pygame.display.set_mode([1280, 800])
screen.fill([0, 0, 0])
pygame.display.set_caption("My Game")


class Character:
    def __init__(self, xposition, yposition, speed):
        self.x = xposition
        self.y = yposition
        self.speed = speed

    def drawCharacter(self):
        pygame.draw.circle(screen, [255, 0, 0], [self.x, self.y], 30, 0)

    def moveCharacter(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed


player = Character(100, 100, 2)
player.drawCharacter()
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.moveCharacter()
    screen.fill([0, 0, 0])
    player.drawCharacter()
    pygame.display.flip()

pygame.quit()