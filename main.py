import pygame
import constants
from logger import log_state
from player import Player
import circleshape


pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
SCREEN_WIDTH = constants.SCREEN_WIDTH
LINE_WIDTH = constants.LINE_WIDTH
PLAYER_RADIUS = constants.PLAYER_RADIUS

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

running = True
while running:
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(60) / 1000
    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

class Player(player.Player):
 def __init__(self, x, y):
     super().__init__(x, y, PLAYER_RADIUS)
     x = constants.SCREEN_WIDTH / 2
     y = constants.SCREEN_HEIGHT / 2





def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()