import pygame
from fighter import  Fighter
from enemy import Enemy

class Main_game:
  def __init__(self,character,enemy,restart):
    

    pygame.init()

    self.clock = pygame.time.Clock()
    self.FPS = 60
    self.restart = restart

    #create game window
    self.SCREEN_WIDTH = 800
    self.SCREEN_HEIGHT = 432

    self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    pygame.display.set_caption("Parallax")

    #define game variables
    self.intro_count = 3
    self.last_count_update = pygame.time.get_ticks()
    self.score = [0, 0]#player scores. [P1, P2]
    self.round_over = False
    self.ROUND_OVER_COOLDOWN = 2000

    #define game variables
    self.scroll = 0

    self.ground_image = pygame.image.load("assets/images/background/ground.png").convert_alpha()
    self.ground_width = self.ground_image.get_width()
    self.ground_height = self.ground_image.get_height()

    self.bg_images = []
    for i in range(1, 6):
      bg_image = pygame.image.load(f"assets/images/background/plx-{i}.png").convert_alpha()
      self.bg_images.append(bg_image)
    self.bg_width = self.bg_images[0].get_width()


    CHARACTER_NAME = ['Evil Wizard 3','Hero Knight','Huntress','Martial Hero 3']
    ACTIONS = [['Idle','Run','Fall1','Attack','Take Hit','Death'],['Idle','Run','Jump','Attack1','Attack2','Take Hit','Death','Attack3']]
    STEPS = [[10,8,6,13,3,18],[11,8,3,7,7,4,11],[8,8,2,5,5,3,8,7],[10,8,3,7,6,3,11,9]]
    FRAME_SIZE = [140,180,150,126]
    OFFSET = [[200,160],[290,220],[290,256],[190,105]]
    SCALE=[3.5,3.5,4.5,3.5]

    ENEMY_NAME = ['warrior','wizard']
    ENEMY_STEPS = [[10,8,3,7,7,3,7,8],[8,8,2,8,8,3,7]]
    ENEMY_FRAME_SIZE = [162,250]
    ENEMY_OFFSET = [[270,225],[350,355]]
    ENEMY_SCALE = [4,3.2]

    # TEMPORRY VARIABLE
    self.enemy = enemy
    self.character = character
    if self.character == 0:
      action = 0
    else:
      action = 1


    # instence of fighter class 
    self.fighter1 = Fighter(90,190,False,CHARACTER_NAME[self.character],ACTIONS[action],STEPS[self.character],FRAME_SIZE[self.character],OFFSET[self.character],SCALE[self.character])
    self.fighter2 = Enemy(600,190,True,ENEMY_NAME[self.enemy],ACTIONS[1],ENEMY_STEPS[self.enemy],ENEMY_FRAME_SIZE[self.enemy],ENEMY_OFFSET[self.enemy],ENEMY_SCALE[self.enemy])

    #define font
    self.count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
    self.score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

    #load vicory image
    self.victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()
    self.victory_img = pygame.transform.scale(self.victory_img,(50*12,10*12))
    self.defeat_img = pygame.image.load('assets/images/icons/defeat.png').convert_alpha()
    self.defeat_img = pygame.transform.scale(self.defeat_img,(50*12,10*12))


  #function for drawing text
  def draw_text(self,text, font, text_col, x, y,screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

  # background image 
  def draw_bg(self,screen):
    for x in range(5):
      speed = 1
      for i in self.bg_images:
        screen.blit(i, ((x * self.bg_width) - self.scroll * speed, 0))
        speed += 0.2

  def draw_ground(self,screen):
    for x in range(15):
      screen.blit(self.ground_image, ((x * self.ground_width) - self.scroll * 2.5, self.SCREEN_HEIGHT - self.ground_height))


  # draw health bar of player
  def draw_health_bar(self,screen,health , x ,y,):
    
    # color
    YELLOW = (255,255,0)
    RED = (255,0,0)
    GREEN = (0 , 255, 0)
    WHITE = (0,0,0)

    ratio = health / 100
    pygame.draw.rect(screen,WHITE , (x -3,y -3 ,306,36))
    pygame.draw.rect(screen,RED , (x,y,300,30))
    pygame.draw.rect(screen,GREEN , (x,y,300 * ratio,30))

  def draw(self,screen):


    
    self.clock.tick(self.FPS)

    #draw world
    self.draw_bg(screen)
    self.draw_ground(screen)
    self.draw_health_bar(screen,self.fighter1.health,10,10)
    self.draw_health_bar(screen,self.fighter2.health,490,10)

    self.fighter1.update_animation(self.screen)
    self.fighter2.update_animation(screen)

    if self.restart:
      self.intro_count = 3
      self.restart = False
    
      #update countdown
    if self.intro_count <= 0:
      #move fighters
      self.fighter1.move(self.SCREEN_WIDTH,self.SCREEN_HEIGHT,screen,self.fighter2)
      self.fighter2.ai_move(self.SCREEN_WIDTH,self.fighter1)
    else:
      if self.enemy in [0,1]:
        #display count timer
        self.draw_text(str(self.intro_count), self.count_font, (255,0,0), self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 3,screen)
        #update count timer
        if (pygame.time.get_ticks() - self.last_count_update) >= 1000:
          self.intro_count -= 1
          self.last_count_update = pygame.time.get_ticks()


      #check for player defeat
    if self.round_over == False:
      if self.fighter1.alive == False:
        # self.score[1] += 1
        self.round_over = True
        self.round_over_time = pygame.time.get_ticks()
      elif self.fighter2.alive == False:
        # self.score[0] += 1
        self.round_over = True
        self.round_over_time = pygame.time.get_ticks()
    else:
      #display victory image
      if self.fighter1.alive:
        screen.blit(self.victory_img, (110, 100))
        if pygame.time.get_ticks() - self.round_over_time > self.ROUND_OVER_COOLDOWN:
          self.round_over = False
          if self.enemy == 1:
            screen.blit(self.victory_img, (110, 100))
            self.round_over = True
          if self.enemy == 0:
            self.intro_count = 3
            self.enemy = 1
            self.__init__(self.character,self.enemy,self.restart)
      else:
        screen.blit(self.defeat_img,(110,100)) 




    self.fighter1.draw(screen)
    self.fighter2.draw(screen)


    self.fighter1.update_attack(screen,self.fighter2)

    #get keypresses
    key = pygame.key.get_pressed()
    if self.intro_count <=0:
      if self.fighter1.health > 0 and self.fighter2.health > 0:
        if key[pygame.K_a] and self.scroll > 0 :
            if self.fighter1.x < self.SCREEN_WIDTH + 10 :
              self.scroll -=  1.5
        if key[pygame.K_d] and self.scroll < 100:
          if self.fighter2.x > 10 :
            self.scroll += 1.5

    pygame.display.update()



