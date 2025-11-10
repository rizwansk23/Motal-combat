import pygame
import componenet.button as button

#create display window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Demo')

clock = pygame.time.Clock()
FPS = 60

class image_load:
    def __init__(self,image,scale):
        width= image.get_width()
        height = image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(image,(width * scale , height * scale))

    def draw(self,screen,x,y):
        screen.blit(self.image,(x,y))

        


#load images 
next_img = pygame.image.load("assets/images/icons/next.png")
prev_img = pygame.image.load("assets/images/icons/previous.png")
img_1 = pygame.image.load("assets/images/Evil Wizard 3/preview1.png")
img_2 = pygame.image.load("assets/images/Hero Knight/preview1.png")
img_3 = pygame.image.load("assets/images/Huntress/preview1.png")
img_4 = pygame.image.load("assets/images/Martial Hero 3/preview1.png")


character_1 = image_load(img_1,0.6)
character_2 = image_load(img_2,1)
character_3 = image_load(img_3,0.8)
character_4 = image_load(img_4,1)



#create button instances
next_button = button.Button(750,180,next_img,1)
prev_button = button.Button(10,180,prev_img,1)

# game variable
character_list = [character_1,character_2,character_3,character_4]
i=0


#game loop
run = True
while run:

    screen.fill((202, 228, 241))
    clock.tick(FPS)

    key = pygame.key.get_pressed()

    # character_1.draw(screen,220,50)
    # character_2.draw(screen,10,-100)
    # character_3.draw(screen,100,-120)
    # character_4.draw(screen,50,-70)

    # character_list[0].draw(screen,220,50)


    if next_button.draw(screen) or key[pygame.K_RIGHT]:
        i += 1
        if i >= len(character_list) - 1:
            i = -1
        character_list[i].draw(screen,10,-100)
    if prev_button.draw(screen) or key[pygame.K_LEFT]:
        character_list[i]
        i -= 1
        if i == -1:
            i = len(character_list) - 1  


    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()