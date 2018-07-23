import pygame


class Sprite:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)

        self.rect = self.image.get_rect()

    def render(self, window):
        window.blit(self.image, (self.x, self.y))


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FRAMES = 30

car = Sprite(200, 200, "car.png")
car2 = Sprite(0, 0, "car.png")

iterator = True
while iterator:
    screen.fill((255, 255, 255))
    car.render(screen)
    car2.render(screen)
    pygame.display.update()
    clock.tick(FRAMES)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        car.y -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            iterator = False
