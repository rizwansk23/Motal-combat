import pygame
import animation 

pygame.init()

class Fighter:
    def __init__(self,x,y,flip,character_name,actions,steps,size,offset,scale):
        self.x = x
        self.y = y
        self.character_name = character_name
        self.actions = actions
        self.steps = steps
        self.size = size
        self.offset = offset
        self.scale = scale
        self.cooldown = 100
        self.i = 0
        self.last_i = self.i
        self.flip = flip
        self.rect = pygame.Rect(x,y,100,180)
        self.image = animation.animation(self.character_name,self.actions[self.i],self.size,self.size,self.steps[self.i],self.scale,self.cooldown)
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_cooldown = 0
        self.attack_type = False
        self.attack_active = False
        self.health = 100
        self.running = False
        self.alive = True
        self.hit = False
        self.time = 0
        self.a = 0

    def move(self,screen_width,screen_height,surface,target):

        SPEED = 5
        GRAVITY = 2

        dx = 0
        dy = 0

        # keyboard input 
        key = pygame.key.get_pressed()
        
        if self.attacking == False and self.alive == True:
            # moving 
            if key[pygame.K_d]:
                dx = SPEED
                self.running = True
            elif key[pygame.K_a]:
                dx = -SPEED
                self.running = True
            else:
                self.running= False

            # jump
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -25
                self.jump= True
                self.running = False

          # attack
            if key[pygame.K_r]  or key[pygame.K_t]:
                if key[pygame.K_r]:
                    if self.character_name == 'Evil Wizard 3':
                        self.a = 1
                        self.start_attack()
                        self.attack_type = 1
                    else:
                        if self.character_name == 'Hero Knight':
                            self.attack_type = 1
                            self.attack(target,0.8)
                        else:
                            self.attack_type = 1
                            self.attack(target)

                if key[pygame.K_t]:
                    if self.character_name == 'Evil Wizard 3':
                        self.a = 2
                        self.attack_type = 2
                        self.start_attack()
                    else:
                        self.attack_type = 2
                        self.attack(target)

            if key[pygame.K_m]:
                if self.character_name in ['Huntress','Martial Hero 3','warrior']:
                    if self.character_name == 'Huntress':
                        self.attack_type = 3
                        self.a = 3
                        self.start_attack()
                    else:
                        self.attack_type = 3
                        self.attack(target)
            
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

            #apply attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1


        self.rect.x += dx
        self.rect.y += dy


    def update_animation(self,screen):
        
        if self.health <= 0:#death
            self.health = 0
            self.alive = False
            if self.character_name == 'Evil Wizard 3':
                self.i = 5
                self.cooldown = 150
            else:
                self.i = 6
                self.cooldown = 150
        elif self.hit:#hit
            if self.character_name == 'Evil Wizard 3':
                self.i = 4
                self.cooldown = 220
            else:
                self.i = 5
                self.cooldown = 220
            self.attack_cooldown = 30
        elif self.attacking or self.attack_active:#attack
            if self.attack_type == 1:
                self.i = 3
                self.cooldown = 130
            elif self.attack_type == 2:
                if self.character_name == 'Evil Wizard 3':
                    self.i = 3
                else:
                    self.i = 4 
                    self.cooldown = 130
            # special attcak
            elif self.attack_type == 3:
                if self.character_name == 'Huntress':
                    self.i = 7
                    self.cooldown = 170
                else:
                    self.i = 7
                    self.cooldown = 50
        elif self.running == True:#running
            self.i = 1
        elif self.jump == True:#jump
            self.i = 2 
        else:
            self.i = 0
            self.cooldown = 100

 
        # IF ACTION CHANGED => RELOAD ANIMATION
        if self.i != self.last_i:
            self.image = animation.animation(self.character_name,self.actions[self.i],self.size, self.size,self.steps[self.i],self.scale,self.cooldown)
            self.last_i = self.i

        # Attack animation finished
        if self.i in [3,4,7]  and self.image.frame == self.image.animation_step - 1:
            self.attacking = False
            self.attack_cooldown = 20
            # self.hit = False

        # check death animation run one time 
        if self.alive == False:
            img = pygame.image.load('assets/images/icons/defeat.png')
            img = pygame.transform.scale(img,(50*12,10*12))
            screen.blit(img,(110,100)) 
            if self.image.frame == len(self.image.animation_list) - 1:
                self.image = animation.animation(self.character_name,self.actions[self.i],self.size, self.size,self.steps[self.i],self.scale,100)
                self.image.frame = len(self.image.animation_list) - 1

        if self.i in [4,5] and self.image.frame == self.image.animation_step - 1:
            self.hit = False


    def attack(self, target,Range = 1.8,damage = 10):
        if self.attack_cooldown == 0:

            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip),self.rect.y,Range * self.rect.width,self.rect.height)            
            
            if attacking_rect.colliderect(target.rect):
                target.health -= damage
                target.hit = True

            self.attacking = True 

    def start_attack(self):
        if not self.attack_active:
            direction = -1 if self.flip else 1

            self.attack_rect = pygame.Rect(self.rect.centerx + (20 * direction),self.rect.centery - 55,50, 20)

            self.attack_speed = 10 * direction
            self.attack_active = True
            self.last_time = pygame.time.get_ticks()
            

            if self.a == 1:
                # Load projectile animation only ONCE ❗
                self.attack_img = animation.animation("Evil Wizard 3","Explode",50, 50,7,3.5,10)
                self.arrowx = 60
            elif self.a == 2:
                self.attack_img = animation.animation("Evil Wizard 3","Moving",50, 50,4,3.5,140)
                self.arrowx = 30
            elif self.a == 3:
                self.attack_img = animation.animation("Huntress","Spear move",60, 20,4,3.5,100)
                self.arrowx = 30



            # projectile position
            self.attack_x = self.attack_rect.x
            self.attack_y = self.attack_rect.y


    def update_attack(self, surface, target):
        if not self.attack_active:
            return

        current_time = pygame.time.get_ticks()

        # Start movement after 1 second delay
        if current_time - self.last_time >= 1000:

            # Move projectile
            self.attack_x += self.attack_speed
            self.attack_rect.x += self.attack_speed

            if self.attack_img:
            # Draw projectile animation
                self.attack_img.draw(self.attack_x,self.rect.y - self.arrowx,surface,False) #30 for huntress and 60 for wizard

        # Collision
        if self.attack_rect.colliderect(target.rect):
            target.health -= 10
            self.attack_active = False

        # Out of screen
        if self.attack_rect.left > surface.get_width() or self.attack_rect.right < 0:
            self.attack_active = False
            self.attack_rect = None
            self.attack_img = None

            
    def draw(self,surface):
        # pygame.draw.rect(surface,(255,255,0),self.rect)
        self.image.draw(self.rect.x- self.offset[0],self.rect.y- self.offset[1],surface,self.flip)

