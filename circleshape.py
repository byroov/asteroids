import pygame
import constants
from logger import log_event


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH)
        

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            rotate(-dt)
        if keys[pygame.K_d]:
            rotate(dt)

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        r1_r2 = self.radius + other.radius 
        if distance <= r1_r2:
            return True
        return False