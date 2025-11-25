import pygame
import circleshape
import constants


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        pygame.draw.circle(screen, "white", self(x, y), self.radius, constants.LINE_WIDTH)
    def update(self, dt):
        self(x, y) += (self.velocity * dt)