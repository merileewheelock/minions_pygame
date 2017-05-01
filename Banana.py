import pygame #Duh
from pygame.sprite import Sprite

class Banana(Sprite):
	def __init__(self, screen, good_minion, direction):
		super(Banana, self).__init__()
		self.screen = screen

		# self.rect = pygame.Rect(0,0, 50, 32)
		# self.rect.centerx = good_minion.rect.centerx
		# self.rect.top = good_minion.rect.top
		self.image = pygame.image.load("./images/banana.png")
#		self.image = pygame.transform.scale(self.image,(50,32))
		self.rect = self.image.get_rect()
		self.speed = 10
		self.x = good_minion.x + 100
		self.y = good_minion.y + 70
		self.direction = 2

	def update(self):

		if self.direction == 2: #right
			self.x += self.speed #change the y each time update is run
			self.rect.x = self.x #update rect position


	def drawBanana(self, tick): #Making the bullet (not importing image)
		# pygame.draw.rect(self.screen, self.color, self.rect)
		self.rect.left = self.x
		self.rect.top = self.y
		self.screen.blit(pygame.transform.rotate(self.image, tick*-5),[self.x, self.y])
#		self.image = pygame.transform.rotate(self.image, 90) #spinning banana!
