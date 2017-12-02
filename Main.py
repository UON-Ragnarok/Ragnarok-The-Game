import pygame
import random
import time

from PlayerShip import *
from Bullet import *
from Enemy import *
from Menu import *

screen_width = 500
screen_height = 800
FPS = 60


# initialize pygame and creat window
pygame.init()
pygame.mixer.init() # handle sound effects
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

score = 0
level_score = 0
current_level = 1
#boss_health = 50 + 2**current_level*10
boss_health = 10
start_time = time.time()
pause_time = 0
pause_start_time=time.time()
alive = True
pause = False


background = pygame.image.load('img/background.jpg').convert()
ship_image = pygame.image.load('img/spaceship.png').convert()
boss_image = pygame.image.load('img/thor.png').convert()
enemy_image = pygame.image.load('img/enemy.png').convert()
meteor_image = pygame.image.load('img/meteor.png').convert()
background_y = 0


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
    
done = False

player.rect.y = (screen_height - player.rect.height)*0.95

<<<<<<< HEAD
pygame.mixer.music.load('Arcade Funk.ogg')

pygame.mixer.music.play(loops=0, start=0.0)
=======


boss_kill = False    

>>>>>>> efd78124909ec4fe44fceee1018ff6b3e669d192
# -------- Main Program Loop -----------
while not done:

    # keep loop running at the right speed
    clock.tick(FPS)
    # --- Looping the background
    relative_y = background_y % background.get_rect().height
    screen.blit(background, [0, relative_y - background.get_rect().height])
    if relative_y < screen_height:
        screen.blit(background, [0, relative_y])
    background_y += 1

    # --- Main event loop
    key = pygame.key.get_pressed()
	
    
    # process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            done = True

<<<<<<< HEAD
        if alive:
=======
        if event.type == pygame.MOUSEBUTTONDOWN and alive and not pause:
>>>>>>> efd78124909ec4fe44fceee1018ff6b3e669d192
            bullet = Bullet()
            bullet.rect.x = player.rect.x + ship_image.get_rect().width/2
            bullet.rect.y = player.rect.y
            sprites_list.add(bullet)
            bullet_list.add(bullet)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and not alive:
                score = 0
                alive = True
            if event.key == pygame.K_n and not alive:
                done = True
            if event.key == pygame.K_ESCAPE and alive:
                if pause:
                    pause = False
                    pause_time += time.time() - pause_start_time
                else:
                    pause = True
                    pause_start_time = time.time()
                    
    # Update
    sprites_list.update()

    # --- Game mechanics
      
    if alive and not pause:
        # player colliding with enemy
        if pygame.sprite.spritecollide(player, enemies_list, True) or pygame.sprite.spritecollide(player, meteor_list, True):
             alive= False
             
        for bullet in bullet_list:
            enemies_hit_list = pygame.sprite.spritecollide(bullet, enemies_list, True)
            for enemies in enemies_hit_list:
                score += 1
                bullet_list.remove(bullet)
                sprites_list.remove(bullet)


            boss_hit = pygame.sprite.spritecollide(bullet, boss_list, True)

            if boss_health > 0:
                if boss_hit:
                    boss_health -= 1
                    bullet_list.remove(bullet)
                    sprites_list.remove(bullet)
            # 
            if boss_health == 0:
                boss_kill = True
                current_level += 1
                score += 100
                boss_list.remove(boss_list)
                sprites_list.remove(boss_list)
                boss_health = 10**current_level
                level_score = score


            #if bullet goes off screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                sprites_list.remove(bullet)

        #Spawn enemies if there aren't any, levels and speeds fix later
        if not enemies_list and score < level_score + 5  :
            spawn_enemy(2 + current_level)

        for enemy in enemies_list:
            #If enemies go off screen
            if enemy.rect.y > screen_height:
                enemies_list.remove(enemy)
                sprites_list.remove(enemy)


        screen.blit(pygame.font.SysFont("'freesansbold.ttf", 60, True).render(str(score), 1, (91, 109, 131)), (screen_width-100,50 ))

        #Spawn meteor:
        if not meteor_list:
            spawn_meteor(3 + current_level)

        for meteor in meteor_list:
            #If meteor go off screen
            if meteor.rect.y > screen_height:
                meteor_list.remove(meteor)
                sprites_list.remove(meteor)
    
        #Spawn boss:
        if not enemies_list and not boss_kill: # need to get 
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

    # Draw
    sprites_list.draw(screen)
	
    # after draing everything flip the display
    pygame.display.flip()

# Close the window and quit.
pygame.quit()
