from .config import *
from .sounds import *
from .sprites import *
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

        self.level = 1
        self.level_started = False
        self.total_levels = len(glob.glob('levels/*.txt'))
        self.over = False

        pygame.display.set_caption("Brick Mania")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if not self.level_started:
                    self.ball.y_velocity = MAX_VELOCITY
                    self.level_started = True

                elif self.over:
                    self.level = 1
                    self.level_started = False
                    self.reset_sprites()
                    self.populate_level()
                    self.over = False
            

    def populate_level(self):
        """
        Map Format:
        - -> Empty space
        b -> Breakable brick
        u -> Unbreakable brick
        """
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
            sound_collision_hard.play()
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
                sound_collision_soft.play()
                brick_colliding.kill()
            else:
                sound_collision_hard.play()

        # With ceiling
        if self.ball.rect.top <= 0:
            sound_collision_hard.play()
            self.ball.y_velocity = -self.ball.y_velocity
        # With walls
        if self.ball.rect.x <= 0 or self.ball.rect.right >= SCREEN_WIDTH:
            sound_collision_hard.play()
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

        score_text = f"Level: {self.level}/{self.total_levels}"
        if not self.level_started:
            score_text += "             Use the right and left arrow keys to move."
        if self.over:
            score_text += "             Press any key to play again."
        self.screen.blit(self.font.render(score_text, True, "white"), (10, 20))
        pygame.display.flip()

    
    def reset_sprites(self):
        self.bricks.empty()
        self.moveables.empty()
        self.ball = Ball()
        self.paddle = Paddle()
        self.moveables.add(self.ball, self.paddle)

