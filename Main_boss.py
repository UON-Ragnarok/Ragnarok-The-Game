import pygame
import random
import time
import math

from PlayerShip import *
from Bullet import *
from Enemy import *
from Bosses import *
from Menu import *
from PowerUp import *

score = 0
current_level = 0
difficulty = 10
bullet_speed = 5
enemies_speed = math.sqrt(10 + current_level)
boss_health = 10
start_time = time.time()
pause_time = 0
pause_start_time=time.time()
alive = True
pause = False
flag = True
background_y = 0

screen_width = 500
screen_height = 800
FPS = 60

# initialize pygame and creat window
pygame.init()
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Ragnarok The Game")
clock = pygame.time.Clock()

background = pygame.image.load('img/background.jpg').convert()
menu_background = pygame.image.load('img/main_menu_bg.jpg').convert()
title = pygame.image.load('img/Ragnarok_logo.png').convert_alpha()
ship_image = pygame.image.load('img/spaceship.png').convert_alpha()
boss_image = pygame.image.load('img/thor.png').convert()
enemy_image = pygame.image.load('img/mob.png').convert_alpha()
meteor_image = pygame.image.load('img/meteor.png').convert_alpha()

start_button_image = pygame.image.load('img/start_button.png').convert()
about_button_image = pygame.image.load('img/about_button.png').convert()
back_button_image = pygame.image.load('img/back_button.png').convert()

#List of all sprites
sprites_list = pygame.sprite.Group()

#List of bullets
bullet_list = pygame.sprite.Group()

#BOSS
boss_list = pygame.sprite.Group()

#List of all enemies
enemy_list = pygame.sprite.Group()

#List of mobs
mob_list = pygame.sprite.Group()

#List of PowerUps
power_up_list = pygame.sprite.Group()

#List of meteor
meteor_list = pygame.sprite.Group()

#Creating sprites
player = PlayerShip(screen_width, screen_height,ship_image, [sprites_list])

#Setting up firing bullet delay
fire_bullet_event = pygame.USEREVENT + 1
fire_bullet_delay = 500
pygame.time.set_timer(fire_bullet_event, fire_bullet_delay)

# load the highscore
f = open('highscore.txt', 'r')
temp = f.read()
if temp != "":
    highscore = int(temp)
else:
    highscore = 0
f.close()

# main menu
# set up the height and width
sb_top_left_x = screen_width / 2 - start_button_image.get_rect().width / 2
sb_top_left_y = screen_height / 2
bb_top_left_x = screen_width / 2 - back_button_image.get_rect().width / 2
sb_height = start_button_image.get_rect().height
sb_width = start_button_image.get_rect().width
ab_height = about_button_image.get_rect().height
ab_width = about_button_image.get_rect().width
bb_height = back_button_image.get_rect().height
bb_width = back_button_image.get_rect().width


def spawn_boss(speed):
    boss = Boss(screen_width, boss_image, speed, boss_health, [boss_list, sprites_list])
    boss.rect.x = screen_width/2-boss.rect.width/2
    boss.rect.y = 50

def fire_bullet():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('laser.ogg'))
    pygame.mixer.Channel(1).set_volume(0.2)
    bullet = Bullet((player.rect.x + ship_image.get_rect().width/2), player.rect.y, bullet_speed, [sprites_list, bullet_list])
    pygame.time.set_timer(fire_bullet_event, fire_bullet_delay)


