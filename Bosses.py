import pygame
import random
import time
from os import path
from Constants import *

class Boss(pygame.sprite.Sprite):
    # flags for boss states
    forward = True # whether the boss moves forward or backward horizontally
    moving_vertical = False # whether the boss moves up or down
    moving_horizontal = True
    # initialise Boss by accepting relevant data from outside of the class
    def __init__(self, game, boss_id, screen, speed, current_level, images, *groups):
        super().__init__(*groups)

        self.boss_id = boss_id
        self.game = game
        self.screen = screen
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.animation_frames = 3
        self.current_frame = 0
        self.moving_horizontal_old_time = time.time()
        self.action_old_time = time.time()

        # initialise boss properties
        self.speed = speed
        self.health = 5 * current_level
        self.total_health = self.health
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = 0

        self.going_in = False
        self.pause = False

        self.anger = False
        self.anger_speech = False
        self.death = False
        self.death_speech = False
        self.killed = False
        self.anger_value = 0.5
        self.anger_multiplier = 1.5

    # update the boss
    def update(self):
        if self.pause == False:
            self.say_phrases() # boss speech
            # boss animation
            if self.health < (self.total_health / 100 * 50) and self.index < 19:
                self.update_animation()
            if self.death and self.index < 30:
                self.animation_frames = 7
                self.update_animation()
                if self.index >= 30:
                    self.killed = True
            if not self.going_in :
                if self.rect.y < 50:
                    self.rect.y += 2
                else:
                    self.going_in = True
            else:
                if not self.death:
                    # define boss's movements
                    if self.boss_id == 1:
                        self.boss_one_movement()
                        self.boss_action(self.boss_id, 2, 3 * self.speed)
                    elif self.boss_id == 2:
                        self.boss_two_movement()
                    elif self.boss_id == 3:
                        self.boss_one_movement()
                        self.boss_action(self.boss_id, 2, 5 * self.speed)

    # boss moves forwards and backwards horizontally, speed increases when anger
    def boss_one_movement(self):
        if self.forward:
            if self.anger:
                self.rect.x += self.speed * 2
            else:
                self.rect.x += self.speed
        elif not self.forward:
            if self.anger:
                self.rect.x -= self.speed
            else:
                self.rect.x -= self.speed / 2
        # revert direction when reaching screen bounds
        if self.rect.right > SCREEN_WIDTH - 50 :
            self.forward = False
        if self.rect.left < 50:
            self.forward = True

    def boss_two_movement(self):
        # if the boss is moving horizontally
        if self.moving_horizontal:
            if self.forward:
                self.rect.x += self.speed
            elif not self.forward:
                self.rect.x -= self.speed / 2
            # revert horizontal direction when reaching screen bounds
            if self.rect.right > SCREEN_WIDTH - 50 :
                self.forward = False
            if self.rect.left < 50:
                self.forward = True
            # stop horizontal movement after every 3-5 seconds
            if time.time() - self.moving_horizontal_old_time > random.randint(3,5):
                self.moving_horizontal = False
        # otherwise
        else:
            # moving quickly towards player
            if self.moving_vertical:
                if self.anger:
                    self.rect.y -= self.speed * 8
                else:
                    self.rect.y -= self.speed * 4
            # moving towards top of screen, i.e return to top
            elif not self.moving_vertical:
                if self.anger:
                    self.rect.y += self.speed * 8
                else:
                    self.rect.y += self.speed * 4
            # revert vertical direction when reaching bottom of screen
            if self.rect.bottom >= (SCREEN_HEIGHT - 50):
                self.moving_vertical = True
            if self.rect.y <= 50:
                self.moving_vertical = False
                self.moving_horizontal_old_time = time.time()
                self.moving_horizontal = True
    # define boss's actions
    def boss_action(self, boss_id, time_between, speed):
        # set interval between actions
        if self.anger:
            time_speed_of_actions = [time_between / 2, speed * self.anger_multiplier]
        else:
            time_speed_of_actions = [time_between , speed * self.anger_multiplier]
        # define actions for different bosses
        if time.time() - self.action_old_time > time_speed_of_actions[0]:
            if boss_id == 1: # boss 1 fires bullets
                self.game.boss_fire_bullet(self, time_speed_of_actions[1])
            if boss_id == 3: # boss 3 spawns meteors
                self.game.spawn_meteor(time_speed_of_actions[1])
            self.action_old_time = time.time()

    def update_health_bar(self):
        if self.going_in and not self.death:
            # draw health bar
            pygame.draw.line(self.screen, RED, (10, 10) , (SCREEN_WIDTH - 10, 10), 8)
            pygame.draw.line(self.screen, GREEN, (10, 10) , ((SCREEN_WIDTH - 10) * (self.health/ self.total_health), 10), 8)

    def update_animation(self):
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def say_phrases(self): # boss speech
        phrase = random.randint(0, 3)
        if not self.going_in:
            opening_line = ['I am thor fear me.ogg', 'I am the starting point of the asgard.ogg', 'my name is thorsten altenkirch.ogg', 'obviously I am the big boss.ogg']
            pygame.mixer.Channel(7).play(pygame.mixer.Sound(path.join(self.game.snd_folder, opening_line[phrase])))
        if self.anger and not self.anger_speech:
            anger_line = ['i made an error for you to spot.ogg', 'stupid question.ogg', 'you cannot pickle my brain.ogg', 'this is easy exercise.ogg']
            pygame.mixer.Channel(7).play(pygame.mixer.Sound(path.join(self.game.snd_folder, anger_line[phrase])))
            self.anger_speech = True
        if self.death and not self.death_speech:
            closing_line = ['Ill be back.ogg', 'rah.ogg', 'lecture resumes next week.ogg', 'how can you pickle my brain.ogg']
            pygame.mixer.Channel(7).play(pygame.mixer.Sound(path.join(self.game.snd_folder, closing_line[phrase])))
            self.death_speech = True

    # if hit, decrease boss health
    def is_hit(self, bullet_damage):
        if self.going_in:
            self.health -= 1 + bullet_damage
            # boss anger when health below threshold
            if self.health < self.total_health * self.anger_value:
                self.anger = True
    # returns if boss is alive
    def is_alive(self):
        return self.health > 0

class Boss_Bullet(pygame.sprite.Sprite):
    bullet_speed = 3
    prev_x_pos = -1
    def __init__(self, game, img, boss, x_pos, y_pos, bullet_speed, *groups):
        super().__init__(*groups)
        self.game = game
        self.boss = boss
        self.boss_id = boss.boss_id
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.origin_pos_x = x_pos
        self.boss_origin_pos_x = boss.rect.x + boss.image.get_rect().centerx
        self.rect.y = y_pos
        self.speed = bullet_speed
        self.pause = False



    def update(self):

        if self.pause == False:
            # update bullet trajectory (splitting bullets)
            self.rect.x += ((self.origin_pos_x - self.boss_origin_pos_x)/25)
            self.rect.y += self.speed
