import pygame
from pygame.locals import *
import sys
from pathlib import Path

# 2.определяем константы
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 512
FRAMES_PER_SECOND = 30
BASE_PATH = Path(__file__).resolve().parent

# 3.инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4. загружаем элементы изображения
pathToBall = BASE_PATH + 'images/ball.png'

while True:
    # 7. проверяем наличие событий в окне и производим необходимые действия
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 9. очищаем окно
    window.fill(BLACK)

    # 11. обновляем окно
    pygame.display.update()

    # 12. делаем паузу
    clock.tick(FRAMES_PER_SECOND)
