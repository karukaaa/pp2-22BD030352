import random
import pygame
import psycopg2

pygame.init()
WIDTH, HEIGHT = 700, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
score_font = pygame.font.SysFont("Verdana", 30)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]
        self.score = 0
        self.level = 1
        self.speed = 7

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y

        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x >= WIDTH // BLOCK_SIZE:
            quit()
        elif self.body[0].x < 0:
            quit()
        elif self.body[0].y < 0:
            quit()
        elif self.body[0].y >= HEIGHT // BLOCK_SIZE:
            quit()

        for block in self.body[1:]:
            if self.body[0].x == block.x and self.body[0].y == block.y:
                quit()

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)
        self.color = GREEN

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            self.color,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


def main():
    name = input("Enter user name: ")

    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="Shyngys1",
        database="postgres"
    )
    cur = conn.cursor()
    # cur.execute("CREATE TABLE Snake_users (id SERIAL PRIMARY KEY, name VARCHAR(50))")
    # cur.execute("CREATE TABLE Snake_scores (userId INT PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), score INT)")

    running = True
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, -1
    color_change_food = GREEN

    while running:
        SCREEN.fill(BLACK)
        food.color = color_change_food

        snake.level = snake.score // 5 + 1
        snake.speed = snake.level * 1.3 + 3

        score_txt = score_font.render(f"score: {snake.score}", True, WHITE)
        level_txt = score_font.render(f"level: {snake.level}", True, WHITE)
        SCREEN.blit(score_txt, (WIDTH/1.3, 0))
        SCREEN.blit(level_txt, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_RIGHT:
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0

        snake.move(dx, dy)

        if snake.check_collision(food):
            number = random.randint(0, 1)

            if food.color == GREEN:
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
                snake.score += 1

            elif food.color == BLUE:
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
                snake.score += 2

            if number == 0:
                color_change_food = GREEN
            elif number == 1:
                color_change_food = BLUE

            pos_x = random.randint(1, WIDTH // BLOCK_SIZE - 2)
            pos_y = random.randint(1, HEIGHT // BLOCK_SIZE - 2)

            for block in snake.body[0:]:
                if pos_x == block.x and pos_y == block.y:
                    pos_x = random.randint(1, WIDTH // BLOCK_SIZE - 2)
                    pos_y = random.randint(1, HEIGHT // BLOCK_SIZE - 2)

            food.location.x = pos_x
            food.location.y = pos_y

        snake.draw()
        food.draw()
        draw_grid()
        pygame.display.flip()
        clock.tick(snake.speed)


if __name__ == '__main__':
    main()