def intro():
    main = True
    about = False
    menu_background_x = 0
    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        pressedkeys = pygame.key.get_pressed()

        # --- Looping the background
        relative_x = menu_background_x % menu_background.get_rect().width
        screen.blit(menu_background, [relative_x - menu_background.get_rect().width, 0])
        if relative_x < screen_width:
            screen.blit(menu_background, [relative_x, 0])
        menu_background_x += -0.3

        screen.blit(title, [screen_width / 9, screen_height / 6])

        #mute
        if pressedkeys[pygame.K_m]:
            pygame.mixer.pause()
            #pygame.mixer.unpause()

            
        # start button
        if main and sb_top_left_x < mouse[0] < sb_top_left_x+sb_width and sb_top_left_y < mouse[1] < sb_top_left_y + sb_height:
            big_start_button_image = pygame.transform.rotozoom(start_button_image,0,1.2)
            screen.blit(big_start_button_image, [sb_top_left_x, sb_top_left_y])
            screen.blit(about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
            pygame.display.flip()
            if click[0] == 1:
                main = False
                break
        # about button
        elif main and sb_top_left_x < mouse[0] < sb_top_left_x+ab_width and sb_top_left_y + 20 + ab_height < mouse[1] < sb_top_left_y + 20 + sb_height+ab_height:
            big_about_button_image = pygame.transform.rotozoom(about_button_image,0,1.2)
            screen.blit(start_button_image, [sb_top_left_x, sb_top_left_y])
            screen.blit(big_about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
            pygame.display.flip()
            if click[0]==1:
                main = False
                about = True
        
        elif about and bb_top_left_x < mouse[0] < bb_top_left_x+bb_width and sb_top_left_y+200 < mouse[1] < sb_top_left_y+200 + bb_height:
            big_back_button_image = pygame.transform.rotozoom(back_button_image,0,1.2)
            screen.blit(big_back_button_image, [bb_top_left_x, sb_top_left_y + 200])
            pygame.display.flip()
            if click[0] == 1:
                main = True
                about = False
        else:
            if main:
                screen.blit(start_button_image, [sb_top_left_x, sb_top_left_y])
                screen.blit(about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
            elif about:
                screen.blit(back_button_image, [bb_top_left_x,sb_top_left_y+200 ]);
            pygame.display.flip()
        

        clock.tick(FPS)

intro()
done = False
boss_kill = False

# -------- Main Program Loop -----------
while not done:

    # --- Looping the background
    if not pause and alive:
        relative_y = background_y % background.get_rect().height
        screen.blit(background, [0, relative_y - background.get_rect().height])
        if relative_y < screen_height:
            screen.blit(background, [0, relative_y])
        background_y += 1

    # --- Main event loop
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #update highscore when you quit
            f = open('highscore.txt', 'w')
            f.write(str(highscore))
            f.close()
            done = True

        if alive and event.type == fire_bullet_event and not pause:
            fire_bullet()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and (not alive):
                score = 0 
                alive = True
                intro()
                player = PlayerShip(screen_width,screen_height,ship_image, [sprites_list])
                #update highscore when you die 
                f = open('highscore.txt', 'w')
                f.write(str(highscore))
                f.close()
            if event.key == pygame.K_n and (not alive):
                done = True
            if event.key == pygame.K_ESCAPE and alive:
                if not pause:
                    temp_speed = [enemies_speed, bullet_speed]
                    boss.speed = 0
                    for enemy in enemy_list:
                        enemy.speed = 0
                    for bullet in bullet_list:
                        bullet.speed = 0
                    for power_up in power_up_list:
                        power_up.speed = 0
                    pause = True
                    player.pause = True
                    pause_start_time = time.time()
                else:
                    for enemy in enemy_list:
                        enemy.speed = temp_speed[0]
                    for bullet in bullet_list:
                        bullet.speed = temp_speed[1]
                    for power_up in power_up_list:
                        power_up.speed = temp_speed[0] * 1.5
                    pause = False
                    player.pause = False
                    pause_time += time.time() - pause_start_time

    sprites_list.update()
    # --- Game mechanics

    if alive and not pause:

        if not boss_kill:
            spawn_boss(0)
        
        for bullet in bullet_list:

            boss_hit = pygame.sprite.spritecollide(bullet, boss_list, False)
            for boss in boss_hit:
                boss.health -= 1
                bullet.kill()
                if boss.health <= 0:
                    boss.kill()
                    score += 100
                    boss_kill = True
                        
            #if bullet goes off screen
            if bullet.rect.y < -10:
                bullet.kill()

        for sprite in sprites_list  :
            #If enemies go off screen
            if sprite.rect.y > screen_height:
                sprite.kill()

        screen.blit(pygame.font.SysFont("'freesansbold.ttf", 60, True).render(str(score), 1, (91, 109, 131)), (screen_width-100,50 ))

		
    #m = Menu(screen_width/2,screen_height/2)
    if not alive:
       # sprites_list.remove(player))
        Menu().displayMenu(screen,"c",score,highscore)
        current_level = 0
        for sprite in sprites_list:
            sprite.kill()
    elif pause :
        Menu().displayMenu(screen, "b")

    sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

# Close the window and quit.
pygame.quit()
