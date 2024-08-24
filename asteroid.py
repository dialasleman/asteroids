from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self) 
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        first_vector = self.velocity.rotate(random_angle)
        second_vector = self.velocity.rotate(random_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        first_asteroid.velocity = first_vector * 1.2
        second_asteroid.velocity = second_vector * 1.2


    