import pygame

pygame.init()

from brick_mania import Game

game = Game()

while True:
    game.handle_events()

    if not game.level_started:
        game.populate_level()
        game.level_started = True

    game.moveables.update()
    game.handle_collisions()
    game.draw()
    game.clock.tick(30)
