import pygame
import random
import time

class Boss(pygame.sprite.Sprite):

    forward = True
    moving_vertical = False
    moving_horizontal = True
    RED = (255,0,0)
    GREEN = (0,255,0)
    def __init__(self, boss_id, screen, screen_width, screen_height, speed, current_level, images,  *groups):
        super().__init__(*groups)
        self.boss_id = boss_id
        self.screen = screen
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.animation_frames = 5
        self.current_frame = 0
        self.moving_horizontal_old_time = time.time()

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.speed = speed
        self.health = 5 * current_level
        self.total_health = self.health
        self.rect = self.image.get_rect()

        self.going_in = False
        self.pause = False

        self.anger = False
        self.anger_speech = False
        self.death = False
        self.death_speech = False
        self.killed = False
        self.anger_value = 0.5
        self.bullet_anger_speed_multiplier = 1.5

    # update the bossz
    def update(self):
        if self.pause == False:
            self.say_phrases()
            if self.health < (self.total_health / 100 * 50) and self.index < 19:
                self.update_animation()
            if self.death and self.index < 30:
                self.animation_frames = 10
                self.update_animation()
                if self.index >= 30:
                    self.killed = True
            if not self.going_in :
                if self.rect.y < 50:
                    self.rect.y += 2
                else:
                    self.going_in = True
            else:
                if self.boss_id == 1:
                    self.boss_one_movement()
                elif self.boss_id == 2:
                    self.boss_two_movement()
        else:
            self.rect.x += 0
            self.current_frame += 0

    def boss_one_movement(self):
        if not self.death:
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
                # if the boss go out of the screen
            if self.rect.x + self.image.get_rect().width >= self.screen_width - 50 or self.rect.x <= 50:
                self.forward = not self.forward

    def boss_two_movement(self):
        if not self.death:
            if self.moving_horizontal:
                if self.forward:
                    self.rect.x += self.speed
                elif not self.forward:
                    self.rect.x -= self.speed / 2
                    # if the boss go out of the screen
                if self.rect.x + self.image.get_rect().width > self.screen_width - 50 or self.rect.x < 50:
                    self.forward = not self.forward
                if time.time() - self.moving_horizontal_old_time > random.randint(3,5):
                    self.moving_horizontal = False
            else:
                if self.moving_vertical:
                    if self.anger:
                        self.rect.y -= self.speed * 8
                    else:
                        self.rect.y -= self.speed * 4
                elif not self.moving_vertical:
                    if self.anger:
                        self.rect.y += self.speed * 8
                    else:
                        self.rect.y += self.speed * 4
                if self.rect.y + self.image.get_rect().height > (self.screen_height - 50) or self.rect.y < 50:
                    self.moving_vertical = not self.moving_vertical
                    if self.rect.y < 50:
                        self.moving_horizontal_old_time = time.time()
                        self.moving_horizontal = True

    def update_health_bar(self):
        if self.going_in and not self.death:
            pygame.draw.line(self.screen,self.RED,(self.rect.x + 10,self.rect.y - 10),(self.rect.x+self.image.get_rect().width -10,self.rect.y -10),8)
            pygame.draw.line(self.screen,self.GREEN,(self.rect.x + 10,self.rect.y - 10),(self.rect.x+(self.image.get_rect().width -10)* (self.health/self.total_health),self.rect.y -10),8)

    def update_animation(self):
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def say_phrases(self):
        phrase = random.randint(1,4)
        if not self.going_in:
            if phrase == 1:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/I am thor fear me.ogg'))
            elif phrase == 2:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/I am the starting point of the asgard.ogg'))
            elif phrase == 3:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/my name is thorsten altenkirch.ogg'))
            elif phrase == 4:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/obviously I am the big boss.ogg'))
        if self.anger and not self.anger_speech:
            if phrase == 1:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/i made an error for you to spot.ogg'))
            elif phrase == 2:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/stupid question.ogg'))
            elif phrase == 3:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/you cannot pickle my brain.ogg'))
            elif phrase == 4:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/this is easy exercise.ogg'))
            self.anger_speech = True
        if self.death and not self.death_speech:
            if phrase == 1:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/Ill be back.ogg'))
            elif phrase == 2:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/rah.ogg'))
            elif phrase == 3:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/lecture resumes next week.ogg'))
            elif phrase == 4:
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/how can you pickle my brain.ogg'))
            self.death_speech = True

    # if hit boss health -1
    def is_hit(self, bullet_damage):
        if self.going_in:
            self.health -= 1 + bullet_damage
            if self.health < self.total_health * self.anger_value:
                self.anger = True

    def is_alive(self):
        return self.health > 0

class Boss_Bullet(pygame.sprite.Sprite):
    bullet_speed = 3
    prev_x_pos = -1
    def __init__(self, boss, x_pos, y_pos, bullet_speed, *groups):
        super().__init__(*groups)
        self.boss =  boss
        self.boss_id = boss.boss_id
        self.image = pygame.Surface([5,10])
        self.image.fill([255,255,0]) #yellow bullet, place holder, need to find image or something
        self.rect = self.image.get_rect()
        self.rect.x  = x_pos
        self.origin_pos_x = x_pos
        self.boss_origin_pos_x =  boss.rect.x + boss.image.get_rect().width/2
        self.rect.y  = y_pos
        self.speed = bullet_speed
        self.pause = False

    # different bullets with different bosses
    def update(self):
        if self.pause == False:
            self.rect.x += ((self.origin_pos_x - self.boss_origin_pos_x)/25)
            self.rect.y += self.speed
        else:
            self.rect.x += 0
            self.rect.y += 0
        
            
##            if self.prev_x_pos == -1:
##                self.prev_x_pos = self.rect.x
##                self.rect.x += ((self.prev_x_pos - self.boss.rect.x - self.boss.image.get_rect().width/2)/20)
##            else:
##                self.rect.x += (self.rect.x - self.prev_x_pos)
##                self.prev_x_pos = self.rect.x
        

