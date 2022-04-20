import pygame
import random
import time

pygame.init()

class Snake:
    def __init__(self, x, y, color, speed, size):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = size
        self.dir_x = 0 # -1 0 1
        self.dir_y = 0
        self.count = 1
        self.heads = [] # 0 1
        self.add_head()

    def add_head(self):
        self.heads.append(Snake_head(self.x, self.y, self.color, self.speed, self.size))

    def remove_head(self):
        if len(self.heads) > self.count:
            self.heads.pop(0)

    def draw(self, screen):
        for head in self.heads:
            head.draw(screen)

    def move(self):
        if self.dir_x == 1:
            self.x += self.speed
        if self.dir_x == -1:
            self.x -= self.speed
        if self.dir_y == 1:
            self.y += speed
        if self.dir_y == -1:
            self.y -= speed
        self.add_head()
        self.remove_head()

    def move_right(self):
        if self.count == 1:
            self.dir_x = 1
            self.dir_y = 0
        else:
            if self.dir_y:
                self.dir_x = 1
                self.dir_y = 0

    def move_left(self):
        if self.count == 1:
            self.dir_x = -1
            self.dir_y = 0
        else:
            if self.dir_y:
                self.dir_x = -1
                self.dir_y = 0

    def move_down(self):
        if self.count == 1:
            self.dir_x = 0
            self.dir_y = 1
        else:
            if self.dir_x:
                self.dir_x = 0
                self.dir_y = 1

    def move_up(self):
        if self.count == 1:
            self.dir_x = 0
            self.dir_y = -1
        else:
            if self.dir_x:
                self.dir_x = 0
                self.dir_y = -1

    def check_walls(self):
        if self.x <= 0 or self.y <= 0 or self.y >= HEIGHT - self.size or self.x >= WIDTH - self.size:
            return False
        return True

    def check_snake(self): # 0 0 1 len 3
        for i in range(len(self.heads)):
            if i != len(self.heads) - 1:
                if self.x == self.heads[i].x and self.y == self.heads[i].y:
                    return False
        return True

    def check_food(self, food_x, food_y):
        if self.x == food_x and self.y == food_y:
            self.count += 1
            return True
        return False

class Snake_head:
    def __init__(self, x, y, color, speed, size):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = size
        self.dir_x = 0 # -1 0 1
        self.dir_y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

WIDTH = 720
HEIGHT = 480

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue= (0,0,255)

sr = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('SkySmart Game')
image = pygame.image.load('skyicon.PNG')
pygame.display.set_icon(image)

fps = 10 # frames per second
clock = pygame.time.Clock()

is_key_right = False
is_key_left = False
is_key_down = False
is_key_top = False

speed = 15 # Скорость должна быть равной размеру
size = 15

width_hero = 15
height_hero = 15

food_x = 150
food_y = 150

is_eat = True

f1 = pygame.font.Font(None, 36)
game_over_text = f1.render("Game over", True, Red)

snake = Snake(3 * speed, 3 * speed, Red, speed, size)

is_game_active = True

while is_game_active:
    sr.fill(Black)

    f2 = pygame.font.Font(None, 36)
    score_text = f2.render(str(snake.count), True, Green)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                is_key_right = True
            if event.key == pygame.K_LEFT:
                is_key_left = True
            if event.key == pygame.K_UP:
                is_key_top = True
            if event.key == pygame.K_DOWN:
                is_key_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                is_key_right = False
            if event.key == pygame.K_LEFT:
                is_key_left = False
            if event.key == pygame.K_UP:
                is_key_top = False
            if event.key == pygame.K_DOWN:
                is_key_down = False

    if is_key_right:
        snake.move_right()
    if is_key_left:
        snake.move_left()
    if is_key_top:
        snake.move_up()
    if is_key_down:
        snake.move_down()

    snake.move()
    is_game_active1 = snake.check_walls()
    is_game_active2 = snake.check_snake()
    is_game_active = is_game_active1 and is_game_active2
    is_eat = snake.check_food(food_x, food_y)
    snake.draw(sr)
    if is_eat:
        is_repeat = True
        while is_repeat:
            is_repeat = False
            food_x = random.randint(0, WIDTH) * speed % WIDTH
            food_y = random.randint(0, HEIGHT) * speed % HEIGHT
            for snake_head in snake.heads:
                if food_x == snake_head.x and food_y == snake_head.y:
                    is_repeat = True

    sr.blit(score_text, (0, 0))
    pygame.draw.rect(sr, Blue, (food_x, food_y, size, size))
    pygame.display.update()
    clock.tick(fps)

sr.blit(game_over_text, (250, 200))
pygame.display.update()
time.sleep(10)