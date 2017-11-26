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

score = 0
current_level = 0
start_time = time.time()
pause_time = 0
pause_start_time=time.time()
alive = True
pause = False

background = pygame.image.load('img/background.jpg').convert()
ship_image = pygame.image.load('img/spaceship.png').convert()
enemy_image = pygame.image.load('img/enemy.png').convert()
background_y = 0
pygame.display.set_caption("My Game")

#List of all sprites
sprites_list = pygame.sprite.Group()

#List of bullets
bullet_list = pygame.sprite.Group()

#List of enemies
enemies_list = pygame.sprite.Group()


#Creating sprites
player = PlayerShip(screen_width, ship_image)
sprites_list.add(player)

#Spawning enemies

def spawn_enemy(speed):
    for i in range (6):
        enemy = Enemy(enemy_image, speed)
        enemy.rect.x = 25 + 80*i
        enemy.rect.y = -50
        enemies_list.add(enemy)
        sprites_list.add(enemy)


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


    if not alive:
       # sprites_list.remove(player)
        screen.fill((0,0,0))
        Menu().displayMenu(screen,"c",score)
        current_level=0
    elif pause :
        Menu().displayMenu(screen, "b")

    sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(120)

# Close the window and quit.
pygame.quit()
