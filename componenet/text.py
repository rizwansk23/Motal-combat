import pygame



class draw_text:
    def __init__(self,text, x, y,screen):
        #define fonts
        font = pygame.font.SysFont("arialblack", 40)

        #define colours
        TEXT_COL = (0,0,0)


        img = font.render(text, True,TEXT_COL)
        # img = pygame.transform.scale(img,(2*scale,2*scale))
        screen.blit(img, (x, y))