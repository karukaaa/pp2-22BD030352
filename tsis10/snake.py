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

input_box = pygame.Rect(200, 300, 300, 60)

conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="Shyngys1",
        database="postgres"
    )
cur = conn.cursor()


# cur.execute("CREATE TABLE Snake_users (id SERIAL PRIMARY KEY, username VARCHAR(50) NOT NULL UNIQUE)")
# cur.execute("CREATE TABLE Snake_scores (user_id INT NOT NULL, score INT DEFAULT 0, FOREIGN KEY (user_id) REFERENCES Snake_users(id) ON DELETE CASCADE)")
# conn.commit()

# cur.execute("SELECT * FROM Snake_users")
# for x in cur:
#     print(x)
# cur.execute("SELECT * FROM Snake_scores")
# for x in cur:
#     print(x)


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


def name_entering():
    username = ''

    running = True

    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    cur.execute("SELECT id FROM Snake_users WHERE username = %s", (username,))
                    id_value = cur.fetchone()
                    if not id_value:
                        cur.execute("INSERT INTO Snake_users (username) VALUES (%s)", (username,))
                        cur.execute("SELECT id FROM Snake_users WHERE username = %s", (username,))
                        id_value = cur.fetchone()

                        cur.execute("INSERT INTO Snake_scores (user_id) VALUES (%s)", id_value)
                        conn.commit()

                    cur.execute("SELECT score FROM Snake_scores WHERE user_id = %s", (id_value,))
                    score_value = cur.fetchone()[0]
                    cur.execute("SELECT id FROM Snake_users WHERE username = %s", (username,))
                    id_value = cur.fetchone()[0]

                    main(score_value, id_value)
                    running = False

                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

        text_surface = score_font.render(username, True, RED)
        pygame.draw.rect(SCREEN, RED, input_box, 2)
        SCREEN.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        pygame.display.flip()
        clock.tick(60)


def main(score_value, id_value):

    paused = False
    flag = False
    running = True
    snake = Snake()

    snake.speed = 0

    snake.score = score_value

    food = Food(5, 5)
    dx, dy = 0, -1
    color_change_food = GREEN

    while running:
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
                if event.key == pygame.K_ESCAPE:
                    paused = not paused

        if not paused:
            if not flag:
                for x in range(snake.score):
                    snake.body.append(
                        Point(snake.body[-1].x, snake.body[-1].y)
                    )
                flag = True

            SCREEN.fill(BLACK)
            food.color = color_change_food

            snake.level = snake.score // 5 + 1
            snake.speed = snake.level * 1.3 + 3

            score_txt = score_font.render(f"score: {snake.score}", True, WHITE)
            level_txt = score_font.render(f"level: {snake.level}", True, WHITE)
            SCREEN.blit(score_txt, (WIDTH / 1.3, 0))
            SCREEN.blit(level_txt, (0, 0))

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

        else:
            cur.execute("UPDATE Snake_scores SET score = %s WHERE user_id = %s", (snake.score, id_value))
            conn.commit()


name_entering()
