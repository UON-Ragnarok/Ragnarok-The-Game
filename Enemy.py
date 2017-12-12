import pygame
from Constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, health, images, *groups):
        super().__init__(*groups)
        self.images = images
        self.index = 0
        self.image = self.images[self.index]

        self.animation_frames = 5
        self.current_frame = 0

        self.speed = speed
        self.health = health
        self.rect = self.image.get_rect()
        self.pause = False
        self.killed = False
        self.death = False

    def update(self):
        if self.pause == False:
            self.rect.y += self.speed
            if self.death == True:
                self.update_death_animation()
        else:
            self.rect.y += 0
            if self.death == True:
                self.current_frame += 0

    def update_death_animation(self):
        if self.index != 11:
            self.current_frame += 1
            if self.current_frame >= self.animation_frames:
                self.current_frame = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]
            else:
                self.killed = True

class Meteor(pygame.sprite.Sprite):
    def __init__(self, image, speed, *groups):
        super().__init__(*groups)
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect()
        self.pause = False

    def update(self):
        # kiind of duplicate for Game.py line 308
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        if self.pause == False:
            self.rect.y += self.speed
        else:
            self.rect.y += 0
