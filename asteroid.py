import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, radius)
        a = self.velocity.rotate(random_angle)
        asteroid_1.velocity = a * 1.2

        asteroid_2 = Asteroid(self.position.x, self.position.y, radius)
        b = self.velocity.rotate(-random_angle)
        asteroid_2.velocity = b * 1.2
