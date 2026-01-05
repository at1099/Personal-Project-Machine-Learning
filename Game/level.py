import pygame, random
from obstacle import Obstacle

class Level:
    def __init__(self, speed, player, num_obs, obs_height, avg_gap, variance):
        self.obstacles = []
        self.speed = speed
        self.timer = 0
        self.player = player

        self.num_obs = num_obs
        self.obs_height = obs_height
        self.avg_gap = avg_gap
        self.variance = variance

        self.obs_placed = 0

    def spawn_obstacle(self):
        if self.obs_placed < self.num_obs:
            obstacle = Obstacle(
                800, 550-self.obs_height,
                self.obs_height,
                self.speed,
                self.obstacles,
                self.player
            )
            self.obstacles.append(obstacle)
            self.obs_placed += 1

    def update(self):
        self.timer += 1

        if self.timer % self.avg_gap == 0:
            if random.random() < self.variance:
                self.spawn_obstacle()
