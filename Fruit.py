import pygame
from random import randrange


class Fruit:
    WIDTH = 25
    HEIGHT = 25
    SIZE = 25
    COLOR = 255, 0, 0

    def __init__(self, width, height):
        self.x = randrange(0, width - self.WIDTH, self.WIDTH)
        self.y = randrange(0, height - self.HEIGHT, self.HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, self.COLOR, (self.x, self.y, self.WIDTH, self.HEIGHT))

    def move(self, width, height):
        self.x = randrange(0, width - self.SIZE, self.WIDTH)
        self.y = randrange(0, height - self.SIZE, self.HEIGHT)
