import pygame as pg
from settings import *

# Sprite classes for the Game
class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((40, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width / 2
        self.rect.bottom = screen_height * 0.98

    def update(self):
        pos = pg.mouse.get_pos()
        self.rect.x = pos[0]
        Bullet(self.game, self.rect.centerx, self.rect.y, bullet_speed)
        if self.rect.right == screen_width:  # only work with images because of the get_rect()
            self.rect.right = screen_width

class Bullet(pg.sprite.Sprite):
    def __init__(self, game, x_pos, y_pos, speed):
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface([5,10])
        self.image.fill([255,255,255])   # white bullet, place holder, need to find image or something
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.bottom = x_pos, y_pos
        self.speed = speed

    def update(self):
        pass  # dont know what the suitation of it at the moment
        # self.rect.y -= self.speed
        # if self.rect.bottom < 0 :
        #        self.kill()

class Mob(pg.sprite.Sprite):
    def __init__(self, game, speed, pos):  # need to add the game(self, game)
        self.groups = game.all_sprites, game.all_mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = game.enemy_image
        self.image = pg.Surface((50, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = 10 + 100*pos
        self.rect.y = -50

    def update(self):
        self.rect.y += self.speed
