import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, health, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('img/mob.png').convert_alpha()
        self.speed = speed
        self.health = health
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed

class Meteor(pygame.sprite.Sprite):
    def __init__(self, speed, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('img/meteor.png').convert_alpha()
        self.speed = speed
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed
	
class mob(Enemy):
	pass
	
	
		

