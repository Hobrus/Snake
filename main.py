import pygame
import random

class Snake:
    def __init__(self, x, y, color, speed, size):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = size
        self.dir_x = 0 # -1 0 1
        self.dir_y = 0

    def move(self):
        if self.dir_x == 1:
            self.x += self.speed
        if self.dir_x == -1:
            self.x -= self.speed
        if self.dir_y == 1:
            self.y += speed
        if self.dir_y == -1:
            self.y -= speed

    def move_right(self):
        self.dir_x = 1
        self.dir_y = 0

    def move_left(self):
        self.dir_x = -1
        self.dir_y = 0

    def move_down(self):
        self.dir_x = 0
        self.dir_y = 1

    def move_up(self):
        self.dir_x = 0
        self.dir_y = -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def check_walls(self):
        if self.x <= 0:
            self.move_right()
        if self.y <= 0:
            self.move_down()
        if self.y >= HEIGHT:
            self.move_up()
        if self.x >= WIDTH:
            self.move_left()

    def check_food(self, food_x, food_y):
        if self.x == food_x and self.y == food_y:
            return True
        return False

WIDTH = 720
HEIGHT = 480

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Lime = (0,255,0)
Blue= (0,0,255)

sr = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('SkySmart Game')
image = pygame.image.load('skyicon.PNG')
pygame.display.set_icon(image)

fps = 20 # frames per second
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

snake = Snake(3*speed, 3*speed, Red, speed, size)
while True:
    sr.fill(Black)

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
    snake.check_walls()
    is_eat = snake.check_food(food_x, food_y)
    snake.draw(sr)
    if is_eat:
        food_x = random.randint(0, WIDTH) * speed % WIDTH
        food_y = random.randint(0, HEIGHT) * speed % HEIGHT

    pygame.draw.rect(sr, Blue, (food_x, food_y, size, size))
    pygame.display.update()
    clock.tick(fps)