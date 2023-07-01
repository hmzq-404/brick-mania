from .config import *
import sys
import pygame


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        from .sprites import Paddle, Ball, Brick
        self.paddle = Paddle()
        self.ball = Ball()

        pygame.display.set_caption("Brick Mania")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def handle_collisions(self):
        paddle_ball_collision = self.paddle.mask.overlap(
            self.ball.mask,
            (self.ball.rect.x - self.paddle.rect.x, self.ball.rect.y - self.paddle.rect.y)
        )
        if paddle_ball_collision:
            constant_of_proportionality = (PADDLE_WIDTH / 2) / MAX_VELOCITY
            new_x_velocity = (self.ball.rect.centerx - self.paddle.rect.centerx) / constant_of_proportionality
            self.ball.x_velocity = new_x_velocity
            self.ball.y_velocity = -self.ball.y_velocity

        # With ceiling
        if self.ball.rect.top <= 0:
            self.ball.y_velocity = -self.ball.y_velocity
        # With walls
        if self.ball.rect.x <= 0 or self.ball.rect.right >= SCREEN_WIDTH:
            self.ball.x_velocity = -self.ball.x_velocity
            
    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.paddle.surf, self.paddle.rect)
        self.screen.blit(self.ball.surf, self.ball.rect)
        pygame.display.flip()
