# the Ball bounces in the window. By this we're testing OOP.

import sys
import pygame
from pygame.locals import *
from classes.Ball import *

# определяем константы
COLOR = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3

# инициализируем переменные окна
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# создаём список состоящий из объектов
ballList = []
for i in range(N_BALLS):
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)

# бесконечные цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()
            sys.exit()

    # выполняем действия в рамках фрейма

    # для каждого мяча определяем координаты и движение
    for item in ballList:
        item.update()

    # очищаем экран
    window.fill(COLOR)

    # рисуем мячи из списка 
    for item in ballList:
        item.draw()

    # обновляем окно
    pygame.display.update()

    # делаем паузу
    clock.tick(FRAMES_PER_SECOND)
