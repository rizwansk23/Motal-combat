import pygame
from fighter import  Fighter
from enemy import Enemy

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# color
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0 , 255, 0)
WHITE = (0,0,0)

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Parallax")

#define game variables
scroll = 0

ground_image = pygame.image.load("assets/images/background/ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
for i in range(1, 6):
  bg_image = pygame.image.load(f"assets/images/background/plx-{i}.png").convert_alpha()
  bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

# background image 
def draw_bg():
  for x in range(5):
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed, 0))
      speed += 0.2

def draw_ground():
  for x in range(15):
    screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height))


# draw health bar of player
def draw_health_bar(health , x ,y,):
  ratio = health / 100
  pygame.draw.rect(screen,WHITE , (x -3,y -3 ,306,36))
  pygame.draw.rect(screen,RED , (x,y,300,30))
  pygame.draw.rect(screen,GREEN , (x,y,300 * ratio,30))

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
character = 0
if character == 0:
  action = 0
else:
  action = 1

# instence of fighter class 
fighter1 = Fighter(90,190,False,CHARACTER_NAME[character],ACTIONS[action],STEPS[character],FRAME_SIZE[character],OFFSET[character],SCALE[character])
fighter2 = Enemy(600,190,True,ENEMY_NAME[ENEMY],ACTIONS[1],ENEMY_STEPS[ENEMY],ENEMY_FRAME_SIZE[ENEMY],ENEMY_OFFSET[ENEMY],ENEMY_SCALE[ENEMY])

# enemy = Enemy(600,190,True,character_name[2],actions[0],steps)



#game loop
run = True
while run:

  clock.tick(FPS)

  #draw world
  draw_bg()
  draw_ground()
  draw_health_bar(fighter1.health,10,10)
  draw_health_bar(fighter2.health,490,10)

  fighter1.update_animation(screen)
  fighter2.update_animation(screen)

  # enemy.update_ai(fighter1)
  # enemy.update_animation()
  # enemy.draw(screen)


  fighter1.draw(screen)
  fighter2.draw(screen)
  fighter1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter2)
  # fighter2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter1)
  fighter2.ai_move(SCREEN_WIDTH,fighter1)


  fighter1.update_attack(screen,fighter2)

  #get keypresses
  key = pygame.key.get_pressed()

  if fighter1.health > 0 and fighter2.health > 0:
    if key[pygame.K_a] and scroll > 0 :
        if fighter1.x < SCREEN_WIDTH + 10 :
          scroll -=  1.5
    if key[pygame.K_d] and scroll < 100:
      if fighter2.x > 10 :
        scroll += 1.5


  #event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()


pygame.quit()