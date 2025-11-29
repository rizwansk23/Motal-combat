import pygame
import time
from fighter import Fighter
import random

class Enemy(Fighter):

    def __init__(self, x, y,flip, character_name, actions, steps,size,offset,scale):
        super().__init__(x, y,flip, character_name, actions, steps,size,offset,scale)

        self.speed = 5               # AI movement speed
        self.counter = 0
        self.health = 100

        self.last_time = pygame.time.get_ticks()      


    def ai_move(self,screen_width,target):


        dx = 0
        dy = 0
        self.can_move = False

        #find the distance of player and enemey
        distance_x = target.rect.centerx - self.rect.centerx
        abs_dist = abs(distance_x)

        current_time = pygame.time.get_ticks()

        # --- Timer 4 sec wait ---
        if self.counter == 0:
            if current_time - self.last_time >= 3000:  # 3 second
                self.counter += 1
                self.last_time = current_time

        if self.counter in [1,2,3,4]:
            if current_time - self.last_time >= 500:  # half second
                self.counter -= 1
                self.last_time = current_time   
                if self.counter == 0:
                    self.counter = 0
            self.can_move = True
        else:
            self.can_move = False


        # move enemey
        if self.can_move:      
            if abs_dist >= 100 and self.alive:
                if self.flip:
                    dx = -self.speed
                else:
                    dx = self.speed
                self.running = True
        else:
            self.running = False



      

        # attacking 
        if target.alive and self.alive:
            if abs_dist <= 200 and self.attack_cooldown == 0 and not self.attacking:

                if self.character_name  == 'warrior':
                    self.attack_type = random.choice([1,2,3])
                    if target.health < 20:
                        self.attack_type = 3
                else:
                    self.attack_type = random.choice([1,2])

                
                if self.attack_type == 1:
                    self.attack(target,8,10)
                    if self.attacking:
                        self.attack_cooldown = 100

                elif self.attack_type == 2 or self.attack_type == 3:
                    self.attack(target,1.8,10)
                    if self.attacking:
                        self.attack_cooldown = 100
                
                self.attack_cooldown = 50


        # ensure player face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True
        
        #apply attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1


        if self.rect.left + dx <= 0:
            dx = -self.rect.left
        if self.rect.right + dx >= screen_width:
            dx = screen_width - self.rect.right

        
        self.rect.x += dx
        self.rect.y += dy

        self.can_move = False



