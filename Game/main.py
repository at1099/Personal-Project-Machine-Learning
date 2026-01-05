import pygame
import time
import random
from player import Player
from level import Level
from logger import log_result

class Game:
    def __init__(self):
        #pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Geometry Dash AI")
        self.clock = pygame.time.Clock()
        self.ground_y = 550
        self.game_over = False
        self.player = Player(100, self.ground_y - 20)

        self.level = Level(5, self.player, num_obs=random.randint(5, 30), obs_height=random.randint(10, 40), avg_gap=random.randint(20, 100), variance=round(random.uniform(0.1, 0.6), 1))
        self.running = True

    def reset(self):
        time.sleep(1)
        print("Score was", self.player.score)

        self.player.score = 0
        self.player.rect.topleft = (100, self.ground_y - 50)
        self.player.vel_y = 0

        self.level = Level(
            5,
            self.player,
            num_obs=random.randint(5, 30),
            obs_height=random.randint(20, 60),
            avg_gap=random.randint(20, 100),
            variance=round(random.uniform(0.1, 0.6), 1)
        )


    def run(self):
        while self.running:
            self.key_presses()
            self.update()
            self.draw()

    def key_presses(self):
        if self.game_over:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.player.jump()


    def update(self):
        if self.game_over:
            return

        # collision check
        for obstacle in self.level.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
                print("Game Over! Score:", self.player.score)

                log_result(
                    self.level,
                    self.player.score,
                    completed=False
                )

                self.game_over = True
                return

        # level completed
        if self.player.score >= self.level.num_obs:
            print("Level Completed! Score:", self.player.score)

            log_result(
                self.level,
                self.player.score,
                completed=True
            )

            self.game_over = True
            return

        for obstacle in self.level.obstacles:
            obstacle.update()

        self.player.update(self.ground_y)
        self.level.update()



    def draw(self):
        self.screen.fill((30, 30, 30))
        pygame.draw.rect(self.screen, (100, 255, 100), (0, self.ground_y, 800, 50))
        pygame.draw.rect(self.screen, (0,0,255), self.player.rect)
        for object in self.level.obstacles:
            pygame.draw.rect(self.screen, (255,0,0), object.rect)
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()