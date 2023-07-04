import pygame

pygame.init()

from brick_mania import Game

game = Game()
game.populate_level()

while True:
    game.handle_events()

    if not game.won:
        game.moveables.update()
        game.handle_collisions()

        if game.level_complete():
            if game.level == game.total_levels:
                game.won = True
            else:
                game.level += 1
                game.populate_level()

    game.draw()
    game.clock.tick(30)
