import pygame
from fighter import  Fighter
from enemy import Enemy

class Main_game:
  def __init__(self,caharcter = 0):
    

    pygame.init()

    self.clock = pygame.time.Clock()
    self.FPS = 60

    #create game window
    self.SCREEN_WIDTH = 800
    self.SCREEN_HEIGHT = 432

    self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    pygame.display.set_caption("Parallax")

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
    ENEMY = 0
    character = caharcter
    if character == 0:
      action = 0
    else:
      action = 1

    # instence of fighter class 
    self.fighter1 = Fighter(90,190,False,CHARACTER_NAME[character],ACTIONS[action],STEPS[character],FRAME_SIZE[character],OFFSET[character],SCALE[character])
    self.fighter2 = Enemy(600,190,True,ENEMY_NAME[ENEMY],ACTIONS[1],ENEMY_STEPS[ENEMY],ENEMY_FRAME_SIZE[ENEMY],ENEMY_OFFSET[ENEMY],ENEMY_SCALE[ENEMY])

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



    self.fighter1.draw(screen)
    self.fighter2.draw(screen)
    self.fighter1.move(self.SCREEN_WIDTH,self.SCREEN_HEIGHT,screen,self.fighter2)
    self.fighter2.ai_move(self.SCREEN_WIDTH,self.fighter1)


    self.fighter1.update_attack(screen,self.fighter2)

    #get keypresses
    key = pygame.key.get_pressed()

    if self.fighter1.health > 0 and self.fighter2.health > 0:
      if key[pygame.K_a] and self.scroll > 0 :
          if self.fighter1.x < self.SCREEN_WIDTH + 10 :
            self.scroll -=  1.5
      if key[pygame.K_d] and self.scroll < 100:
        if self.fighter2.x > 10 :
          self.scroll += 1.5

    pygame.display.update()



