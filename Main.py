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
from Constants import *

#Spawning enemies
def spawn_enemy(speed, current_level, difficulty, groups):
    health = int(current_level / difficulty) + 1
    for i in range (5):
        enemy = Enemy(speed, health, groups)
        enemy.rect.x = 10 + 100*i
        enemy.rect.y = -50

def spawn_power_ups(speed, pos_x, pos_y, groups):
    power_up = PowerUp(SCREEN_WIDTH, SCREEN_HEIGHT, speed, groups)
    power_up.rect.x = pos_x
    power_up.rect.y = pos_y

def spawn_meteor(speed, groups):
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('Sound/comet.ogg'))
    pygame.mixer.Channel(2).set_volume(0.8)
    meteor = Meteor(speed, groups)
    meteor.rect.y = -200
    meteor.rect.x = random.randrange(0, SCREEN_WIDTH - meteor.rect.width)

#!!!!!!!!!!!!! can add different boss images!!
def spawn_boss(speed, screen, current_level, boss_id, groups):
    boss = Boss(boss_id,screen,SCREEN_WIDTH, speed, current_level, groups)
    boss.rect.x = SCREEN_WIDTH/2 - boss.rect.width/2
    boss.rect.y = 50

def fire_bullet(player, bullet_speed, fire_bullet_event, fire_bullet_delay, groups):
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sound/laser.ogg'))
    pygame.mixer.Channel(1).set_volume(0.2)
    bullet = Bullet((player.rect.x + player.image.get_rect().width/2), player.rect.y, bullet_speed, groups)
    pygame.time.set_timer(fire_bullet_event, fire_bullet_delay)

def boss_fire_bullet(boss, boss_bullet_speed, groups):
    #can add music
##    pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sound/laser.ogg'))
##    pygame.mixer.Channel(1).set_volume(0.2)
    # if boss.boss_id ==1 the bullet is like this, we could also add boss_id ==2 or more than that if we want different bosses with different bullets
    if boss.boss_id == 1:
        Boss_Bullet(boss,(boss.rect.x + boss.image.get_rect().width/2 -  50), boss.rect.y + boss.image.get_rect().height, boss_bullet_speed, groups)
        Boss_Bullet(boss,(boss.rect.x + boss.image.get_rect().width/2), boss.rect.y + boss.image.get_rect().height, boss_bullet_speed, groups)
        Boss_Bullet(boss,(boss.rect.x + boss.image.get_rect().width/2 + 50), boss.rect.y + boss.image.get_rect().height, boss_bullet_speed, groups)
##    pygame.time.set_timer(boss_bullet_event, 0)z

