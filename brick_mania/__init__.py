from .config import *
from .sprites import Paddle, Ball, BrickBreakable, BrickUnbreakable
import sys
import glob
import pygame


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("freesansbold.ttf", 20)

        self.paddle = Paddle()
        self.ball = Ball()
        self.moveables = pygame.sprite.Group(self.paddle, self.ball)
        self.bricks = pygame.sprite.Group()

        self.level = 3
        self.total_levels = len(glob.glob('levels/*.txt'))
        self.won = False

        pygame.display.set_caption("Brick Mania")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def populate_level(self):
        """
        Map Format:
        - -> Empty space
        b -> Breakable brick
        u -> Unbreakable brick
        """
        self.bricks.empty()
        self.ball.x_velocity = 0
        self.ball.y_velocity = -MAX_VELOCITY
        self.ball.centerx = SCREEN_WIDTH / 2,
        self.ball.centery = SCREEN_HEIGHT * (2/3)
        with open(f"levels/{self.level}.txt") as f:
            bricks_map = f.readlines()
            y = 50
            for row in bricks_map:
                x = 50
                for symbol in row:
                    if symbol == "b":
                        self.bricks.add(BrickBreakable((x, y)))
                    elif symbol == "u":
                        self.bricks.add(BrickUnbreakable((x, y)))
                    x += 101
                y += 51


    def handle_collisions(self):
        # Collision with paddle
        ball_paddle_collision = pygame.sprite.collide_rect(self.ball, self.paddle)
        if ball_paddle_collision:
            constant_of_proportionality = (PADDLE_WIDTH / 2) / MAX_VELOCITY
            new_x_velocity = (self.ball.rect.centerx - self.paddle.rect.centerx) / constant_of_proportionality
            self.ball.x_velocity = new_x_velocity
            self.ball.y_velocity = -self.ball.y_velocity

        # With bricks
        brick_colliding = pygame.sprite.spritecollideany(self.ball, self.bricks)
        if brick_colliding:
            # Ball is below or above brick
            if self.ball.rect.top >= brick_colliding.rect.bottom-5 or self.ball.rect.bottom <= brick_colliding.rect.top+5:
                self.ball.y_velocity = -self.ball.y_velocity

            # Ball is on the side of brick
            if self.ball.rect.right <= brick_colliding.rect.left+5 or self.ball.rect.left >= brick_colliding.rect.right-5:
                self.ball.x_velocity = -self.ball.x_velocity

            if brick_colliding.__class__.__name__ == "BrickBreakable":
                brick_colliding.kill()

        # With ceiling
        if self.ball.rect.top <= 0:
            self.ball.y_velocity = -self.ball.y_velocity
        # REMOVE THISSSSSSSSSSSSSSSSSSSSSSSSSSS
        if self.ball.rect.bottom >= SCREEN_HEIGHT:
            self.ball.y_velocity = -self.ball.y_velocity
        # With walls
        if self.ball.rect.x <= 0 or self.ball.rect.right >= SCREEN_WIDTH:
            self.ball.x_velocity = -self.ball.x_velocity


    def level_complete(self):
        for brick in self.bricks:
            if brick.__class__.__name__ == "BrickBreakable":
                return False
        return True
            
    def draw(self):
        self.screen.fill("black")
        self.moveables.draw(self.screen)
        self.bricks.draw(self.screen)
        score_text = self.font.render(f"Level: {self.level}/{self.total_levels}", True, "white")
        self.screen.blit(score_text, (10, 20))
        pygame.display.flip()
