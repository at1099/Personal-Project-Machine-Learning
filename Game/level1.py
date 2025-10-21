import pygame, random
from obstacle import Obstacle

class Level:
    def __init__(self, speed, player):
        self.obstacles = []
        self.speed = speed
        self.timer = 0
        self.player = player
    
    def spawn_obstacle(self):
        obstacle = Obstacle(800, 520, self.speed, self.obstacles, self.player)
        self.obstacles.append(obstacle)
        

    def update(self):
        self.timer += 1
        if self.timer % 60 == 0:  # every 1 second
            if random.random() < 0.4:
                self.spawn_obstacle()