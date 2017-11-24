import pygame

class Menu(object):
    def displayMenu(self , screen, menu, score = 0):
    #menua = Instruction
    #menub = Pause
    #menuc = Game Over
        if menu =='a':
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render("Instructions", 1, (91, 109, 131)), (50, 200))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("DESTROY ASGARD", 1, (91, 109, 131)), (170, 370))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Mouse to move and click to shoot", 1, (91, 109, 131)), (140, 390))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Esc to pause", 1, (91, 109, 131)), (170, 410))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Press any key to start", 1, (91, 109, 131)), (170, 430))
        elif menu == "b":
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render("Game Paused", 1, (91, 109, 131)), (50, 200))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Press ELSE to resume", 1, (91, 109, 131)), (170, 370))
        elif menu == "c":
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render("Game Over", 1, (91, 109, 131)), (105, 300))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Press R to restart", 1, (91, 109, 131)), (170, 370))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Press N to quit", 1, (91, 109, 131)), (170, 390))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Score", 1, (91, 109, 131)), (230, 440))
            screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render(str(score), 1, (91, 109, 131)), (230, 460))

