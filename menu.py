import pygame
import componenet.button as button
import character_selection as character_selection
import animation 
from main import Main_game
from character_selection import image_load

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432

clock = pygame.time.Clock()
FPS = 60


#fullscreen 
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.FULLSCREEN)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "home"  # home, screen1, screen2, menu, optional_menu 

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("assets/images/buttons/Resume.png").convert_alpha()
replay_img = pygame.image.load("assets/images/buttons/Replay.png").convert_alpha()
quit_img = pygame.image.load("assets/images/buttons/ExitO.png").convert_alpha()

box_img =  pygame.image.load('assets/images/icons/Box.png').convert_alpha()
banner_img =  pygame.image.load('assets/images/icons/Banner.png').convert_alpha()


#create button instances
resume_button = button.Button(306, 140, resume_img, 0.2)
replay_button = button.Button(306, 220, replay_img, 0.2)
quit_button = button.Button(306, 300, quit_img, 0.2)



# image instances

box = image_load(box_img,0.2,250,100)
banner = image_load(banner_img,0.2,290,50)



def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

game_start = False



select_character = character_selection.character_selection()

resume = False
restart = False

#game loop
run = True
while run:
    clock.tick(FPS)

    screen.fill((52, 78, 91))

    if menu_state == "home":   
        # draw_text('home page',font,TEXT_COL,100,100)
        image = pygame.image.load('assets/images/background/intro_page.png').convert_alpha()
        image = pygame.transform.smoothscale(image, (SCREEN_WIDTH,SCREEN_HEIGHT))
        screen.blit(image,(0,0))
        game_start = False
    else:
        #check if game is paused
        if game_paused == True:
            #check menu state
            if menu_state == "game":

                key = pygame.key.get_pressed()

                if key[pygame.K_RETURN]:
                    game_paused = False 

                box.draw(screen)
                banner.draw(screen)

                #draw pause screen buttons
                if resume_button.draw(screen):
                    game_paused = False


                if replay_button.draw(screen):
                    game_paused = False
                    resume = True
                    main_panel = Main_game(character,0,restart)

                if quit_button.draw(screen):
                    game_start = False
                    menu_state = 'home'
                    game_paused = False
                    game_start = False
                    select_character.reset()  
        else:
            if game_start == False:

                # character select page
                select_character.draw(screen)
                     
                    
                if select_character.quit():
                    run = False

                character = select_character.get_character()
                
                if character is not None:
                    game_start = True
                    main_panel = Main_game(character,0,restart)
            # game page 
            
            elif game_start == True:
                main_panel.draw(screen)

            


            
          

  #event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                 menu_state="game"
            if event.key == pygame.K_ESCAPE:
                game_paused = True
            # if event.key == pygame.K_ESCAPE:
            #     run = False

        
    if event.type == pygame.QUIT:
        run = False

    pygame.display.update()

pygame.quit()
