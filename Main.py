import pygame
import random
import time

from PlayerShip import *
from Bullet import *
from Enemy import *
from Menu import *

pygame.init()

screen_width = 500
screen_height = 800
screen = pygame.display.set_mode([screen_width,screen_height])

background = pygame.image.load('img/background.jpg').convert()
ship_image = pygame.image.load('img/spaceship.png').convert()
enemy_image = pygame.image.load('img/enemy.png').convert()

pygame.display.set_caption("My Game")

#List of all sprites
sprites_list = pygame.sprite.Group()

#List of bullets
bullet_list = pygame.sprite.Group()

#List of enemies
enemies_list = pygame.sprite.Group()

alive = True    
pause = False
current_level = 0
score = 0


#Spawning enemies

def spawn_enemy(speed):
    for i in range (6):
        enemy = Enemy(enemy_image, speed)
        enemy.rect.x = 25 + 80*i
        enemy.rect.y = -50
        enemies_list.add(enemy)
        sprites_list.add(enemy)
<<<<<<< HEAD
        
done = False

clock = pygame.time.Clock()
player.rect.y = 700


# -------- Main Program Loop -----------
while not done:

    # --- Looping the background
    relative_y = background_y % background.get_rect().height
    screen.blit(background, [0, relative_y - background.get_rect().height])
    if relative_y < screen_height:
        screen.blit(background, [0, relative_y])
    background_y += 1
        
    # --- Main event loop
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        
        if event.type == pygame.MOUSEBUTTONDOWN and alive:
            bullet = Bullet()
            bullet.rect.x = player.rect.x + ship_image.get_rect().width/2
            bullet.rect.y = player.rect.y
            sprites_list.add(bullet)
            bullet_list.add(bullet)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and (not alive):
                alive = True
            if event.key == pygame.K_n and (not alive):
                done = True
            if event.key == pygame.K_ESCAPE and alive:
                if pause:

                    pause = False
                    pause_time += time.time() - pause_start_time

                else:
                    for enemy in enemies_list:
                        enemies_list.remove(enemy)
                        sprites_list.remove(enemy)
                    pause = True
                    pause_start_time = time.time()

                    
    sprites_list.update()
    # --- Game mechanics

    if alive and (not pause):
        # player colliding with enemy
        hit_list = pygame.sprite.spritecollide(player, enemies_list, True)
        for hit in hit_list:
             alive= False
             
        for bullet in bullet_list:
            enemies_hit_list = pygame.sprite.spritecollide(bullet, enemies_list, True)
            for enemies in enemies_hit_list:
                score += 1
                bullet_list.remove(bullet)
                sprites_list.remove(bullet)

            #if bullet goes off screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                sprites_list.remove(bullet)

        #Spawn enemies if there aren't any, levels and speeds fix later
        if not enemies_list:
            spawn_enemy(2 + current_level)
            current_level += 0.5

        for enemy in enemies_list:
            #If enemies go off screen

            if enemy.rect.y > screen_height:
=======
#Reset flags and variables
def reset_game():
    global alive 
    global pause
    global current_level
    global score

    alive = True
    pause = False
    current_level = 0
    score = 0
    
