import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        vector_positive = self.velocity.rotate(random_angle)
        vector_negative = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_positive = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_negative = Asteroid(self.position.x, self.position.y, new_radius)  
        asteroid_positive.velocity = vector_positive * ASTEROID_VELOCITY_MULTIPLIER
        asteroid_negative.velocity = vector_negative * ASTEROID_VELOCITY_MULTIPLIER