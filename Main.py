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
from Intro import *

score = 0
current_level = 0
difficulty = 10
bullet_speed = 5
enemies_speed = math.sqrt(10 + current_level)
boss_health = 5 + current_level
start_time = time.time()
pause_time = 0
pause_start_time=time.time()
alive = True
pause = False
flag = True
background_y = 0

screen_width = 500
screen_height = 800
FPS = 120

# initialize pygame and creat window
pygame.init()
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Ragnarok The Game")
clock = pygame.time.Clock()

#background music
pygame.mixer.Channel(0).play(pygame.mixer.Sound('Arcade Funk.ogg'),-1)
pygame.mixer.Channel(0).set_volume(0.5)

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

#Spawning enemies
def spawn_enemy(speed):
    health = int(current_level / difficulty) + 1
    for i in range (5):
        enemy = Enemy(enemy_image, speed, health, [enemy_list, mob_list, sprites_list])
        enemy.rect.x = 10 + 100*i
        enemy.rect.y = -50

def spawn_power_ups(speed):
    power_up = PowerUp(screen_width, screen_height, speed, [power_up_list, sprites_list])
    power_up.rect.x = random.randrange(0, screen_width - power_up.rect.width)
    power_up.rect.y = -200

def spawn_meteor(speed):
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('comet.ogg'))
    pygame.mixer.Channel(2).set_volume(0.8)
    meteor = Meteor(pygame.transform.scale(meteor_image,(80,80)), speed, 0, [enemy_list, meteor_list, sprites_list])
    meteor.rect.y = -200
    meteor.rect.x = random.randrange(0, screen_width - meteor.rect.width)

def spawn_boss(speed):
    boss = Boss(screen_width, boss_image, speed, boss_health, [boss_list, sprites_list])
    boss.rect.x = screen_width/2 - boss.rect.width/2
    boss.rect.y = 50

def fire_bullet():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('laser.ogg'))
    pygame.mixer.Channel(1).set_volume(0.2)
    bullet = Bullet((player.rect.x + ship_image.get_rect().width/2), player.rect.y, bullet_speed, [sprites_list, bullet_list])
    pygame.time.set_timer(fire_bullet_event, fire_bullet_delay)


# -------- Intro Screen -----------
intro = Intro(screen, menu_background,screen_width,screen_height,title, start_button_image, about_button_image, back_button_image)
intro.show_intro(screen)
        
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
                intro.show_intro(screen)
                player = PlayerShip(screen_width,screen_height,ship_image, [sprites_list])
                #update highscore when you press r
                f = open('highscore.txt', 'w')
                f.write(str(highscore))
                f.close()
            if event.key == pygame.K_n and (not alive):
                #update highscore when you press n
                f = open('highscore.txt', 'w')
                f.write(str(highscore))
                f.close()
                done = True
            if event.key == pygame.K_ESCAPE and alive:
                if not pause:
                    temp_speed = [enemies_speed, bullet_speed]
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
        # player colliding with enemy
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
        for hit in enemy_hit_list:
            pygame.mixer.Channel(4).play(pygame.mixer.Sound('killed.ogg'))
            pygame.mixer.Channel(4).play(pygame.mixer.Sound('killed_explo.ogg'))
            if score > highscore:
                highscore = score
            alive = False

        #Increase speed of bullets if get power up
        power_up_hit_list = pygame.sprite.spritecollide(player, power_up_list, False)
        for hit in power_up_hit_list:
            hit.kill()
            if fire_bullet_delay >= 150:
                fire_bullet_delay -= 50

        for bullet in bullet_list:
            enemies_hit_list = pygame.sprite.spritecollide(bullet, mob_list, False)
            for enemy in enemies_hit_list:
                enemy.health -= 1
                bullet.kill()
                if enemy.health <= 0:
                    enemy.kill()
                    score += 1
                    pygame.mixer.Channel(3).play(pygame.mixer.Sound('explo.ogg'))
                    pygame.mixer.Channel(3).set_volume(0.5)

            boss_hit_list = pygame.sprite.spritecollide(bullet, boss_list, False)
            for boss in boss_hit_list:
                 boss.health -= 1
                 bullet.kill()
                 if boss.health <= 0:
                     boss.kill()
                     current_level += 1
                     score += 100
                        
            #if bullet goes off screen
            if bullet.rect.y < -10:
                bullet.kill()

        #Kill bullet if it hits meteors
        for meteor in meteor_list:
            meteor_hit_list = pygame.sprite.spritecollide(meteor, bullet_list, True)

       #Spawn enemies if there aren't any, levels and speeds fix later
        if not mob_list and not boss_list:
            if current_level % 5 != 0 or current_level == 0:
                spawn_enemy(enemies_speed)
                current_level += 1
            else:
                spawn_boss(0)

        #Spawn power ups
        if not power_up_list:
            if random.randint(0,100) < 2:
                spawn_power_ups(enemies_speed * 1.5)

        #Spawn meteor:
        if not meteor_list:
            if current_level % 3 == 0:
                spawn_meteor(enemies_speed * 2)

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
