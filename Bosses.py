import pygame


class Boss(pygame.sprite.Sprite):

    forward = True
    RED = (255,0,0)
    GREEN = (0,255,0)
    def __init__(self, boss_id, screen, screen_width, boss_image, speed, current_level, *groups):
        super().__init__(*groups)
        self.boss_id = boss_id
        self.screen = screen
        self.image = boss_image
        self.range = screen_width
        self.speed = speed
        self.health = 10 * current_level
        self.total_health = self.health
        self.rect = self.image.get_rect()

    # update the boss
    def update(self):

        if self.forward:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        # if the boss go out of the screen
        if self.rect.x + self.image.get_rect().width > self.range - 50 or self.rect.x < 50:
            
            self.forward = not self.forward
        # print the hp
        pygame.draw.line(self.screen,self.RED,(self.rect.x + 10,self.rect.y - 10),(self.rect.x+self.image.get_rect().width -10,self.rect.y -10),8)

        pygame.draw.line(self.screen,self.GREEN,(self.rect.x + 10,self.rect.y - 10),(self.rect.x+(self.image.get_rect().width -10)* (self.health/self.total_health),self.rect.y -10),8)
     
    # if hit boss health -1
    def is_hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

class Boss_Bullet(pygame.sprite.Sprite):
    bullet_speed=3
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

    # different bullets with different bosses
    def update(self):

        if self.boss_id == 1:
            
##            if self.prev_x_pos == -1:
##                self.prev_x_pos = self.rect.x
##                self.rect.x += ((self.prev_x_pos - self.boss.rect.x - self.boss.image.get_rect().width/2)/20)
##            else:
##                self.rect.x += (self.rect.x - self.prev_x_pos)
##                self.prev_x_pos = self.rect.x


            self.rect.x += ((self.origin_pos_x - self.boss_origin_pos_x)/25)
            self.rect.y += self.speed
        
            
        
        

