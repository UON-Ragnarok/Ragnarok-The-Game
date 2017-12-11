import pygame
from Constants import *

class PlayerShip(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.sprites_list
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.image.load('img/spaceship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = (SCREEN_HEIGHT - self.rect.y)*0.9
        self.pause = False

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.pause == False:
            self.rect.x = pos[0]
            if pos[0] > (SCREEN_WIDTH - self.image.get_rect().width):
                self.rect.x = (SCREEN_WIDTH - self.image.get_rect().width)
