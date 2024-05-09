import pygame
from pygame.locals import *
import random

class Ball:
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygame.image.load("images/ball.png")

        
        # прямоугольник состоит из x и y
        ballRect = self.image.get_rect()
        self.ballWindth = ballRect.width()
        self.ballHeight = ballRect.height()
        self.MaxWidth = self.windowWidth - self.ballWindth
        self.MaxWidth = self.windowHeight - self.ballHeight
        
