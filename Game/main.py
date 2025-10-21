import pygame
import time
from player import Player
from level1 import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Geometry Dash AI")
        self.clock = pygame.time.Clock()
        self.ground_y = 550

        self.player = Player(100, self.ground_y - 20)

        self.level = Level(5, self.player)
        self.running = True

    def reset(self):
        self.level.obstacles = []
        time.sleep(2)
        print("Score was", self.player.score)
        self.player.score = 0
        self.player.rect.topleft = (100, self.ground_y - 50)
        self.player.vel_y = 0

    def run(self):
        while self.running:
            self.key_presses()
            self.update()
            self.draw()

    def key_presses(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.player.jump()

    def update(self):
        if pygame.sprite.spritecollideany(self.player, self.level.obstacles):
            self.reset()

        for object in self.level.obstacles:
            object.update()
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