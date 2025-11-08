import pygame
from fighter import  Fighter

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


# instence of fighter class 
fighter1 = Fighter(90,190)
fighter2 = Fighter(600,190)



#game loop
run = True
while run:

  clock.tick(FPS)

  #draw world
  draw_bg()
  draw_ground()
  draw_health_bar(fighter1.health,10,10)
  draw_health_bar(fighter2.health,490,10)
  fighter1.draw(screen)
  fighter2.draw(screen)
  fighter1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter2)
  # fighter2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter1)


  fighter1.update_attack(screen,fighter2)

  #get keypresses
  key = pygame.key.get_pressed()
  if key[pygame.K_a] and scroll > 0 :
      if fighter1.x < SCREEN_WIDTH + 10 :
        scroll -=1
  if key[pygame.K_d] and scroll < 100:
    if fighter2.x > 10 :
      scroll += 1

  #event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()


pygame.quit()