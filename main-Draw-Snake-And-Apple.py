import pygame
from pygame.locals import *
import time

SIZE = 40
class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen 
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'
    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):

            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()
 
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'

    def walk(self):
        if self.direction == 'left':
            self.x -= 10
        if self.direction == 'right':
            self.x += 10
        if self.direction == 'up':
            self.y -= 10
        if self.direction == 'down':
            self.y += 10

        self.draw()

class Game:

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((110, 110, 5))
        
        #Creamos una serpiente porque adentro del juego hay una y tiene que interactuar con las funciones del juego 
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        #Event Loop

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            time.sleep(0.2)

if __name__ == '__main__':
    game = Game()
    game.run()
    

