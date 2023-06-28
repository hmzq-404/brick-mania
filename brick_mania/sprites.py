from .config import *
import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.rect = self.surf.get_rect(
            centerx=SCREEN_WIDTH / 2,
            y=SCREEN_HEIGHT - PADDLE_HEIGHT - 10
        )

        self.surf.fill("white")

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.rect.right + PADDLE_SPEED < SCREEN_WIDTH:
                self.rect.move_ip(PADDLE_SPEED, 0)

        elif keys[pygame.K_LEFT]:
            if self.rect.left - PADDLE_SPEED > 0:
                self.rect.move_ip(-PADDLE_SPEED, 0)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        