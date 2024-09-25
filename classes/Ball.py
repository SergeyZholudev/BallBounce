import pygame
from pathlib import Path
import random


# определяем константы
BASE_PATH = str(Path(__file__).resolve().parent)


class Ball:
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygame.image.load(BASE_PATH + '\\images\\ball.png')
        
        # прямоугольник состоит из x и y
        ballRect = self.image.get_rect()
        self.ballWidth = ballRect.width
        self.ballHeight = ballRect.height
        self.MaxWidth = self.windowWidth - self.ballWidth
        self.MaxHeight = self.windowHeight - self.ballHeight

        # выбираем произвольную начальную позицию
        self.x = random.randint(0, self.MaxWidth)
        self.y = random.randint(0, self.ballHeight)

        # определяем скорость движения объекта
        speedValues = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.speedX = random.choice(speedValues)
        self.speedY = random.choice(speedValues)

    def update(self):
        # проверяем столкновение объекта со стенками, если true
        # меняем направление
        if self.x < 0 or (self.x >= self.MaxWidth):
            self.speedX = -self.speedX

        if self.y < 0 or (self.y >= self.MaxHeight):
            self.speedY = -self.speedY

        # обновляем координату x и y
        self.x = self.x + self.speedX
        self.y = self.y + self.speedY

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
