# the Ball bounces in the window. By this we're testing OOP.

import sys
import random
import pygame
from pygame.locals import *
from classes.Ball import *

# определяем константы
COLOR = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# инициализируем переменные окна
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# инициализируем переменные
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# бесконечные цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()
            sys.exit()

    # выполняем действия в рамках фрейма
    oBall.update()

    # очищаем экран
    window.fill(COLOR)

    # рисуем мяч
    oBall.draw()

    # обновляем окно
    pygame.display.update()

    # делаем паузу
    clock.tick(FRAMES_PER_SECOND)
