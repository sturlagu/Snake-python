import pygame


class Snake:
    WIDTH = 25
    HEIGHT = 25
    SIZE = 25
    VELOCITY = 25

    def __init__(self, pos, direction, color):
        self.x = pos[0]
        self.y = pos[1]
        self.direction = direction
        self.color = color

    def reset(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def clear(self, screen, bg):
        pygame.draw.rect(screen, bg, (self.x, self.y, self.WIDTH, self.HEIGHT))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.WIDTH, self.HEIGHT))

    def move(self):
        if self.direction == "left":
            self.x = self.x - self.VELOCITY
        elif self.direction == "right":
            self.x = self.x + self.VELOCITY
        elif self.direction == "up":
            self.y = self.y - self.VELOCITY
        elif self.direction == "down":
            self.y = self.y + self.VELOCITY

    def keyboard_input(self, key):
        if key == pygame.K_LEFT and self.direction != "right":
            self.direction = "left"
        elif key == pygame.K_RIGHT and self.direction != "left":
            self.direction = "right"
        elif key == pygame.K_UP and self.direction != "down":
            self.direction = "up"
        elif key == pygame.K_DOWN and self.direction != "up":
            self.direction = "down"
