import pygame
import sys
from Banana import Banana
from pygame.sprite import Group, groupcollide
from Good import *




def checkEvents(good_minion, screen, bananas, tick, banana_sound, evils, minion_yahoo):
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
#starts
		elif event.type==pygame.KEYDOWN and not good_minion.isAlive():
			if event.key == 13:
	                        good_minion.lives = 3
        	                good_minion.score = 0
                	        good_minion.opponent_frequency = 100
				evils.empty()
				minion_yahoo.play()
                        	return False
#ends
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				good_minion.shouldMove("up", False)
			elif event.key == 274:
				good_minion.shouldMove("down", False)


def Collisions(goods, evils, bananas, good_minion, evil_minion, got_hit_sound, hit_enemy_sound):
	good_died = groupcollide(goods, evils, False, True) #will make hero die when they collide
	evil_died = groupcollide(bananas, evils, True, True)
	good_minion_died = not len(good_died) == 0
	evil_minion_died = not len(evil_died) == 0

	if good_minion_died and good_minion.isAlive():
		good_minion.decreaseLife()
		got_hit_sound.play()
		if good_minion.lives > 0:
			good_minion.x -=1
	if evil_minion_died:
		good_minion.score += 1
		if good_minion.opponent_frequency > 2:
			good_minion.opponent_frequency -= 2 
			hit_enemy_sound.play()


def welcomeScreen(screen, title_text, title_image, continue_text, minion_yahoo):
	#yellow = (255,255,0)
        white = (250,250,250)
	end_welcome_screen = False
	tick2 = 0
        last_shown = 0
	while (end_welcome_screen == False):
		#screen.blit(title_text, [210,200])
		screen.fill(white)
		#welcome_font1 = pygame.font.SysFont(None, 200)
		#welcome_font2 = pygame.font.SysFont(None, 60)
                tick2 += 1
		
		#welcome_message1 = welcome_font1.render("FILET MINION", 1, (13,3,163) )
		#welcome_message2 = welcome_font2.render("Press any key to continue", True, (255,255,255))

		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN and event.key == 13:
				end_welcome_screen = True
				minion_yahoo.play()
			elif event.type == pygame.QUIT:
				sys.exit()
		screen.blit(title_image, [160,50])
		#screen.blit(welcome_message1,(210,200))
		if tick2 > last_shown + 30:
	#		screen.blit(welcome_message2,(450,320))
			screen.blit(continue_text, [515,320])
		if tick2 > last_shown + 50:
			last_shown = tick2 
		
		screen.blit(title_text, [460,150])
		pygame.display.flip()

