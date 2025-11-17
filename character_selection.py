import pygame
import componenet.button as button


class image_load:
    def __init__(self,image,scale,x,y):
        width= image.get_width()
        height = image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(image,(width * scale , height * scale))
        self.x = x
        self.y = y

    def draw(self,screen):
        screen.blit(self.image,(self.x, self.y))


class character_selection:
    def __init__(self):
        self.run = False
        self.clock = pygame.time.Clock()
        self.FPS = 60


        #load images 
        next_img = pygame.image.load("assets/images/icons/next.png").convert_alpha()
        prev_img = pygame.image.load("assets/images/icons/previous.png").convert_alpha()
        img_1 = pygame.image.load("assets/images/character/Evil Wizard 3/preview1.png").convert_alpha()
        img_2 = pygame.image.load("assets/images/character/Hero Knight/preview1.png").convert_alpha()
        img_3 = pygame.image.load("assets/images/character/Huntress/preview1.png").convert_alpha()
        img_4 = pygame.image.load("assets/images/character/Martial Hero 3/preview1.png").convert_alpha()


        character_1 = image_load(img_1, 0.6, 220,50)
        character_2 = image_load(img_2, 1, 10, -100)
        character_3 = image_load(img_3, 0.8, 100, -120)
        character_4 = image_load(img_4, 1, 50, -70)



        #create button instances
        self.next_button = button.Button(750,180,next_img,1)
        self.prev_button = button.Button(10,180,prev_img,1)

        # game variable
        self.character_list = [character_1,character_2,character_3,character_4]
        self.i=0

    def draw(self,screen):
        screen.fill((202, 228, 241))
        self.clock.tick(self.FPS)

        if self.next_button.draw(screen):
                self.i += 1
                if self.i >= len(self.character_list) - 1:
                    self.i = -1
        if self.prev_button.draw(screen):
                self.i -= 1
                if self.i == -1:
                    self.i = len(self.character_list) - 1  

        try:
            self.character_list[self.i].draw(screen)
        except IndexError:
            self.character_list[0].draw(screen)
              


        #event handler
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                self.run = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                        self.i += 1
                        if self.i >= len(self.character_list) - 1:
                            self.i = -1
                if event.key == pygame.K_LEFT:
                        self.i -= 1
                        if self.i == -1:
                            self.i = len(self.character_list) - 1  


    def quit(self):
        return self.run
    

