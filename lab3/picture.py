import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((300, 300))


pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

