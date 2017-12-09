import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, health, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('img/mob.png').convert_alpha()
        self.speed = speed
        self.health = health
        self.rect = self.image.get_rect()
        self.pause = False

    def update(self):
        if self.pause == False:
            self.rect.y += self.speed
        else:
            self.rect.y += 0

class Meteor(pygame.sprite.Sprite):
    def __init__(self, speed, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('img/meteor.png').convert_alpha()
        self.speed = speed
        self.rect = self.image.get_rect()
        self.pause = False

    def update(self):
        if self.pause == False:
            self.rect.y += self.speed
        else:
            self.rect.y += 0
	
class mob(Enemy):
    pass
	
	
		

