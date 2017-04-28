import pygame
from game_functions import *
from Good import *
from Evil import *
from Banana import *

def run_game():
	pygame.init()
	screen_size = (1400,527)
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption("Filet Minion")
	background_image = pygame.image.load("./images/background.png")
	banana_image = pygame.image.load("./images/banana.png")
	banana_sound = pygame.mixer.Sound("./sounds/banana.wav")

	good_minion = Good(screen, "./images/good_minion.png")
	evil_minion = Evil(screen, "./images/evil_minion.png")

	goods = Group()
	goods.add(good_minion)

	evils = Group()
	evils.add(evil_minion)

	bananas = Group()

	tick = 0
	while 1:
		tick += 1
		if tick % evil_minion.evil_freq == 0:
			evils.add(Evil(screen, "./images/evil_minion.png"))

		screen.blit(background_image, [0,0])

		font = pygame.font.Font(None, 25)
		# timer = font.render("Seconds passed: %d" % (tick / 30), True, (0,0,0))
		lives = font.render("Lives: %d" % (good_minion.lives), True, (0,0,0))
		score = font.render("Score: %d" % (good_minion.score), True, (0,0,0))

		high_score = font.render("High Score: %d" % (0), True, (0,0,0))

		# screen.blit(timer, [1200,50])
		screen.blit(lives, [1200,50])
		screen.blit(score, [1200,80])
		screen.blit(high_score, [1200,110])

		#Draw the player
		for good_minion in goods:
			good_minion.drawMe()
			if good_minion.lives > 0:
				goods.add(good_minion)

		for banana in bananas:
			banana.update()
			banana.drawBanana()

		for evil_minion in evils:
			evil_minion.updateMe(good_minion)
			evil_minion.drawMe()

		checkEvents(good_minion, screen, bananas, tick, banana_sound)

		Collisions(goods, evils, bananas, good_minion, evil_minion)

		if not good_minion.isAlive():
			font = pygame.font.Font(None, 100)
			game_over = font.render("GAME OVER", True, (0,0,0))
			screen.blit(game_over, [500,200])

		pygame.display.flip()

run_game()

#Filet Minion
#One in a Minion