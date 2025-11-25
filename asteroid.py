import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def update(self, dt):
       self.position += (self.velocity * dt)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        n = random.uniform(20, 50)
        v1 = self.velocity.rotate(n)
        v2 = self.velocity.rotate(-n)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_a1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_a1.velocity = v1 * 1.2
        new_a2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_a2.velocity = v2 * 1.2
