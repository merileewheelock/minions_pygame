import pygame
from pygame.sprite import Sprite
import math
from random import randint

class Evil(Sprite):
	def __init__(self, screen, image):
		super(Evil,self).__init__()
		self.image = pygame.image.load(image)
		self.speed = 10
		self.x = 1500
		self.y = randint(1,400)
		self.screen = screen
		self.rect = self.image.get_rect()
		# self.evil_freq = 120

	def updateMe(self, good_minion):
		self.x -= self.speed
		self.rect.top = self.y
		self.rect.left = self.x

	def drawMe(self):
		self.screen.blit(self.image, [self.x, self.y])