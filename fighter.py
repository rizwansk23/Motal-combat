import pygame
import animation 

class Fighter:
    def __init__(self,x,y):
        self.x = x
        self.flip = False
        self.rect = pygame.Rect(x,y,80,180)
        self.image = animation.animation("Evil Wizard 3","Attack",140,140,13,3.5,100)
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0 
        self.attack_active = False
        self.health = 100

    def move(self,screen_width,screen_height,surface,target):

        SPEED = 5
        GRAVITY = 2

        dx = 0
        dy = 0

        # keyboard input 
        key = pygame.key.get_pressed()
        
        if self.attacking == False:
            # moving 
            if key[pygame.K_d]:
                dx = SPEED
                # self.image = animation.animation("Evil Wizard 3","Run",140,140,8,4)
            if key[pygame.K_a]:
                dx = -SPEED
            # jump
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -15
                self.jump= True
          # attack
            if key[pygame.K_r]  or key[pygame.K_t]:
                if key[pygame.K_r]:
                    self.attack(surface,target)
                    self.attack_type = 1
                if key[pygame.K_t]:
                    self.start_attack()
                    self.attack_type = 2
            
        # apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # check the player are stay on screen
        if self.rect.left + dx <= 0:
            dx = -self.rect.left
        if self.rect.right + dx >= screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 62 :
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 62 - self.rect.bottom

        # ensure player face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True


        self.rect.x += dx
        self.rect.y += dy


    def attack(self,surface,target):
        # self.attacking = True

        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 1.5 * self.rect.width, self.rect.height)
        pygame.draw.rect(surface,(0,255,0),attacking_rect)

        if attacking_rect.colliderect(target.rect):
            target.health -= 10
            self.attacking = False

    def start_attack(self):
        if not self.attack_active:
            direction = -1 if self.flip else 1
            self.attack_rect = pygame.Rect(self.rect.centerx + (20 * direction),self.rect.centery - 55,50,20)
            self.attack_img = animation.animation("Evil Wizard 3","Moving",50,50,4,3.5,100)
            self.attack_speed = 10 * direction
            self.attack_active = True
            self.x = self.rect.x

    def update_attack(self, surface, target):
        if self.attack_active and self.attack_rect and self.attack_img:
            # Move attack
            self.x += self.attack_speed
            self.attack_rect.x += self.attack_speed

            # Draw projectile
            # pygame.draw.rect(surface, (0,0,0,128), self.attack_rect)
            self.attack_img.draw(self.x+10,self.rect.y - 60,surface,False)

            # Collision check
            if  self.attack_rect.colliderect(target.rect):
                target.health -= 10
                self.attack_active = False

            # Out of screen
            if (self.attack_rect.right < 0 or self.attack_rect.left > surface.get_width()):
                self.attack_active = False
                self.attack_rect = None
                self.attack_img = None


            

    def draw(self,surface):
        pygame.draw.rect(surface,(255,255,0),self.rect)
        self.image.draw(self.rect.x-200,self.rect.y-160,surface,self.flip)