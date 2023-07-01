import pygame

pygame.init()

from brick_mania import Game
from brick_mania.config import *

game = Game()

while True:
    game.handle_events()
    game.paddle.move()
    game.ball.move()
    game.handle_collisions()
    game.draw()
    game.clock.tick(FPS)
