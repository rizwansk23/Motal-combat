import pygame
pygame.init()

class animation:
    def __init__(self,character,action,step):
        self.character_sheet = pygame.image.load(f'assets/images/{character}/Sprites/{action}.png').convert_alpha()
        self.animation_list = []
        self.animation_step = step #13
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0

        for x in range(self.animation_step):
            self.animation_list.append(self.get_image(self.character_sheet,x,140,140,4))


    def get_image(self,sheet,frame,width,height,scale):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(sheet,(0,0),(width * frame,0,width,height))
        image= pygame.transform.scale(image,(width*scale,height*scale))
        image.set_colorkey((0,0,0))
        
        return image
    
    def draw(self,screen):

        screen.fill((202, 228, 241))

        current_time = pygame.time.get_ticks()

        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time

            if self.frame >= len(self.animation_list):
                self.frame = 0

        screen.blit(self.animation_list[self.frame],(0,0))
