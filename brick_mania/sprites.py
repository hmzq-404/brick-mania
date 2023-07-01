from .assets import *
from .config import *
import pygame


class Paddle:
    def __init__(self):
        super().__init__()
        self.surf = paddle_image
        self.rect = self.surf.get_rect(
            centerx=SCREEN_WIDTH / 2,
            y=SCREEN_HEIGHT - PADDLE_HEIGHT - 10
        )
        self.mask = pygame.mask.from_surface(self.surf)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.rect.right + PADDLE_SPEED < SCREEN_WIDTH:
                self.rect.move_ip(PADDLE_SPEED, 0)

        elif keys[pygame.K_LEFT]:
            if self.rect.left - PADDLE_SPEED > 0:
                self.rect.move_ip(-PADDLE_SPEED, 0)


class Ball:
    def __init__(self):
        super().__init__()
        self.surf = ball_image
        self.rect = self.surf.get_rect(
            centerx=SCREEN_WIDTH / 2,
            centery=SCREEN_HEIGHT * (2/3)
        )
        self.mask = pygame.mask.from_surface(self.surf)
        self.x_velocity = 0
        self.y_velocity = MAX_VELOCITY

    def move(self):
        self.rect.move_ip(self.x_velocity, self.y_velocity)


class Brick:
    def __init__(self):
        super().__init__()
        