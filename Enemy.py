import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_location, speed):
        super().__init__()
        self.image = image_location
        self.speed = speed
        self.rect = self.image.get_rect()
        self.image.set_colorkey([255,255,255])

    def update(self):
        self.rect.y += self.speed