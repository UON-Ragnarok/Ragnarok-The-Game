import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([5,10])
        self.image.fill([255,255,255]) #black bullet, place holder, need to find image or something

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5