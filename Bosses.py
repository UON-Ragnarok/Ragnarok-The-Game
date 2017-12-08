import pygame
from Bullet import *

class Boss(pygame.sprite.Sprite):

    #List of bullets
    bullet_list = pygame.sprite.Group()
    def __init__(self, screen, screen_width, boss_image, speed, current_level, *groups):
        super().__init__(*groups)
        self.screen = screen
        self.image = boss_image
        self.range = screen_width
        self.speed = speed
        self.health = 10 * current_level
        self.rect = self.image.get_rect()
        

##    def update(self):
####        print("test")bullet_speed = 5
##        bullet_speed = 5
##        bullet = Bullet((self.rect.x + self.image.get_rect().width/2), self.rect.y, bullet_speed, [boss_bullet_list, sprites_list],forward = False)
####        self.fire_bullet()
####        self.bullet_list.draw(self.screen)
####        pygame.display.flip()
##        
    
    def is_hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

##    def fire_bullet(self, bullet_speed = 5):
##
##        bullet = Bullet((self.rect.x + self.image.get_rect().width/2), self.rect.y, bullet_speed, [self.bullet_list],forward = False)
####        pygame.time.set_timer(fire_bullet_event, fire_bullet_delay)
