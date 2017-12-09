import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.sprites_list
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.ship_image
        self.rect = self.image.get_rect()
        self.rect.y = (self.screen_height - self.rect.y)*0.9
        self.pause = False

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.pause == False:
            self.rect.x = pos[0]
            if pos[0] > (self.screen_width - self.image.get_rect().width):
                self.rect.x = (self.screen_width - self.image.get_rect().width)

class Mob(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.sprites_list
        # need another group, what am i suppose to do?
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.enemy_image
        self.rect = self.image.get_rect()
        self.x = 10 + 100*i
        self.y = -50

    def update(self):
        self.rect.y += self.speed
