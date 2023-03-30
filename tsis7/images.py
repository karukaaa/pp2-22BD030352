import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((600, 600))
done = False
clock = pygame.time.Clock()


def minutes_angle():
    minute = datetime.datetime.now().minute
    angle_time = -(minute*6-96)
    return angle_time


def seconds_angle():
    seconds = datetime.datetime.now().second
    angle_time = -(seconds*6-96)
    return angle_time


def load_image(path):
    image = pygame.image.load(path)
    scaled_image = pygame.transform.scale(image, (image.get_width() // 2, image.get_height() // 2))
    return scaled_image


def rot_anchor(image, angle, anchor):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(**anchor)

    return rotated_image, new_rect

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    screen.blit(load_image('main-clock.png'), (100, 100))  # clock

    angle = minutes_angle()
    anchor = (0, load_image('right-hand.png').get_height() // 2)  # minutes
    rotated_image, rect = rot_anchor(load_image('right-hand.png'), angle, {'center': (300, 300)})
    screen.blit(rotated_image, rect)

    angle = seconds_angle()
    anchor = (0, load_image('left-hand.png').get_height() // 2)  # seconds
    rotated_image, rect = rot_anchor(load_image('left-hand.png'), angle, {'center': (300, 300)})
    screen.blit(rotated_image, rect)

    pygame.display.flip()
    clock.tick(60)
