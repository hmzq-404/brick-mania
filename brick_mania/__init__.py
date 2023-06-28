from .config import *
from .sprites import Paddle, Ball, Brick
import sys
import pygame


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.paddle = Paddle()

        pygame.display.set_caption("Brick Mania")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.paddle.surf, self.paddle.rect)
        pygame.display.flip()
