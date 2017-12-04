import pygame

class Menu(object):


    def displayMenu(self , screen, menu, score = 0):
    #menua = Instruction
    #menub = Pause
    #menuc = Game Over
        if menu == "b":
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render("Game Paused", 1, (91, 109, 131)), (50, 200))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Press ELSE to resume", 1, (91, 109, 131)), (170, 370))
        elif menu == "c":
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render("Game Over", 1, (91, 109, 131)), (105, 300))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Press R to go to main menu", 1, (91, 109, 131)), (170, 370))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Press N to quit", 1, (91, 109, 131)), (170, 390))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Score", 1, (91, 109, 131)), (230, 440))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render(str(score), 1, (91, 109, 131)), (230, 460))

