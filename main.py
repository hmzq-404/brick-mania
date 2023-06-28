from brick_mania import Game
from brick_mania.config import *
import pygame

pygame.init()

game = Game()

while True:
    game.handle_events()
    game.paddle.move()
    game.draw()
    game.clock.tick(FPS)
