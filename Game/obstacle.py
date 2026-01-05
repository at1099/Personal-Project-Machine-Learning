import pygame
class Obstacle():
    def __init__(self, x, y, height, speed, list_from, player):
        self.rect = pygame.Rect(x,y, 30, height)
        self.speed = speed
        self.list_from = list_from
        self.player = player

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.list_from.remove(self)
            self.player.score += 1