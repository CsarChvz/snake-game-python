import pygame
from pygame.locals import *


if __name__ == '__main__':

   #Event Loop es importante para todos los programas de UI
    def event_loop():
        """ EVENT LOOP """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False

    # Funcion para mostrar el bloque en la pantalla surface

    def draw_block(block_y, block_x):
        surface.fill((255, 255, 254))
        block_x = 100
        block_y = 100
        block = pygame.image.load("resources/block.jpg").convert()
        surface.blit(block, (block_x, block_y))

    # Se termina el event loop para cerrar la ventana sin tener un timeer
    pygame.init()
    surface = pygame.display.set_mode((600, 600))
    draw_block()
    pygame.display.flip()
    event_loop()
    # Para mover nuestro cuadrado necesitamos moverlo en nuestra funcion event lopp 

