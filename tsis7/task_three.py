import pygame

pygame.init()
width = 400
height = 300
screen = pygame.display.set_mode((width, height))
done = False
x = y = 30
clock = pygame.time.Clock()


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 20
    if pressed[pygame.K_DOWN]:
        y += 20
    if pressed[pygame.K_LEFT]:
        x -= 20
    if pressed[pygame.K_RIGHT]:
        x += 20

    if x <= 25:
        x = 25
    elif x >= width-25:
        x = width-25
    if y <= 25:
        y = 25
    elif y >= height-25:
        y = height-25

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    clock.tick(30)
    pygame.display.flip()

