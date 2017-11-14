import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_location):
        super().__init__()
        self.image = image_location
        self.rect = self.image.get_rect()
        self.image.set_colorkey([255,255,255])