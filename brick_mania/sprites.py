from .config import *
import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/paddle.png").convert_alpha()
        self.rect = self.image.get_rect(
            centerx=SCREEN_WIDTH / 2,
            y=SCREEN_HEIGHT - PADDLE_HEIGHT - 10
        )

    def update(self):
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
        self.image = pygame.image.load("assets/ball.png").convert_alpha()
        self.rect = self.image.get_rect(
            centerx=SCREEN_WIDTH / 2,
            centery=SCREEN_HEIGHT * (2/3)
        )
        self.x_velocity = 0
        self.y_velocity = MAX_VELOCITY

    def update(self):
        self.rect.move_ip(self.x_velocity, self.y_velocity)


class Brick(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

class BrickBreakable(Brick):
    def __init__(self, coordinates):
        self.image = pygame.image.load("assets/brick_breakable.png").convert_alpha()
        super().__init__(coordinates)

class BrickUnbreakable(Brick):
    def __init__(self, coordinates):
        self.image = pygame.image.load("assets/brick_unbreakable.png").convert_alpha()
        super().__init__(coordinates)