def game():

    global background_y
    global alive 
    global pause
    global current_level
    global score
    
    #Creating sprites
    player = PlayerShip(screen_width, ship_image)
    player.rect.y = 700
    sprites_list.add(player)
    
    done = False

    clock = pygame.time.Clock()
    

    background_y = 0
    # -------- Main Program Loop -----------
    while not done:

        # --- Looping the background
        relative_y = background_y % background.get_rect().height
        screen.blit(background, [0, relative_y - background.get_rect().height])
        if relative_y < screen_height:
            screen.blit(background, [0, relative_y])
        background_y += 1

        # --- Main event loop
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN and alive:
                bullet = Bullet()
                bullet.rect.x = player.rect.x + ship_image.get_rect().width/2
                bullet.rect.y = player.rect.y
                sprites_list.add(bullet)
                bullet_list.add(bullet)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and (not alive):
                    reset_game()
                    #Creating sprites
                    player = PlayerShip(screen_width, ship_image)
                    player.rect.y = 700
                    sprites_list.add(player)
                if event.key == pygame.K_n and (not alive):
                    done = True
                if event.key == pygame.K_ESCAPE and alive:
                    if pause:
                        pause = False
                        pause_time += time.time() - pause_start_time
                    else:
                        pause = True
                        pause_start_time = time.time()
                        
        sprites_list.update()
        # --- Game mechanics

        if alive and (not pause):
            # player colliding with enemy
            hit_list = pygame.sprite.spritecollide(player, enemies_list, True)
            for hit in hit_list:
                 alive= False
                 
            for bullet in bullet_list:
                enemies_hit_list = pygame.sprite.spritecollide(bullet, enemies_list, True)
                for enemies in enemies_hit_list:
                    score += 1
                    bullet_list.remove(bullet)
                    sprites_list.remove(bullet)

                #if bullet goes off screen
                if bullet.rect.y < -10:
                    bullet_list.remove(bullet)
                    sprites_list.remove(bullet)

            #Spawn enemies if there aren't any, levels and speeds fix later
            if not enemies_list:
                spawn_enemy(2 + current_level)
                current_level += 0.5

            for enemy in enemies_list:
                #If enemies go off screen

                if enemy.rect.y > screen_height:
                    enemies_list.remove(enemy)
                    sprites_list.remove(enemy)


            screen.blit(pygame.font.SysFont("'freesansbold.ttf", 60, True).render(str(score), 1, (91, 109, 131)), (screen_width-100,50 ))

        # remove enemies, player and display score
        if not alive:
            sprites_list.remove(player)
            for enemy in enemies_list:
>>>>>>> a3326c09c23bd1f934aeed34d9a7af272c01e8b5
                enemies_list.remove(enemy)
                sprites_list.remove(enemy)
            screen.fill((0,0,0))
            Menu().displayMenu(screen,"gameover",score)
            current_level=0
        elif pause :
            Menu().displayMenu(screen, "pause")

        sprites_list.draw(screen)

        pygame.display.flip()

        clock.tick(120)

    # Close the window and quit.
    pygame.quit()
    
# The "about " in the menu
def aboutMenu():
    menuTitle = Menu(
        ["Ragnorik"])

    info = Menu(
        [""],
        ["Use mouse to move your ship and left click to shoot."],
        [""],
        ["       PRESS ESC TO PAUSE and RETURN          "])

    #the colour and type of the pont in "about"
    menuTitle.set_font(pygame.font.SysFont("'freesansbold.ttf'", 70, True))
    menuTitle.center_at(250, 300)
    menuTitle.set_highlight_color((255, 255, 255))

    info.center_at(250, 400)
    info.set_highlight_color((255, 255, 255))
    info.set_normal_color((200, 200, 255))

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)

        #Handle input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
            elif event.type == pygame.QUIT:
                keepGoing = False

        #Draw
        screen.blit(background, (0,0))
        menuTitle.draw(screen)
        info.draw(screen)
        pygame.display.flip()
        
#Functions
def option1():
    game()
def option2():
    aboutMenu()
def option3():
    pygame.quit()

    
def main():
    menuTitle = Menu(
        ["Ragnorik"])

    menu = Menu(
        ["Start", option1],
        ["About", option2],
        ["Exit", option3])

    #Title
    menuTitle.set_font(pygame.font.SysFont("'freesansbold.ttf'", 70, True))
    menuTitle.center_at(250, 150)
    menuTitle.set_highlight_color((255, 255, 255))

    #Menu settings
    menu.center_at(250, 320)
    menu.set_highlight_color((255, 255, 255))
    menu.set_normal_color((200, 200, 255))

    clock = pygame.time.Clock()
    keepGoing = True

    while True:
        clock.tick(30)

        #Events
        events = pygame.event.get()

        #Update Menu
        menu.update(events)

        #Handle quit event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
                return

        #Draw
        screen.blit(background, (0, 0))
        menu.draw(screen)
        menuTitle.draw(screen)

        pygame.display.flip() 


main()
