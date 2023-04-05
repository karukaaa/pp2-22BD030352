import random
import time

import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
SCORE = 0
clock = pygame.time.Clock()
background = pygame.image.load('AnimatedStreet.png')
score_font = pygame.font.SysFont("Verdana", 30)

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 1
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.move_ip(self.speed, 0)


coin_img = pygame.image.load('coin.png')
scaled_coin = pygame.transform.scale(coin_img, (30,30))


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        self.coins = 0
        super().__init__()
        self.speed = 5
        self.image = scaled_coin
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH-self.rect.width),
            0,
        )


    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            self.rect.center = (
                random.randint(self.rect.width, WIDTH-self.rect.width),
                0,
            )



def play_music(name):
    pygame.mixer.music.load(name)
    pygame.mixer.music.play(-1)


def main():
    running = True
    player = Player()
    enemy = Enemy()
    coin_obj = Coin()
    enemies = pygame.sprite.Group()
    enemies.add(enemy)
    coins = pygame.sprite.Group()
    coins.add(coin_obj)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(enemy)
    all_sprites.add(coin_obj)

    while running:

        SCREEN.blit(background, (0, 0))
        score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 0))
        game_over = score_font.render("Game Over :(", True, (255, 255, 255))
        coin_score_txt = score_font.render(f"Coins: {coin_obj.coins}", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))
        SCREEN.blit(coin_score_txt, (WIDTH/1.5, 0))

        for entity in all_sprites:
            SCREEN.blit(entity.image, entity.rect)
            entity.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pygame.sprite.spritecollideany(player, enemies):
            play_music('crash.wav')
            time.sleep(0.5)

            SCREEN.fill(RED)
            SCREEN.blit(game_over, (WIDTH/4, HEIGHT / 2))
            pygame.display.update()

            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            running = False

        if pygame.sprite.spritecollideany(player, coins):
            coin_obj.rect.center = (
                random.randint(coin_obj.rect.width, WIDTH - coin_obj.rect.width),
                0,
            )
            coin_obj.coins += 1

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()