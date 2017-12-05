import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_location, speed, health, *groups):
        super().__init__(*groups)
        self.image = image_location
        self.speed = speed
        self.health = health
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed

class Meteor(Enemy):
	pass
	
class mob(Enemy):
	pass
	
	
		

