import pygame
class Obstacle():
    def __init__(self, x, y, speed, list, player):
        self.rect = pygame.Rect(x,y, 30, 30)
        #self.rect1 = pygame.Rect(x1,y1,1,10)
        #self.rect2 = pygame.Rect(x2,y2,1,10)
        self.speed = speed
        self.list = list
        self.player = player

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.list.remove(self)
            self.player.score += 1