# -------- Main Program Loop -----------
def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    pygame.display.set_caption(GAME_TITLE)

    # -------- Intro Screen -----------
    intro = Intro(screen,SCREEN_WIDTH,SCREEN_HEIGHT, ARCADE_FUNK)
    intro.show_intro(screen)
    background = pygame.image.load(BACKGROUND_IMG).convert()

    #List of all sprites
    sprites_list = pygame.sprite.Group()

    #List of bullets
    bullet_list = pygame.sprite.Group()
    boss_bullet_list = pygame.sprite.Group()

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
    player = PlayerShip(SCREEN_WIDTH, SCREEN_HEIGHT, [sprites_list])

    background_y = 0
    done = False
    clock = pygame.time.Clock()
    #background music

    start_time = time.time()
    pause_time = 0
    pause_start_time=time.time()
    alive = True
    pause = False

    #Game Properties
    score = 0
    current_level = 0
    difficulty = 10

    #Player Properties
    bullet_speed = 5

    #Enemies Properties
    boss_speed = 1
    boss_bullet_speed = 5
    enemies_speed = math.sqrt(10 + current_level)
    boss_id = 0

    #Setting up firing bullet delay
    fire_bullet_event = pygame.USEREVENT + 1
    fire_bullet_delay = 500
    pygame.time.set_timer(fire_bullet_event, fire_bullet_delay)

    #Setting up the boss firing bullet delay
    boss_bullet_event = pygame.USEREVENT + 2
    boss_bullet_delay = 100
    boss_bullet_counter = 0
    pygame.time.set_timer(boss_bullet_event, boss_bullet_delay)

    # load the highscore
    f = open('highscore.txt', 'r')
    temp = f.read()
    if temp != "":
        highscore = int(temp)
    else:
        highscore = 0
    f.close()

    while not done:
        # --- Looping the background
        if not pause and alive:
            relative_y = background_y % background.get_rect().height
            screen.blit(background, [0, relative_y - background.get_rect().height])
            if relative_y < SCREEN_HEIGHT:
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
                fire_bullet(player, bullet_speed, fire_bullet_event, fire_bullet_delay, [sprites_list, bullet_list])
            # update the boss bullet
            if alive and event.type == boss_bullet_event and not pause:
                if boss_list:
                    boss_fire_bullet(boss_list.sprites()[0], boss_bullet_speed, [sprites_list, boss_bullet_list])
                    boss_bullet_counter +=  1
                    if boss_bullet_counter >= 2:
                        pygame.time.set_timer(boss_bullet_event, 2500)
                        boss_bullet_counter = 0
                    else:
                        pygame.time.set_timer(boss_bullet_event, boss_bullet_delay)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and (not alive):
                    score = 0
                    alive = True
                    intro.show_intro(screen)
                    bullet_speed = 5
                    player = PlayerShip(SCREEN_WIDTH,SCREEN_HEIGHT, [sprites_list])
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
                        temp_speed = [enemies_speed, bullet_speed, boss_bullet_speed]
                        for enemy in enemy_list:
                            enemy.speed = 0
                        for bullet in bullet_list:
                            bullet.speed = 0
                        for bullet in boss_bullet_list:
                            bullet.speed = 0
                        for power_up in power_up_list:
                            power_up.speed = 0
                        pause = True
                        player.pause = True
                        if boss_list:
                            boss.pause = True
                        pause_start_time = time.time()

                        if event.key == pygame.K_r and (not alive):
                            score = 0
                            alive = True
                            intro.show_intro(screen)
                            bullet_speed = 5
                            player = PlayerShip(SCREEN_WIDTH,SCREEN_HEIGHT, [sprites_list])
                            #update highscore when you press r
                            f = open('highscore.txt', 'w')
                            f.write(str(highscore))
                            f.close()
                    else:
                        for enemy in enemy_list:
                            enemy.speed = temp_speed[0]
                        for bullet in bullet_list:
                            bullet.speed = temp_speed[1]
                        for bullet in boss_bullet_list:
                            bullet.speed = temp_speed[2]
                        for power_up in power_up_list:
                            power_up.speed = temp_speed[0] * 1.5

                        pause = False
                        player.pause = False
                        if boss_list:
                            boss.pause = False
                        pause_time += time.time() - pause_start_time

                        """
                        milliseconds = 0
                        second = 1
                        countdown = 3
                        while second < 3:
                            milliseconds += clock.tick_busy_loop(60)
                            if milliseconds > second*1000:
                                second = milliseconds/1000
                                screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 200, True).render(str(countdown - 1), 1, (91, 109, 131)), (50, 200))

                        """

        sprites_list.update()

        # --- Game mechanics
        if alive and not pause:
            # player colliding with enemy
            enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
            if enemy_hit_list:
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('Sound/killed_explo.ogg'))
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
                        #Spawn power ups
                        if not power_up_list:
                            if random.randint(0,100) < POWERUP_PERCENTAGE:
                                spawn_power_ups(enemies_speed * 1.5, enemy.rect.x, enemy.rect.y, [power_up_list, sprites_list])
                        score += 1
                        pygame.mixer.Channel(3).play(pygame.mixer.Sound('Sound/explo.ogg'))
                        pygame.mixer.Channel(3).set_volume(0.5)

                #when player bullet colliding boss
                boss_hit_list = pygame.sprite.spritecollide(bullet, boss_list, False)
                for boss in boss_hit_list:
                     bullet.kill()
                     boss.is_hit()

                     if not boss.is_alive():
                         current_level += 1
                         score += 100
                         boss.kill()
                         # can add sound here
                         for boss_bullet in boss_bullet_list:
                             boss_bullet.kill()
    ##                     boss_bullet.kill()
    ##                     if boss_bullet_delay >= 500:
    ##                        boss_bullet_delay -= 100


                #if player bullet goes off screen
                if bullet.rect.y < -10:
                    bullet.kill()
            # when player colliding boss bullet
            player_hit_list = pygame.sprite.spritecollide(player, boss_bullet_list, False)
            if player_hit_list:
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound('Sound/killed_explo.ogg'))
                    alive = False

            #Kill bullet if it hits meteors
            for meteor in meteor_list:
                meteor_hit_list = pygame.sprite.spritecollide(meteor, bullet_list, True)

           #Spawn enemies if there aren't any, levels and speeds fix later
            if not mob_list and not boss_list:
                if current_level % 5 != 0 or current_level == 0:
                    spawn_enemy(enemies_speed, current_level, difficulty, [enemy_list, mob_list, sprites_list])
                    current_level += 1
                else:
                    boss_id += 1
                    spawn_boss(boss_speed,screen, current_level, boss_id, [boss_list,boss_bullet_list, sprites_list])

            #Spawn meteor:
            if not meteor_list and not boss_list:
                if current_level % 5 == 0:
                    spawn_meteor(enemies_speed * 2,  [enemy_list, meteor_list, sprites_list])

            for sprite in sprites_list  :
                #If enemies go off screen
                if sprite.rect.y > SCREEN_HEIGHT:
                    sprite.kill()
            screen.blit(pygame.font.SysFont("'freesansbold.ttf", 60, True).render(str(score), 1, (91, 109, 131)), (SCREEN_WIDTH-100,50 ))

        #m = Menu(screen_width/2,screen_height/2)
        if not alive:
            bullet_speed = 5
            if score > highscore:
                highscore = score
           # sprites_list.remove(player))
            Menu(SCREEN_WIDTH,SCREEN_HEIGHT).displayMenu(screen,"c",score,highscore)
            current_level = 0
            for sprite in sprites_list:
                sprite.kill()

        elif pause :
            Menu(SCREEN_WIDTH,SCREEN_HEIGHT).displayMenu(screen, "b")
            #Erm, why is pressing R doesn't make it go back to screen can someone fix

        sprites_list.draw(screen)

        pygame.display.flip()

        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()

if __name__ == "__main__":
    main()
