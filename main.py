import pygame
from pygame.locals import *


if __name__ == '__main__':
    pygame.init()

    surface = pygame.display.set_mode((600, 600))
    surface.fill((109, 248, 24))
    pygame.display.flip()
    #Event Loop es importante para todos los programas de UI
    
    """ EVENT LOOP """
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN or event.type == QUIT:
                running = False
