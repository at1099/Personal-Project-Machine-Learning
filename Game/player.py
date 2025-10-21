import pygame
class Player():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x,y,50,50)
        self.vel_y = 0
        self.jumping = False
        self.score = 0

    def gravity(self):
        self.vel_y += 0.6
        self.rect.y += self.vel_y

    def jump(self):
        if not self.jumping:
            self.vel_y = -10
            self.jumping = True

    def update(self, ground_y):
        self.gravity()
        if self.rect.bottom >= ground_y:
            self.rect.bottom = ground_y
            self.jumping = False