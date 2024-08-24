import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0.0
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

def main():
	pygame.init()
	drawable = pygame.sprite.Group()
	updateable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = updateable
	Shot.containers = (shots, drawable, updateable)
	player = Player(x, y)
	asteroid_field = AsteroidField()

	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill((0, 0, 0))
		for drw in drawable:
			drw.draw(screen)	
		pygame.display.flip()
		dt = (clock.tick(60)) / 1000

		for upt in updateable:
			upt.update(dt)

		for asteroid in asteroids:
			for bullet in shots:
				if asteroid.collision(bullet):
					asteroid.split() 
			if asteroid.collision(player):
				print("Game over!")
				sys.exit()

if __name__ == "__main__":
    main()
