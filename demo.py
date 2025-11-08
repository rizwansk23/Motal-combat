import pygame

#create display window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Demo')

#game loop
run = True
while run:

	screen.fill((202, 228, 241))

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()