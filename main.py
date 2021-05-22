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
                    if event.key = UP:

                elif event.type == QUIT:
                    running = False

    # Funcion para mostrar el bloque en la pantalla surface

    def draw_block():
        surface.fill((255, 255, 254))
        block = pygame.image.load("resources/block.jpg").convert()
        surface.blit(block, (100, 100))

    # Se termina el event loop para cerrar la ventana sin tener un timeer
   
    
    pygame.init()
    surface = pygame.display.set_mode((600, 600))
    draw_block()
    pygame.display.flip()
    event_loop()
    # Para mover nuestro cuadrado necesitamos moverlo en nuestra funcion event lopp 

