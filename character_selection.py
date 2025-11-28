import pygame
import componenet.button as button
import componenet.text as text




class image_load:
    def __init__(self,image,scale:int,x:int,y:int):
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
        self.charcter = 0


        #load images 
        next_img = pygame.image.load("assets/images/icons/next.png").convert_alpha()
        prev_img = pygame.image.load("assets/images/icons/previous.png").convert_alpha()
        select_img = pygame.image.load("assets/images/buttons/select.png").convert_alpha()
        img_1 = pygame.image.load("assets/images/character/Evil Wizard 3/preview1.png").convert_alpha()
        img_2 = pygame.image.load("assets/images/character/Hero Knight/preview1.png").convert_alpha()
        img_3 = pygame.image.load("assets/images/character/Huntress/preview1.png").convert_alpha()
        img_4 = pygame.image.load("assets/images/character/Martial Hero 3/preview1.png").convert_alpha()
        background = pygame.image.load("assets/images/background/stage4.jpg").convert_alpha()
        # platform = pygame.image.load("assets/images/background/ground.png").convert_alpha()
        # width = platform.get_width()


        #create a image instances
        character_1 = image_load(img_1, 0.6, 220,50)
        character_2 = image_load(img_2, 1, 10, -100)
        character_3 = image_load(img_3, 0.8, 100, -120)
        character_4 = image_load(img_4, 1, 50, -70)
        self.background = image_load(background,1.3,0,-100)
        # self.platform = []
        # for i in range(0,3):
        #     self.platform.append(image_load(platform,1,i * width,340))



        #create button instances
        self.next_button = button.Button(750,180,next_img,1)
        self.prev_button = button.Button(10,180,prev_img,1)
        self.select_button = button.Button(330,360,select_img,0.45)

        # game variable
        self.character_list = [character_1,character_2,character_3,character_4]
        self.character_name = ['Evil Wizard','Hero Knight','Hunter','Martial Hero']
        self.i=0

    # def ground(self,screen):
    #     for n in range(0,3):
    #         self.platform[n].draw(screen)
              
              
    def draw(self,screen):
        # screen.fill((202, 228, 241))

        # draw background
        self.background.draw(screen)
        # self.ground(screen)

        self.clock.tick(self.FPS)


        #logic to change the character
        if self.next_button.draw(screen):
                self.i += 1
                if self.i >= len(self.character_list) - 1:
                    self.i = -1
        if self.prev_button.draw(screen):
                self.i -= 1
                if self.i == -1:
                    self.i = len(self.character_list) - 1  

        # draw character name

        #draw character in frame 
        try:
            text.draw_text(self.character_name[self.i],10,10,screen)
            self.character_list[self.i].draw(screen)
        except IndexError:
            text.draw_text(self.character_name[0],10,10,screen)
            self.character_list[0].draw(screen)

        
        # draw select button
        if self.select_button.draw(screen):
            self.charcter = self.i

        
              


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

                if event.key == pygame.K_RETURN:
                     self.charcter = self.i
                     


    def quit(self):
        return self.run
    
    def get_character(self):
        return  self.charcter
    

