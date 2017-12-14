import pygame
import random
import math
import time
from os import path

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
        # set caption
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        # flags for game states 
        self.running = True
        self.alive = True
        self.pause = False
        self.countdown = False
        self.is_mute = False
        # variable to allow rolling background 
        self.background_y = 0
        # load game components 
        self.load_data()
        self.load_mob_images()
        self.load_boss_images()
        self.load_power_up_images()
        self.load_music()
        self.init_masks()
        # enable game volume
        self.set_volume(True)
        # initiate game and display main menu
        self.menu_screen()

    # load all game music
    def load_music(self):
        self.ARCADE_FUNK = pygame.mixer.Sound(path.join(self.snd_folder,'Arcade Funk.ogg'))  # Channel 0
        self.EXPLOSION = pygame.mixer.Sound(path.join(self.snd_folder,'explo.ogg')) # Channel 1
        self.COIN = pygame.mixer.Sound(path.join(self.snd_folder,'coin.ogg'))  # Channel 2
        self.KILLED = pygame.mixer.Sound(path.join(self.snd_folder,'killed_explo.ogg'))  # Channel 3
        self.COMET = pygame.mixer.Sound(path.join(self.snd_folder,'comet.ogg'))  # Channel 4
        self.LASER = pygame.mixer.Sound(path.join(self.snd_folder,'laser.ogg'))  # Channel 5
        self.BOSS_LASER = pygame.mixer.Sound(path.join(self.snd_folder,'Boss_laser.ogg'))  # Channel 6

    
    def set_volume(self, bool):
       
        if bool == True:  # not mute
            pygame.mixer.Channel(0).set_volume(0.3) # Arcade
            pygame.mixer.Channel(1).set_volume(0.3) # Explosion
            pygame.mixer.Channel(2).set_volume(0.3) # Coin
            pygame.mixer.Channel(3).set_volume(0.3) # Killed
            pygame.mixer.Channel(4).set_volume(0.3) # Comet
            pygame.mixer.Channel(5).set_volume(0.1) # Laser
            pygame.mixer.Channel(6).set_volume(0.3) # Boss_Laser
            pygame.mixer.Channel(7).set_volume(1.0) # Boss Channel
        else:  # mute
            for i in range(0, 8):
                pygame.mixer.Channel(i).set_volume(0)

    # load game components including images and sounds
    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.img_folder = path.join(self.game_folder, 'img')
        self.snd_folder = path.join(self.game_folder, 'Sound')
        self.mob_img_folder = path.join(self.img_folder, 'Enemy')
        self.boss_img_folder = path.join(self.img_folder, 'Thorsten')
        self.powerups_img_folder = path.join(self.img_folder, 'PowerUps')
        self.player_ship_img = pygame.image.load(path.join(self.img_folder, 'player_ship.png')).convert_alpha()
        self.bullet_img = pygame.image.load(path.join(self.img_folder, 'bullet.png')).convert()  # come up error when implement (NEED TO REMOVE)
        self.meteor_img = pygame.image.load(path.join(self.img_folder, 'meteor.png')).convert_alpha()
        self.boss_bolt_img = pygame.image.load(path.join(self.img_folder, 'boss_bolt.png')).convert_alpha()
        self.background = pygame.image.load(path.join(self.img_folder, 'background.jpg')).convert()

        # load high score
        # this will work on linux not the other one but i cant get it to save (NEED TO REMOVE)
        with open(path.join(self.game_folder, HIGHSCORE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0


    def init_masks(self):
        self.player_ship_img_mask = pygame.mask.from_surface(self.player_ship_img)
        self.meteor_img_mask = pygame.mask.from_surface(self.meteor_img)
        self.boss_bolt_img_mask = pygame.mask.from_surface(self.boss_bolt_img)

    # load images for enemy ships
    def load_mob_images(self):
        self.mob_images_list = [path.join(self.mob_img_folder, str(number) + ".png") for number in range(0, 12)]
        self.mob_images = []
        for file in self.mob_images_list:
            image = pygame.image.load(file).convert_alpha()
            image = pygame.transform.scale(image, (80, 80))
            self.mob_images.append(image)
        self.mob_img_mask = pygame.mask.from_surface(self.mob_images[0])
        self.mob_image_rect = self.mob_images[0].get_rect()

    # load images for bosses
    def load_boss_images(self):
        self.boss_images_list = [path.join(self.boss_img_folder, str(number) + ".png") for number in range(1, 32)]
        self.boss_images = []
        for file in self.boss_images_list:
            image = pygame.image.load(file).convert_alpha()
            image = pygame.transform.scale(image, (170,190))
            self.boss_images.append(image)
        self.boss_img_mask = pygame.mask.from_surface(self.boss_images[0])
        self.boss_image_rect = self.boss_images[0].get_rect()

    # load images for Power-ups
    def load_power_up_images(self):
        self.power_up_images_list = []
        self.power_up_images = [[] for i in range(1, len(POWER_UP_ID_LIST) + 1)]
        for power_up_id in POWER_UP_ID_LIST:
            self.power_up_images_list.append([path.join(self.powerups_img_folder, str(power_up_id) + str(number) + ".png") for number in range(1, 11)])
        for i in range(0, len(self.power_up_images)):
            for file in self.power_up_images_list[i]:
                image = pygame.image.load(file).convert_alpha()
                image = pygame.transform.scale(image, (50, 50))
                self.power_up_images[i].append(image)

    # write highscore to file
    def write_highscore(self):
        if self.score >= self.highscore: # if current score is greater than current highscore
            with open(path.join(self.game_folder, HIGHSCORE), 'w') as f:
                f.write(str(self.score))

    # initiate new game
    def new_game(self):

        self.sprites_list = pygame.sprite.Group()  #List of all sprites
        self.bullet_list = pygame.sprite.Group()  #List of bullets
        self.boss_bullet_list = pygame.sprite.Group() #list of boss bullets
        self.boss_list = pygame.sprite.Group()  #list of boss
        self.enemy_list = pygame.sprite.Group()  #List of all enemies
        self.mob_list = pygame.sprite.Group()  #List of mobs
        self.power_up_list = pygame.sprite.Group()  #List of PowerUps
        self.speed_power_up_list = pygame.sprite.Group()  #List of speed power ups
        self.damage_power_up_list = pygame.sprite.Group()  #List of damage power ups
        self.double_power_up_list = pygame.sprite.Group()  #List of double power ups
        self.meteor_list = pygame.sprite.Group()  #List of meteor

        #Creating sprites
        self.player = PlayerShip(self.player_ship_img, self.sprites_list)

        #Game Properties
        self.score = 0
        self.current_level = 0

        #Player Properties
        self.bullet_speed = 10
        self.bullet_damage = 0
        self.double_power = False

        #Enemies Properties
        self.boss_speed = 2
        self.boss_id = 0
        self.boss_bullet_speed = 8
        self.enemies_speed = 6

        #Setting up firing bullet delay
        self.fire_bullet_event = pygame.USEREVENT + 1
        self.fire_bullet_delay = 500
        pygame.time.set_timer(self.fire_bullet_event, self.fire_bullet_delay)

        self.run()

    def menu_screen(self):
        if not pygame.mixer.Channel(0).get_busy():
            pygame.mixer.Channel(0).play(self.ARCADE_FUNK, -1)
        # intro screen
        self.intro = Intro(self)
        # initiate new game
        self.new_game()

    # display relevant menu
    def show_menu(self, page):
        Menu().displayMenu(self.screen, page, self.score, self.highscore)


    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            # get and process events
            self.events()
            # update game components
            self.update()
            # update screen
            self.draw()
            self.clock.tick(FPS)

    # draw rolling background
    def draw_background(self):
        if not self.pause and self.alive:
            relative_y = self.background_y % self.background.get_rect().height
            self.screen.blit(self.background, [0, relative_y - self.background.get_rect().height])
            if relative_y < SCREEN_HEIGHT:
                self.screen.blit(self.background, [0, relative_y])
            self.background_y += 1

    # update screen: background -> sprites -> menus
    def draw(self):
        self.draw_background()
        # update sprites
        self.sprites_list.draw(self.screen)

        # check if menus need to be drawn
        if self.alive and not self.pause:
            # update score
            if self.score > self.highscore:
                self.screen.blit(pygame.font.SysFont(FONT, 40, True).render(str(self.score), 0, RED), (SCREEN_WIDTH - 100, 50))
            else:
                self.screen.blit(pygame.font.SysFont(FONT, 40, True).render(str(self.score), 0, GREY), (SCREEN_WIDTH - 100, 50))
        elif self.pause: # show pause menu if on pause
            self.show_menu("b")
        else:
            self.screen.blit(pygame.font.SysFont(FONT, 40, True).render(str(self.score), 0, BLACK), (SCREEN_WIDTH - 100, 50))
        if self.boss_list:
            for boss in self.boss_list:
                # update boss's health bar
                boss.update_health_bar()
        # *after* drawing everything, flip the display
        pygame.display.flip()

    # get and process events
    def events(self):
        key = pygame.key.get_pressed()
        # process events
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: # on quit
                #update highscore when you quit
                self.write_highscore()
                # update game flags
                self.playing = False
                self.running = False

            if self.alive and event.type == self.fire_bullet_event and not self.pause:
                # enable automatically bullet shooting
                self.fire_bullet(self.player, self.bullet_speed, self.fire_bullet_event, self.fire_bullet_delay)

            elif event.type == pygame.KEYDOWN: # key presses
                if event.key == pygame.K_r and (not self.alive):
                    #update highscore when you press r
                    self.write_highscore()
                    # reset game and return to main menu
                    self.alive = True
                    self.menu_screen()
                if self.pause: # on pause
                    if event.key == pygame.K_r and self.alive:
                        # unpause and return to main menu
                        self.pause = False
                        self.menu_screen()
                if event.key == pygame.K_n and (not self.alive): # Press n to quit
                    #update highscore when you press n
                    self.write_highscore()
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_ESCAPE and self.alive:
                    if not self.pause:
                        # pause game
                        self.pause = True
                        for sprite in self.sprites_list:
                            sprite.pause = True
                    else:
                        # unpause
                        self.pause = False
                        self.countdown = True

    def update(self):
        self.sprites_list.update()

        if self.alive and not self.pause:
            # detect player colliding (prefect collision) with enemy
            for mob in self.mob_list: # collision with enemy ships
                self.check_for_collision(self.player, mob, self.player_ship_img_mask, self.mob_img_mask)

            for meteor in self.meteor_list: # collision with meteors
                self.check_for_collision(self.player, meteor, self.player_ship_img_mask, self.meteor_img_mask)

            if self.boss_list: # collision with boss
                for boss in self.boss_list:
                    self.check_for_collision(self.player, boss, self.player_ship_img_mask, self.boss_img_mask)

            for boss_bullet in self.boss_bullet_list:# collision with boss bullets
                self.check_for_collision(self.player, boss_bullet, self.player_ship_img_mask, self.boss_bolt_img_mask)

            # load different types of powerups
            power_up_hit_list = pygame.sprite.spritecollide(self.player, self.power_up_list, False)
            for hit in power_up_hit_list:
                pygame.mixer.Channel(2).play(self.COIN)
                if hit in self.speed_power_up_list: # speed power up, increase the speed
                    if self.fire_bullet_delay >= 150:
                        self.fire_bullet_delay -= 50
                elif hit in self.damage_power_up_list:# damage power up, increase the damage
                    self.bullet_damage += 1
                elif hit in self.double_power_up_list:# double power up, double shoot
                    self.double_power = True
                    self.double_power_old_time = time.time()
                hit.kill() # remove power up on hit
            # set the duration of double power up
            if self.double_power:
                if time.time() - self.double_power_old_time > 10:
                    self.double_power = False
            # kill the enemy
            for bullet in self.bullet_list:
                enemies_hit_list = pygame.sprite.spritecollide(bullet, self.mob_list, False)
                for mob in enemies_hit_list:
                    # update the enemy health
                    if mob.death == False:
                        mob.health -= 1 + self.bullet_damage
                        self.score += 1
                        bullet.kill()
                        if mob.health <= 0:
                            mob.death = True
                            mob.remove(self.mob_list, self.enemy_list)
                            #Spawn power ups
                            if not self.power_up_list:
                                if random.randint(0, 100) < POWERUP_PERCENTAGE:
                                    which_power_up = random.randint(0, 2)
                                    which_group = [self.speed_power_up_list, self.damage_power_up_list, self.double_power_up_list]
                                    PowerUp(POWER_UP_ID_LIST[which_power_up], POWER_UP_ID_LIST, self.power_up_images, mob.rect.centerx, mob.rect.y, [which_group[which_power_up], self.power_up_list, self.sprites_list])
                            pygame.mixer.Channel(1).play(self.EXPLOSION)
                    if mob.killed:
                        mob.kill()

                #Kill bullet if it hits meteors
                for meteor in self.meteor_list:
                    meteor_hit_list = pygame.sprite.spritecollide(meteor, self.bullet_list, True)

                #when player bullet collides with boss
                boss_hit_list = pygame.sprite.spritecollide(bullet, self.boss_list, False)
                for boss in boss_hit_list:
                     if not boss.death:
                        bullet.kill()
                     # update boss's health
                     boss.is_hit(self.bullet_damage)
                     # on destruction of boss
                     if not boss.is_alive() and not boss.death:
                         self.score += 100
                         boss.death = True
                         pygame.mixer.Channel(1).play(self.EXPLOSION)
                     # remove boss and boss bullets
                     if boss.killed:
                         boss.kill()

                         for boss_bullet in self.boss_bullet_list:
                             boss_bullet.kill()


           #Spawn enemies
            if not self.mob_list and not self.boss_list:
                if self.current_level % DIFFICULTY != 0 or self.current_level == 0:
                    self.spawn_enemy(self.enemies_speed, self.current_level)
                else:
                    # spawn new boss
                    self.boss_id += 1
                    if self.boss_id > 3:
                        self.boss_id = 1
                    Boss(self, self.boss_id, self.screen, self.boss_speed * (1 + self.current_level / 100), self.current_level, self.boss_images, [self.boss_list, self.sprites_list])
                self.current_level += 1 # increment game level

            #Spawn meteor:
            if not self.meteor_list and not self.boss_list:
                if self.current_level % METEOR_SPAWN_RATE == 0:
                    self.spawn_meteor(self.enemies_speed * 2)

            for sprite in self.sprites_list :
                #If objects go off screen, for meteor, boss moves, enemy/mobs
                if sprite.rect.top > SCREEN_HEIGHT:
                    sprite.kill()

        
        if not self.alive: # on player's death 
            # update highscore 
            if self.score > self.highscore:
                self.highscore = self.score
            self.show_menu('c') # show game over screen
            for sprite in self.sprites_list: # remove all game objects
                sprite.kill()

        elif self.pause: # on pause
            self.show_menu('b')# show pause screen

        elif not self.pause and self.countdown: # on unpause
            self.show_menu('d') # show countdown screen
            self.countdown = False
            for sprite in self.sprites_list:
                sprite.pause = False
    # check for perfect collision
    def check_for_collision(self, player, enemy, player_mask, enemy_mask):
        offset_x, offset_y = (enemy.rect.x - player.rect.x), (enemy.rect.y - player.rect.y)
        if (player_mask.overlap(enemy_mask, (offset_x, offset_y)) != None):
            pygame.mixer.Channel(3).play(self.KILLED)
            self.alive = False

    # spawning enemies
    def spawn_enemy(self, speed, current_level):
        health = int(current_level / DIFFICULTY) + 1
        for i in range(5):
            enemy = Enemy(speed * (1 + current_level / 100), health, self.mob_images, [self.enemy_list, self.mob_list, self.sprites_list])
            enemy.rect.x = 10 + 100*i
            enemy.rect.y = -50
    # spawning meteors
    def spawn_meteor(self, speed):
        pygame.mixer.Channel(4).play(self.COMET)
        meteor = Meteor(self.meteor_img, speed, [self.enemy_list, self.meteor_list, self.sprites_list])
        meteor.rect.y = -200
        meteor.rect.x = random.randrange(0, SCREEN_WIDTH - meteor.rect.w)
    # spawning fire bullets
    def fire_bullet(self, player, bullet_speed, fire_bullet_event, fire_bullet_delay):
        pygame.mixer.Channel(5).play(self.LASER)
        if self.double_power:
            bullet1 = Bullet(self.bullet_img, (player.rect.x + player.image.get_rect().width/4), player.rect.top, bullet_speed, [self.bullet_list, self.sprites_list])
            bullet2 = Bullet(self.bullet_img, (player.rect.x + player.image.get_rect().width/4 * 3), player.rect.top, bullet_speed, [self.bullet_list, self.sprites_list])
        else:
            bullet = Bullet(self.bullet_img, player.rect.centerx, player.rect.top, bullet_speed, [self.bullet_list, self.sprites_list])
        pygame.time.set_timer(fire_bullet_event, fire_bullet_delay)
    # spawning boss fire bullet
    def boss_fire_bullet(self, boss, boss_bullet_speed):
        if boss.going_in and not boss.death:
            Boss_Bullet(self, self.boss_bolt_img, boss, (boss.rect.centerx - 50), boss.rect.bottom, boss_bullet_speed, [self.boss_bullet_list, self.sprites_list])
            Boss_Bullet(self, self.boss_bolt_img, boss, (boss.rect.centerx), boss.rect.bottom, boss_bullet_speed, [self.boss_bullet_list, self.sprites_list])
            Boss_Bullet(self, self.boss_bolt_img, boss, (boss.rect.centerx + 50), boss.rect.bottom, boss_bullet_speed, [self.boss_bullet_list, self.sprites_list])
            pygame.mixer.Channel(6).play(self.BOSS_LASER)

# initiate new game
g = Game()

while g.running:
    g.new_game()

pygame.quit()
