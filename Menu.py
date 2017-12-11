import pygame
from Constants import *

class Menu:
    def __init__(self):
        self.mid_x = SCREEN_WIDTH/2
        self.mid_y = SCREEN_HEIGHT/2

    def displayMenu(self, screen, menu, score = 0, highscore = 0):
    #menua = Instro
    #menub = Pause
    #menuc = Game Over
        gp_width = pygame.font.SysFont(FONT, 70, True) .size("Game Paused")[0]
        res_width = pygame.font.SysFont(FONT, 30, True).size("Press Escape to resume")[0]
        r_width = pygame.font.SysFont(FONT, 30, True).size("Press R to go to main menu")[0]
        go_width = pygame.font.SysFont(FONT, 70, True) .size("Game Over")[0]
        r2_width = pygame.font.SysFont(FONT, 30, True).size("Press R to go to main menu")[0]
        n_width = pygame.font.SysFont(FONT, 30, True).size("Press N to quit")[0]
        s_width = pygame.font.SysFont(FONT, 30, True).size("Score")[0]
        s_string_width = pygame.font.SysFont(FONT, 70, True) .size(str(score))[0]
        b_width = pygame.font.SysFont(FONT, 30, True).size("Best")[0]
        b_string_width = pygame.font.SysFont(FONT, 70, True).size(str(highscore))[0]

        if menu == "b":
            screen.blit(pygame.font.SysFont(FONT, 70, True).render("Game Paused", 1, BLUE), (self.mid_x - gp_width/2 ,self.mid_y/2 ))
            screen.blit(pygame.font.SysFont(FONT, 30, True).render("Press Escape to resume", 1, BLUE), (self.mid_x - (res_width/2), self.mid_y-40))
            screen.blit(pygame.font.SysFont(FONT, 30, True).render("Press R to go to main menu", 1, BLUE), (self.mid_x - (r_width/2), self.mid_y))
        elif menu == "c":
            screen.blit(pygame.font.SysFont(FONT, 70, True).render("Game Over", 1, BLUE), (self.mid_x - go_width/2, self.mid_y/2))
            screen.blit(pygame.font.SysFont(FONT, 30, True).render("Press R to go to main menu", 1, BLUE), (self.mid_x - (r2_width/2), self.mid_y-60))
            screen.blit(pygame.font.SysFont(FONT, 30, True).render("Press N to quit", 1, BLUE), (self.mid_x - n_width/2, self.mid_y-20))
            screen.blit(pygame.font.SysFont(FONT, 30, True).render("Score", 1, BLUE), (self.mid_x/2 - s_width/2, self.mid_y+30))
            screen.blit(pygame.font.SysFont(FONT, 30, True).render("Best", 1, BLUE), (self.mid_x*3/2 - b_width/2, self.mid_y+30))
            if score >= highscore:
                screen.blit(pygame.font.SysFont(FONT, 70, True).render(str(score), 1, RED), (self.mid_x/2 - s_string_width/2, self.mid_y+50))
                screen.blit(pygame.font.SysFont(FONT, 70, True).render(str(highscore), 1, RED), (self.mid_x*3/2 - b_string_width/2, self.mid_y+50))
            else:
                screen.blit(pygame.font.SysFont(FONT, 70, True).render(str(score), 1, BLUE), (self.mid_x/2 - s_string_width/2, self.mid_y+50))
                screen.blit(pygame.font.SysFont(FONT, 70, True).render(str(highscore), 1, BLUE), (self.mid_x*3/2 - b_string_width/2, self.mid_y+50))
