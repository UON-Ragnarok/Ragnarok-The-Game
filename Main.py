import pygame
import random
import time
import math

from PlayerShip import *
from Bullet import *
from Enemy import *
from Menu import *

pygame.init()

screen_width = 500
screen_height = 800
screen = pygame.display.set_mode([screen_width,screen_height])

score = 0
current_level = 0
enemies_speed = math.sqrt(10 + current_level)
boss_health = 20 + current_level
start_time = time.time()
pause_time = 0
pause_start_time=time.time()
alive = True
pause = False
intro = True

background = pygame.image.load('img/background.jpg').convert()
ship_image = pygame.image.load('img/spaceship.png').convert()
boss_image = pygame.image.load('img/thor.png').convert()
enemy_image = pygame.image.load('img/mob.png').convert()
meteor_image = pygame.image.load('img/meteor.png').convert()

start_button_image = pygame.image.load('img/start_button.png').convert()
about_button_image = pygame.image.load('img/about_button.png').convert()

background_y = 0
pygame.display.set_caption("My Game")

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

#List of meteor
meteor_list = pygame.sprite.Group()

#Creating sprites
player = PlayerShip(screen_width, ship_image)
sprites_list.add(player)

clock = pygame.time.Clock()
FPS = 120

#Setting up firing bullet delay
fire_bullet_event = pygame.USEREVENT + 1
fire_bullet_delay = 300
pygame.time.set_timer(fire_bullet_event, 500)

player.rect.y = (screen_height - player.rect.height)*0.95

pygame.mixer.Channel(0).play(pygame.mixer.Sound('Arcade Funk.ogg'))
pygame.mixer.Channel(0).set_volume(0.5)
#Spawning enemies

def spawn_enemy(speed):
    for i in range (6):
        enemy = Enemy(enemy_image, speed, 0, [enemy_list, mob_list, sprites_list])
        enemy.rect.x = 25 + 80*i
        enemy.rect.y = -50

def spawn_meteor(speed):
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('comet.ogg'))
    pygame.mixer.Channel(2).set_volume(0.8)
    meteor = Meteor(pygame.transform.scale(meteor_image,(50,50)), speed, 0, [enemy_list, meteor_list, sprites_list])
    meteor.rect.y = -200
    meteor.rect.x = random.randrange(0, screen_width - meteor.rect.width)
# trying to make it move dignoally but it will then need a speedx

def spawn_boss(speed):
    boss = Boss(boss_image, speed, 0, [boss_list, sprites_list])
    boss.rect.x = screen_width/2-boss.rect.width/2
    boss.rect.y = 50

def fire_bullet():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('laser.ogg'))
    pygame.mixer.Channel(1).set_volume(0.2)
    bullet = Bullet((player.rect.x + ship_image.get_rect().width/2),player.rect.y,[sprites_list, bullet_list])
    pygame.time.set_timer(fire_bullet_event, fire_bullet_delay)


# main menu
# set up the height and width
sb_top_left_x=screen_width/2 - start_button_image.get_rect().width/2
sb_top_left_y=screen_height/2
sb_height=start_button_image.get_rect().height
sb_width=start_button_image.get_rect().width
ab_height=about_button_image.get_rect().height
ab_width=about_button_image.get_rect().width
about=False 


