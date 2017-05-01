import pygame
from game_functions import *
from Good import *
from Evil import *
from Banana import *
from score_handler import *

def twitch(good_minion):
	if good_minion.x < 50 and good_minion.x < good_minion.previous_x and good_minion.x > 0:
		good_minion.x -= 7
		good_minion.prebious_x = good_minion.x
	elif good_minion.x == 0:
		good_minion.x = 1
		good_minion. previous_x = 0
	elif good_minion.x < 50 and good_minion.x > good_minion.previous_x:
		good_minion.x += 5
		good_minion.previous_x = good_minion.x
	else:
		good_minion.x = 50
		good_minion.previous_x = 50

def run_game():
	pygame.init()
	screen_size = (1400,527)
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption("Filet Minion")
	background_image = pygame.image.load("./images/background.png")
	title_text = pygame.image.load("./images/Filet_Minion.png")
	continue_text = pygame.image.load("./images/Continue.png")
        game_over_text = pygame.image.load("./images/Game_over.png")
        title_image = pygame.image.load("./images/pair.png")
	banana_image = pygame.image.load("./images/banana.png")
	sad_minion_image = pygame.image.load("./images/sad_minion.png") #game over minion
	banana_sound = pygame.mixer.Sound("./sounds/banana.wav")
	pygame.mixer.music.load("./sounds/super-bell-hill.wav")
	minion_yahoo = pygame.mixer.Sound("./sounds/minion-yahoo-3.wav")
	got_hit_sound = pygame.mixer.Sound("./sounds/minion-hit-2.wav")
	hit_enemy_sound = pygame.mixer.Sound("./sounds/squish.wav")
	pygame.mixer.music.play(-1)

	good_minion = Good(screen, "./images/good_minion.png")
	evil_minion = Evil(screen, "./images/evil_minion.png")

	goods = Group()
	goods.add(good_minion)

	evils = Group()
	evils.add(evil_minion)

	bananas = Group()

	tick = 0
        previous_bad_guy = 0  #This needs to be outside the while loop


	highest_score = getHighScore()

	#INTRO WELCOME SCREEN
	welcomeScreen(screen, title_text, title_image, continue_text, minion_yahoo)
        
	game_active = True
	last_shown = 0

	while game_active:
		in_game = True
		#evils.empty()	
		while in_game:
			tick += 1
		#	last_bad_guy = 0
	#		if not good_minion.isAlive():
	#			break
			if tick > previous_bad_guy + good_minion.opponent_frequency:
				evils.add(Evil(screen, "./images/evil_minion.png"))
				previous_bad_guy = tick
		
	#		if tick % 30 == 0:
	#				evils.add(Evil(screen, "./images/evil_minion.png"))

			screen.blit(background_image, [0,0])

			font = pygame.font.Font(None, 35)
			# timer = font.render("Seconds passed: %d" % (tick / 30), True, (0,0,0))
			lives = font.render("Lives: %d" % (good_minion.lives), True, (255,255,0))
			score = font.render("Score: %d" % (good_minion.score), True, (255,255,255))
			high_score = font.render("High Score: %d" % (highest_score), True, (255,255,255))

			# screen.blit(timer, [1200,50])
			screen.blit(lives, [1200,30])
			screen.blit(score, [1200,60])
			screen.blit(high_score, [1200,90])

			#Draw the player
			if good_minion.isAlive(): #added for sad_minion
				for good_minion in goods:
					good_minion.drawMe()
		#			if good_minion.lives > 0:
		#				goods.add(good_minion)

			for banana in bananas:
				banana.update()
				banana.drawBanana(tick)

			for evil_minion in evils:
				evil_minion.updateMe(good_minion)
				evil_minion.drawMe()

			checkEvents(good_minion, screen, bananas, tick, banana_sound, evils, minion_yahoo)

			Collisions(goods, evils, bananas, good_minion, evil_minion, got_hit_sound, hit_enemy_sound)
			twitch(good_minion)

			if good_minion.score > highest_score:
				highest_score = good_minion.score
				setHighScore(highest_score)

			if not good_minion.isAlive():
				screen.blit(sad_minion_image, [good_minion.x, good_minion.y])
				screen.blit(game_over_text, [310,100])
				in_game = checkEvents(good_minion, screen, bananas, tick, banana_sound, evils, minion_yahoo) 
                                if tick > last_shown + 50:
                                        last_shown = tick
                		if tick > last_shown + 30:
                        		screen.blit(continue_text, [315,220])
			pygame.display.flip()

run_game()

#One in a Minion
