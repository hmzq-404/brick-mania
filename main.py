import pygame


pygame.init()

from brick_mania import Game
from brick_mania.config import *
from brick_mania.sounds import *

game = Game()
game.populate_level()

while True:
    game.handle_events()

    if not game.over:
        game.moveables.update()
        game.handle_collisions()

        if game.level_complete():
            if game.level == game.total_levels:
                game.over = True
                sound_game_won.play()
            else:
                sound_level_complete.play()
                game.level += 1
                game.reset_sprites()
                game.populate_level()
                game.level_started = False

        if game.ball.rect.bottom >= SCREEN_HEIGHT:
            game.over = True
            sound_game_lost.play()

    game.draw()
    game.clock.tick(30)





