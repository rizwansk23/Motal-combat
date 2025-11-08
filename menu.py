import pygame
import componenet.button as button

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
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("assets/images/buttons/button_resume.png").convert_alpha()
options_img = pygame.image.load("assets/images/buttons/button_options.png").convert_alpha()
quit_img = pygame.image.load("assets/images/buttons/button_quit.png").convert_alpha()
video_img = pygame.image.load('assets/images/buttons/button_video.png').convert_alpha()
audio_img = pygame.image.load('assets/images/buttons/button_audio.png').convert_alpha()
keys_img = pygame.image.load('assets/images/buttons/button_keys.png').convert_alpha()
back_img = pygame.image.load('assets/images/buttons/button_back.png').convert_alpha()

#create button instances
resume_button = button.Button(344, 125, resume_img, 0.7)
options_button = button.Button(337, 220, options_img, 0.7)
quit_button = button.Button(376, 300, quit_img, 0.7)
video_button = button.Button(226, 75, video_img, 0.7)
audio_button = button.Button(225, 170, audio_img, 0.7)
keys_button = button.Button(246, 250, keys_img, 0.7)
back_button = button.Button(332, 350, back_img, 0.7)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


#game loop
run = True
while run:
    clock.tick(FPS)

    screen.fill((52, 78, 91))

    if menu_state == "main":   
        # draw_text('home page',font,TEXT_COL,100,100)
        image = pygame.image.load('assets/images/background/intro_page.png').convert_alpha()
        image = pygame.transform.smoothscale(image, (SCREEN_WIDTH,SCREEN_HEIGHT))
        screen.blit(image,(0,0))
    else:
        #check if game is paused
        if game_paused == True:
            #check menu state
            if menu_state == "game":

                key = pygame.key.get_pressed()

                if key[pygame.K_RETURN]:
                    game_paused = False 

                #draw pause screen buttons
                if resume_button.draw(screen):
                    game_paused = False
                if options_button.draw(screen):
                    menu_state = "options"
                if quit_button.draw(screen):
                    menu_state="main"
            #check if the options menu is open
            if menu_state == "options":
                #draw the different options buttons
                if video_button.draw(screen):
                    print("Video Settings")
                if audio_button.draw(screen):
                    print("Audio Settings")
                if keys_button.draw(screen):
                    print("Change Key Bindings")
                if back_button.draw(screen):
                    menu_state = "game"
        else:
            draw_text('space for pause the game ',font,TEXT_COL,100,100)

  #event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                 menu_state="game"
            if event.key == pygame.K_SPACE:
                game_paused = True
            if event.key == pygame.K_ESCAPE:
                run = False

        
    if event.type == pygame.QUIT:
        run = False

    pygame.display.update()

pygame.quit()

