import pygame
from pygame.locals import *
import random


class Ball:
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygame.image.load("images/ball.png")
        