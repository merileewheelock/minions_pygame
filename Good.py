import pygame
from pygame.sprite import Sprite
from random import randint

class Good(Sprite):
	def __init__(self, screen, image):
		super(Good, self).__init__()
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image,(150,150))
		self.x = 50
		self.y = randint(100,250)
		self.speed = 10
		self.screen = screen
		self.should_move_up = False
		self.should_move_down = False
		self.should_move_left = False
		self.should_move_right = False
		self.rect = self.image.get_rect()
		self.lives = 3
		self.score = 0
                self.opponent_frequency = 100
		self.previous_x = 50

	def drawMe(self):
		if self.should_move_up and self.y > 0:
			self.y -= self.speed
		elif self.should_move_down and self.y < 377:
			self.y += self.speed
		# if self.should_move_left:
		# 	self.x -= self.speed
		# elif self.should_move_right:
		# 	self.x += self.speed

		self.rect.left = self.x
		self.rect.top = self.y
		self.screen.blit(self.image, [self.rect.left, self.rect.top])

	def shouldMove(self, direction, true_or_false):
		if direction == "up":
			self.should_move_up = true_or_false
		elif direction == "down":
			self.should_move_down = true_or_false
		# if direction == "left":
		# 	self.should_move_left = true_or_false
		# elif direction == "right":
		# 	self.should_move_right = true_or_false

	def decreaseLife(self):
		if self.lives > 0:
			self.lives -= 1

	def isAlive(self):
		return self.lives > 0
