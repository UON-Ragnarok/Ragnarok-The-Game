import pygame
import random
import time
import pygame as pg

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
boss_health = 20 + current_level
#Pause
start_time = time.time()
pause_time = 0
pause_start_time=time.time()
alive = True
pause = False
intro = True


background = pygame.image.load('img/background.jpg').convert()
ship_image = pygame.image.load('img/spaceship.png').convert()
boss_image = pygame.image.load('img/thor.png').convert()
enemy_image = pygame.image.load('img/enemy.png').convert()
meteor_image = pygame.image.load('img/meteor.png').convert()
start_image = pygame.image.load('img/spaceship.png').convert()

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

#List of enemies
enemies_list = pygame.sprite.Group()

#List of meteor
meteor_list = pygame.sprite.Group()

#Creating sprites
player = PlayerShip(screen_width, ship_image)
sprites_list.add(player)

#Spawning enemies

def spawn_enemy(speed):
    for i in range (6):
        enemy = Mob(enemy_image, speed)
        enemy.rect.x = 25 + 80*i
        enemy.rect.y = -50
        enemies_list.add(enemy)
        sprites_list.add(enemy)

def spawn_meteor(speed):
    meteor = Meteor(pygame.transform.scale(meteor_image,(50,50)), speed)
    meteor.rect.x = random.choice([-meteor.rect.width/2,screen_width-meteor.rect.width/2])
    meteor.rect.y = random.randrange(-meteor.rect.height/2,40)
# trying to make it move dignoally but it will then need a speedx
    meteor_list.add(meteor)
    sprites_list.add(meteor)

def spawn_boss(speed):
    boss = Boss(boss_image, speed)
    boss.rect.x = screen_width/2-boss.rect.width/2
    boss.rect.y = 50
    boss_list.add(boss)
    sprites_list.add(boss)

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
        big_start_button_image=pg.transform.rotozoom(start_button_image,0,1.2)
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
        big_about_button_image=pg.transform.rotozoom(about_button_image,0,1.2)
        screen.blit(start_button_image, [sb_top_left_x, sb_top_left_y]);
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
        screen.blit(start_button_image, [sb_top_left_x, sb_top_left_y]);
        screen.blit(about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height]);
        pygame.display.flip()
done = False

clock = pygame.time.Clock()
player.rect.y = (screen_height - player.rect.height)*0.95

pygame.mixer.music.load('Arcade Funk.ogg')

pygame.mixer.music.play(loops=0, start=0.0)
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

        if alive:
            bullet = Bullet()
            bullet.rect.x = player.rect.x + ship_image.get_rect().width/2
            bullet.rect.y = player.rect.y
            sprites_list.add(bullet)
            bullet_list.add(bullet)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and (not alive):
                score = 0
                alive = True
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

    if alive and not pause:
        # player colliding with enemy
        hit_list = pygame.sprite.spritecollide(player, enemies_list, True) or pygame.sprite.spritecollide(player, meteor_list, True)
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
        if not enemies_list and score < 5:
            spawn_enemy(2 + current_level)
            current_level += 0.2

        for enemy in enemies_list:
            #If enemies go off screen
            if enemy.rect.y > screen_height:
                enemies_list.remove(enemy)
                sprites_list.remove(enemy)


        screen.blit(pygame.font.SysFont("'freesansbold.ttf", 60, True).render(str(score), 1, (91, 109, 131)), (screen_width-100,50 ))

        #Spawn meteor:
        if not meteor_list:
            spawn_meteor(3 + current_level)
            current_level += 0.5

        for meteor in meteor_list:
            #If meteor go off screen
            if meteor.rect.y > screen_height:
                meteor_list.remove(meteor)
                sprites_list.remove(meteor)

        #Spawn boss:
        if not enemies_list and score >= 5:
            spawn_boss(0)

    if not alive:
       # sprites_list.remove(player)
        screen.fill((0,0,0))
        Menu().displayMenu(screen,"c",score)
        current_level=0
        #sprites_list.remove(bullet)
        #sprites_list.remove(enemy)
        #sprites_list.remove(meteor)
        sprites_list.remove()
        # can do remove or freeze?
    elif pause :
        Menu().displayMenu(screen, "b")

    sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(120)

# Close the window and quit.
pygame.quit()