while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    # start button
    if sb_top_left_x <mouse[0]<sb_top_left_x+sb_width and sb_top_left_y <mouse[1]<sb_top_left_y +sb_height:
        screen.fill((0,0,0))
        screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render("Ragnorak", 1, (91, 109, 131)), (sb_top_left_x-20,sb_top_left_y -20-sb_height))
        big_start_button_image=pygame.transform.rotozoom(start_button_image,0,1.2)
        screen.blit(big_start_button_image, [sb_top_left_x, sb_top_left_y])
        screen.blit(about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
        pygame.display.flip()
        if click[0] == 1:
            intro = False
            break
    # about button
    elif sb_top_left_x <mouse[0]<sb_top_left_x+ab_width and sb_top_left_y +20+ab_height<mouse[1]<sb_top_left_y+20+sb_height+ab_height:
        screen.fill((0,0,0))
        screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render("Ragnorak", 1, (91, 109, 131)), (sb_top_left_x-20,sb_top_left_y -20-sb_height))
        big_about_button_image=pygame.transform.rotozoom(about_button_image,0,1.2)
        screen.blit(start_button_image, [sb_top_left_x, sb_top_left_y])
        screen.blit(big_about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
        pygame.display.flip()
        #if click[0]==1:
            #screen.fill((0,0,0))
            #screen.blit(start_button_image, [sb_top_left_x, sb_top_left_y]);
            #screen.blit(about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
            #pygame.display.flip()
            #while about ==True:
                #if sb_top_left_x <mouse[0]<sb_top_left_x+ab_width and sb_top_left_y +20+sb_height<mouse[1]<sb_top_left_y+20+sb_height+ab_height:
                    #screen.fill((0,0,0))
                    #big_about_button_image=pg.transform.rotozoom(about_button_image,0,1.2)
                    #screen.blit(big_about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height]);
                    #pygame.display.flip()
                    #if click[0] == 1:
                       # continue
               # else:
                    #screen.fill((0,0,0))
                    #screen.blit(start_button_image, [sb_top_left_x, sb_top_left_y]);
                    #screen.blit(about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
    else:
        screen.fill((0,0,0))
        screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 70, True).render("Ragnorak", 1, (91, 109, 131)), (sb_top_left_x-20,sb_top_left_y -20-sb_height))
        screen.blit(start_button_image, [sb_top_left_x, sb_top_left_y])
        screen.blit(about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
        pygame.display.flip()

done = False

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

        if alive and event.type == fire_bullet_event and not pause:
            fire_bullet()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and (not alive):
                score = 0
                alive = True
            if event.key == pygame.K_n and (not alive):
                done = True
            if event.key == pygame.K_ESCAPE and alive:
                if not pause:
                    temp_enemies_speed = enemies_speed
                    for enemy in enemy_list:
                        enemy.speed = 0
                    for bullet in bullet_list:
                        bullet.speed = 0
                    pause = True
                    player.pause = True
                    pause_start_time = time.time()
                else:
                    for enemy in enemy_list:
                        enemy.speed = temp_enemies_speed
                    for bullet in bullet_list:
                        bullet.speed = 5
                    pause = False
                    player.pause = False
                    pause_time += time.time() - pause_start_time
                    
    sprites_list.update()
    # --- Game mechanics

    if alive and not pause:
        # player colliding with enemy
        hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
        for hit in hit_list:
            alive= False
            pygame.mixer.Channel(4).play(pygame.mixer.Sound('killed.ogg'))

             
        for bullet in bullet_list:
            enemies_hit_list = pygame.sprite.spritecollide(bullet, mob_list, True)
            for enemies in enemies_hit_list:
                score += 1
                bullet.kill()
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('explo.ogg'))
                pygame.mixer.Channel(3).set_volume(0.5)               

            #if bullet goes off screen
            if bullet.rect.y < -10:
                bullet.kill()

        #Kill bullet if it hits meteors
        for meteor in meteor_list:
            meteor_hit_list = pygame.sprite.spritecollide(meteor, bullet_list, True)

        #Spawn enemies if there aren't any, levels and speeds fix later
        if not mob_list and score < 5000:
            spawn_enemy(enemies_speed)
            current_level += 1

        for enemy in enemy_list:
            #If enemies go off screen
            if enemy.rect.y > screen_height:
                enemy.kill()

        screen.blit(pygame.font.SysFont("'freesansbold.ttf", 60, True).render(str(score), 1, (91, 109, 131)), (screen_width-100,50 ))

        #Spawn meteor:
        if not meteor_list:
            if current_level % 3 == 0:
                spawn_meteor(enemies_speed * 2)

        #Spawn boss:
        if not enemy_list and score >= 1000:
            spawn_boss(0)

    if not alive:
       # sprites_list.remove(player)
        screen.fill((0,0,0))
        Menu().displayMenu(screen,"c",score)
        current_level=0
        for sprite in enemy_list:
            sprite.kill()
    elif pause :
        Menu().displayMenu(screen, "b")

    sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

# Close the window and quit.
pygame.quit()
