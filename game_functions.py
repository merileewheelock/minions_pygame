import pygame
import sys
from Banana import Banana
from pygame.sprite import Group, groupcollide
from Good import *

def checkEvents(good_minion, screen, bananas, tick, banana_sound):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN and good_minion.isAlive():
			if event.key == 273:
				good_minion.shouldMove("up", True)
			elif event.key == 274:
				good_minion.shouldMove("down", True)
			elif event.key == 32: #spacebar to FIRE
				for direction in range(2, 3):
					new_banana  = Banana(screen, good_minion, direction)
					bananas.add(new_banana)
				banana_sound.play()

		elif event.type == pygame.KEYUP:
			if event.key == 273:
				good_minion.shouldMove("up", False)
			elif event.key == 274:
				good_minion.shouldMove("down", False)


def Collisions(goods, evils, bananas, good_minion, evil_minion):
	good_died = groupcollide(goods, evils, False, True) #will make hero die when they collide
	evil_died = groupcollide(bananas, evils, True, True)
	good_minion_died = not len(good_died) == 0
	evil_minion_died = not len(evil_died) == 0

	if good_minion_died:
		good_minion.decreaseLife()
	if evil_minion_died:
		good_minion.score += 1
		evil_minion.evil_freq -= 20
