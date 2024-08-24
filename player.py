import pygame
from shot import *
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.position = pygame.Vector2(x, y)
		self.rotation = 0.0
		self.timer = 0.0
	
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	
	def draw(self, screen):
		pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def update(self, dt):
		self.timer -= dt
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(dt)
		if keys[pygame.K_d]:
			self.rotate(dt * -1)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(dt * -1)
		if keys[pygame.K_SPACE]:
			self.shoot(self.position)
			self.timer = PLAYER_SHOOT_COOLDOWN 


	def shoot(self, position):
		if self.timer <= 0.0 :
			shot = Shot(position[0], position[1])
			shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

		