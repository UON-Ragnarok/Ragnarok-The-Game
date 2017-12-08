import pygame

class Menu(object):
    #def __init__(self,x,y):
        #self.x=x
        #self.y=y

    def displayMenu(self , screen, menu, score = 0, highscore = 0):
    #menua = Instruction
    #menub = Pause
    #menuc = Game Over

        
        #myFont = pygame.font.Font(pygame.font.SysFont("'freesansbold.ttf'", 50, True))
        
        #gp_width=myFont.size("Game Paused")[0]
        #res_width=myFont.size("Press Escape to resume")[0]
        #go_width=myFont.size("Game Over")[0]
        #r_width=myFont.size(go_width=myFont.size("Press R to go to main menu"))[0]
        #n_width=myFont.size(go_width=myFont.size("Press N to quit")[0]
        #s_w=myFont.size(go_width=myFont.size("Score")[0]
        #b_width=myFont.size(go_width=myFont.size("Best")[0]idt
                         
        if menu == "b":
            
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render("Game Paused", 1, (91, 109, 131)), (50, 200))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Press Escape to resume", 1, (91, 109, 131)), (170, 370))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Press R to go to main menu", 1, (91, 109, 131)), (170, 390))
        elif menu == "c":
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render("Game Over", 1, (91, 109, 131)), (105, 300))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Press R to go to main menu", 1, (91, 109, 131)), (170, 370))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Press N to quit", 1, (91, 109, 131)), (170, 390))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Score", 1, (91, 109, 131)), (170, 440))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render(str(score), 1, (91, 109, 131)), (170, 460))     
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Best", 1, (91, 109, 131)), (300, 440))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render(str(highscore), 1, (91, 109, 131)), (300, 460))  
