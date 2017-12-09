import pygame


class Boss(pygame.sprite.Sprite):

    forward = True
    RED = (255,0,0)
    GREEN = (0,255,0)
    def __init__(self, boss_id, screen, screen_width, speed, current_level, *groups):
        super().__init__(*groups)
        self.boss_id = boss_id
        self.screen = screen
        self.images_list = ["img/Thorsten/" + str(number) + ".png" for number in range(1,21)]
        self.images = []
        #Load all images
        for file in self.images_list:
            image = pygame.image.load(file).convert_alpha()
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.range = screen_width
        self.speed = speed
        self.health = 10 * current_level
        self.total_health = self.health
        self.rect = self.image.get_rect()
        self.going_in = False
        self.pause = False
        self.animation_frames = 5
        self.current_frame = 0
        self.anger = False
        self.anger_value = 0.5
        self.bullet_anger_speed_multiplier = 1.5


    # update the bossz
    def update(self):
        if self.pause == False:
            if self.health < (self.total_health / 100 * 50) and self.index != 19:
                self.update_sprite_animation()
            if not self.going_in:
                if self.rect.y < 50:
                    self.rect.y += 2
                else:
                    self.going_in = True
            else:
                if self.forward:
                    if self.anger:
                        self.rect.x += self.speed * 2
                    else:
                        self.rect.x += self.speed
                else:
                    if self.anger:
                        self.rect.x -= self.speed * 2
                    else:
                        self.rect.x -= self.speed
                    # if the boss go out of the screen
                if self.rect.x + self.image.get_rect().width > self.range - 50 or self.rect.x < 50:
                    self.forward = not self.forward
                    # print the hp
        else:
            self.rect.x += 0

    def update_health_bar(self):
        if self.going_in:
            pygame.draw.line(self.screen,self.RED,(self.rect.x + 10,self.rect.y - 10),(self.rect.x+self.image.get_rect().width -10,self.rect.y -10),8)
            pygame.draw.line(self.screen,self.GREEN,(self.rect.x + 10,self.rect.y - 10),(self.rect.x+(self.image.get_rect().width -10)* (self.health/self.total_health),self.rect.y -10),8)

    def update_sprite_animation(self):
        if self.pause == False:
            self.current_frame += 1
            if self.current_frame >= self.animation_frames:
                self.current_frame = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]
        else:
            self.current_frame += 0

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
##            if self.prev_x_pos == -1:
##                self.prev_x_pos = self.rect.x
##                self.rect.x += ((self.prev_x_pos - self.boss.rect.x - self.boss.image.get_rect().width/2)/20)
##            else:
##                self.rect.x += (self.rect.x - self.prev_x_pos)
##                self.prev_x_pos = self.rect.x
                self.rect.x += ((self.origin_pos_x - self.boss_origin_pos_x)/25)
                self.rect.y += self.speed
            else:
                self.rect.x += 0
                self.rect.y += 0
        
            
        
        

