import pygame
from Constants import *

class PlayerShip(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.sprites_list
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.spaceship_img
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT *0.95
        self.pause = False

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.pause == False:
            self.rect.x = pos[0]
            if self.rect.right >= SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
