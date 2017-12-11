import pygame
import random
import math
import time

from PlayerShip import *
from Bullet import *
from Enemy import *
from Bosses import *
from Menu import *
from PowerUp import *
from Intro import *
from Constants import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_highscore()
        self.alive = True
        self.pause = False
        self.background_y = 0
        self.load_mob_images()
        self.load_boss_images()
        self.load_power_up_images()
        self.load_music()
        self.menu_screen()
        
        

    def load_music(self):
        self.ARCADE_FUNK = 'Sound/Arcade Funk.ogg'  # Channel 0
        self.EXPLOSION = pygame.mixer.Sound('Sound/explo.ogg') # Channel 1
        self.COIN = pygame.mixer.Sound('Sound/coin.ogg')  # Channel 2
        self.KILLED = pygame.mixer.Sound('Sound/killed_explo.ogg')  # Channel 3
        self.COMET = pygame.mixer.Sound('Sound/comet.ogg')  # Channel 4
        self.LASER = pygame.mixer.Sound('Sound/laser.ogg')  # Channel 5
        self.BOSS_LASER = pygame.mixer.Sound('Sound/Boss_laser.ogg')  # Channel 6
        pygame.mixer.Channel(1).set_volume(0.3) # Explosion
        pygame.mixer.Channel(2).set_volume(0.3) # Coin
        pygame.mixer.Channel(3).set_volume(0.3) # Killed
        pygame.mixer.Channel(4).set_volume(0.3) # Comet
        pygame.mixer.Channel(5).set_volume(0.1) # Laser
        pygame.mixer.Channel(6).set_volume(0.3) # Boss_Laser
        pygame.mixer.Channel(7).set_volume(1.0) # Boss Channel
        
        
    def load_mob_images(self):
        self.mob_images_list = ["img/enemy/" + str(number) + ".png" for number in range(0,12)]
        self.mob_images = []
        for file in self.mob_images_list:
            image = pygame.image.load(file).convert_alpha()
            image = pygame.transform.scale(image, (80,80))
            self.mob_images.append(image)

    def load_boss_images(self):
        self.boss_images_list = ["img/Thorsten/" + str(number) + ".png" for number in range(1,32)]
        self.boss_images = []
        for file in self.boss_images_list:
            image = pygame.image.load(file).convert_alpha()
            image = pygame.transform.scale(image, (170,190))
            self.boss_images.append(image)

    def load_power_up_images(self):
        self.power_up_images_list = []
        self.power_up_images = [[] for i in range(1, len(POWER_UP_ID_LIST) + 1)]
        for power_up_id in POWER_UP_ID_LIST:
            self.power_up_images_list.append(["img/PowerUps/" + str(power_up_id) + str(number) + ".png" for number in range(1,11)])
        for i in range(0, len(self.power_up_images)):
            for file in self.power_up_images_list[i]:
                image = pygame.image.load(file).convert_alpha()
                image = pygame.transform.scale(image, (50,50))
                self.power_up_images[i].append(image)


    def load_highscore(self):
        f = open(HIGHSCORE, 'r')
        temp = f.read()
        if temp != "":
            self.highscore = int(temp)
        else:
            self.highscore = 0
        f.close()

    def write_highscore(self):
        if self.score >= self.highscore:
            f = open(HIGHSCORE, 'w')
            f.write(str(self.score))
            f.close()

    def new_game(self):
        #List of all sprites
        self.sprites_list = pygame.sprite.Group()
        #List of bullets
        self.bullet_list = pygame.sprite.Group()
        self.boss_bullet_list = pygame.sprite.Group()
        #BOSS
        self.boss_list = pygame.sprite.Group()
        #List of all enemies
        self.enemy_list = pygame.sprite.Group()
        #List of mobs
        self.mob_list = pygame.sprite.Group()
        #List of PowerUps
        self.power_up_list = pygame.sprite.Group()
        #List of speed power ups
        self.speed_power_up_list = pygame.sprite.Group()
        #List of damage power ups
        self.damage_power_up_list = pygame.sprite.Group()
        #List of double power ups
        self.double_power_up_list = pygame.sprite.Group()
        #List of meteor
        self.meteor_list = pygame.sprite.Group()
        #Creating sprites
        self.player = PlayerShip(self)

        #Game Properties
        self.score = 0
        self.current_level = 0

        #Player Properties
        self.bullet_speed = 5
        self.bullet_damage = 0
        self.double_power = False

        #Enemies Properties
        self.boss_speed = 1
        self.boss_bullet_speed = 5
        self.enemies_speed = 3

        #Setting up firing bullet delay
        self.fire_bullet_event = pygame.USEREVENT + 1
        self.fire_bullet_delay = 500
        pygame.time.set_timer(self.fire_bullet_event, self.fire_bullet_delay)

        #Setting up the boss firing bullet delay
        self.boss_bullet_event = pygame.USEREVENT + 2
        self.boss_bullet_delay = 100
        self.boss_bullet_counter = 0
        pygame.time.set_timer(self.boss_bullet_event, self.boss_bullet_delay)
        self.run()

    def menu_screen(self):
        self.intro = Intro(self.screen, self.ARCADE_FUNK)
        self.background = pygame.image.load(BACKGROUND_IMG).convert()
        self.new_game()

    def show_menu(self, id):
        Menu().displayMenu(self.screen, id ,self.score, self.highscore)

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def draw_background(self):
        if not self.pause and self.alive:
            relative_y = self.background_y % self.background.get_rect().height
            self.screen.blit(self.background, [0, relative_y - self.background.get_rect().height])
            if relative_y < SCREEN_HEIGHT:
                self.screen.blit(self.background, [0, relative_y])
            self.background_y += 1

    def draw(self):
        self.draw_background()
        # *after* drawing everything, flip the display
        if self.alive and not self.pause:
            if self.score >= self.highscore:
                self.screen.blit(pygame.font.SysFont(FONT, 40, True).render(str(self.score),  0, RED), (SCREEN_WIDTH - 100, 50))
            else:
                self.screen.blit(pygame.font.SysFont(FONT, 40, True).render(str(self.score), 0, GREY), (SCREEN_WIDTH - 100, 50))
        else:
            self.screen.blit(pygame.font.SysFont(FONT, 40, True).render(str(self.score), 0, BLACK), (SCREEN_WIDTH - 100, 50))
        if self.boss_list:
            for boss in self.boss_list:
                boss.update_health_bar()
        self.sprites_list.draw(self.screen)
        pygame.display.flip()

    def events(self):
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #update highscore when you quit
                self.write_highscore()
                self.playing = False
                self.running = False

            if self.alive and event.type == self.fire_bullet_event and not self.pause:
                self.fire_bullet(self.player, self.bullet_speed, self.fire_bullet_event, self.fire_bullet_delay)
             # update the boss bullet
            if self.alive and event.type == self.boss_bullet_event and not self.pause and self.boss_list and self.boss_list.sprites()[0].boss_id == 1:
                self.boss_fire_bullet(self.boss_list.sprites()[0], self.boss_bullet_speed, [self.sprites_list, self.boss_bullet_list])
                self.boss_bullet_counter += 1
                if self.boss_bullet_counter >= 2:
                    pygame.time.set_timer(self.boss_bullet_event, 2500)
                    self.boss_bullet_counter = 0
                else:
                    pygame.time.set_timer(self.boss_bullet_event, self.boss_bullet_delay)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and (not self.alive):
                    #update highscore when you press r
                    self.write_highscore()
                    self.alive = True
                    self.menu_screen()
                if self.pause:
                    if event.key == pygame.K_r and self.alive:
                        self.pause = False
                        self.menu_screen()
                if event.key == pygame.K_n and (not self.alive):
                    #update highscore when you press n
                    self.write_highscore()
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_ESCAPE and self.alive:
                    if not self.pause:
                        self.pause = True
                        for sprite in self.sprites_list:
                            sprite.pause = True
                    else:
                        self.pause = False
                        for sprite in self.sprites_list:
                            sprite.pause = False

    def update(self):
        self.sprites_list.update()

        if self.alive and not self.pause:
            # player colliding with enemy
            enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, True)
            if enemy_hit_list:
                pygame.mixer.Channel(3).play(self.KILLED)
                self.alive = False

            #If hit a power up
            power_up_hit_list = pygame.sprite.spritecollide(self.player, self.power_up_list, False)
            for hit in power_up_hit_list:
                pygame.mixer.Channel(2).play(self.COIN)
                if hit in self.speed_power_up_list:
                    if self.fire_bullet_delay >= 150:
                        self.fire_bullet_delay -= 50
                elif hit in self.damage_power_up_list:
                    self.bullet_damage += 1
                elif hit in self.double_power_up_list:
                    self.double_power = True
                    self.double_power_old_time = time.time()
                hit.kill()

            if self.double_power:
                if time.time() - self.double_power_old_time > 10:
                    self.double_power = False

            for bullet in self.bullet_list:
                enemies_hit_list = pygame.sprite.spritecollide(bullet, self.mob_list, False)
                for enemy in enemies_hit_list:
                    if enemy.death == False:
                        enemy.health -= 1 + self.bullet_damage
                        self.score += 1
                        bullet.kill()
                        if enemy.health <= 0:
                            enemy.death = True
                            enemy.remove(self.mob_list, self.enemy_list)
                            #Spawn power ups
                            if not self.power_up_list:
                                if random.randint(0, 100) < POWERUP_PERCENTAGE:
                                    which_power_up = random.randint(1,3)
                                    if which_power_up == 1:
                                        self.spawn_power_up(POWER_UP_ID_LIST[0], enemy.rect.x + 15, enemy.rect.y, [self.speed_power_up_list, self.power_up_list, self.sprites_list])
                                    elif which_power_up == 2:
                                        self.spawn_power_up(POWER_UP_ID_LIST[1], enemy.rect.x + 15, enemy.rect.y, [self.damage_power_up_list, self.power_up_list, self.sprites_list])
                                    elif which_power_up == 3:
                                        self.spawn_power_up(POWER_UP_ID_LIST[2], enemy.rect.x + 15, enemy.rect.y, [self.double_power_up_list, self.power_up_list, self.sprites_list])
                            pygame.mixer.Channel(1).play(self.EXPLOSION)
                    if enemy.killed:
                        enemy.kill()

                #when player bullet colliding boss
                boss_hit_list = pygame.sprite.spritecollide(bullet, self.boss_list, False)
                for boss in boss_hit_list:
                     if not boss.death:
                        bullet.kill()
                     boss.is_hit(self.bullet_damage)

                     if not boss.is_alive() and not boss.death:
                         self.score += 100
                         boss.death = True
                         pygame.mixer.Channel(1).play(self.EXPLOSION)

                     if boss.killed:
                         boss.kill()

                         for boss_bullet in self.boss_bullet_list:
                             boss_bullet.kill()

            # when player colliding boss bullet
            player_hit_list = pygame.sprite.spritecollide(self.player, self.boss_bullet_list, False)
            if player_hit_list:
                    pygame.mixer.Channel(3).play(self.KILLED)
                    self.alive = False

            #Kill bullet if it hits meteors
            for meteor in self.meteor_list:
                meteor_hit_list = pygame.sprite.spritecollide(meteor, self.bullet_list, True)

           #Spawn enemies if there aren't any, levels and speeds fix later
            if not self.mob_list and not self.boss_list:
                if self.current_level % DIFFICULTY != 0 or self.current_level == 0:
                    self.spawn_enemy(self.enemies_speed, self.current_level, [self.enemy_list, self.mob_list, self.sprites_list])
                else:
                    self.boss_id = random.randint(1,2)
                    self.spawn_boss(self.boss_speed, self.screen, self.current_level, self.boss_id, [self.boss_list,self.boss_bullet_list, self.sprites_list])
                self.current_level += 1

            #Spawn meteor:
            if not self.meteor_list and not self.boss_list:
                if self.current_level % METEOR_SPAWN_RATE == 0:
                    self.spawn_meteor(self.enemies_speed * 2)

            for sprite in self.sprites_list :
                #If enemies go off screen, for meteor, boss moves, enemy/mobs
                if sprite.rect.top > SCREEN_HEIGHT:
                    sprite.kill()
        #m = Menu(screen_width/2,screen_height/2)
        if not self.alive:
            if self.score > self.highscore:
                self.highscore = self.score
           # sprites_list.remove(player))
            self.show_menu('c')
            for sprite in self.sprites_list:
                sprite.kill()

        elif self.pause :
            self.show_menu('b')

    #Spawning enemies
    def spawn_enemy(self, speed, current_level, groups):
        health = int(current_level / DIFFICULTY) + 1
        for i in range (5):
            enemy = Enemy(speed * (1 + current_level / 100), health, self.mob_images, groups)
            enemy.rect.x = 10 + 100*i
            enemy.rect.y = -50

    def spawn_power_up(self, id, pos_x, pos_y, groups):
        power_up = PowerUp(id, POWER_UP_ID_LIST, self.power_up_images, groups)
        power_up.rect.x = pos_x
        power_up.rect.y = pos_y

    def spawn_meteor(self, speed):
        pygame.mixer.Channel(4).play(self.COMET)
        meteor = Meteor(self, speed)
        meteor.rect.y = -200
        meteor.rect.x = random.randrange(0, SCREEN_WIDTH - meteor.rect.width)

    #!!!!!!!!!!!!! can add different boss images!!
    def spawn_boss(self, speed, screen, current_level, boss_id, groups):
        boss = Boss(boss_id, screen, speed * (1 + current_level / 100), current_level, self.boss_images, groups)
        boss.rect.x = SCREEN_WIDTH/2 - boss.rect.width/2
        boss.rect.y = -200

    def fire_bullet(self, player, bullet_speed, fire_bullet_event, fire_bullet_delay):
        pygame.mixer.Channel(5).play(self.LASER)
        if self.double_power:
            bullet1 = Bullet(self, (player.rect.x + player.image.get_rect().width/4), player.rect.y, bullet_speed)
            bullet2 = Bullet(self, (player.rect.x + player.image.get_rect().width/4 * 3), player.rect.y, bullet_speed)
        else:
            bullet = Bullet(self, (player.rect.x + player.image.get_rect().width/2), player.rect.y, bullet_speed)
        pygame.time.set_timer(fire_bullet_event, fire_bullet_delay)

    def boss_fire_bullet(self, boss, boss_bullet_speed, groups):
        #can add music
        # if boss.boss_id ==1 the bullet is like this, we could also add boss_id ==2 or more than that if we want different bosses with different bullets
        if boss.going_in and not boss.death:
            if boss.anger == True:
                boss_bullet_speed = boss_bullet_speed * boss.bullet_anger_speed_multiplier
            Boss_Bullet(boss,(boss.rect.x + boss.image.get_rect().width/2 - 50), boss.rect.y + boss.image.get_rect().height, boss_bullet_speed, groups)
            Boss_Bullet(boss,(boss.rect.x + boss.image.get_rect().width/2), boss.rect.y + boss.image.get_rect().height, boss_bullet_speed, groups)
            Boss_Bullet(boss,(boss.rect.x + boss.image.get_rect().width/2 + 50), boss.rect.y + boss.image.get_rect().height, boss_bullet_speed, groups)
            pygame.mixer.Channel(6).play(self.BOSS_LASER)
    ##    pygame.time.set_timer(boss_bullet_event, 0)


g = Game()

while g.running:
    g.new_game()

pygame.quit()
