import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x_pos, y_pos, speed):
        self.groups = game.bullet_list, game.sprites_list
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface([5,10])
        self.image.fill([255,255,255]) #black bullet, place holder, need to find image or something
        self.rect = self.image.get_rect()
        self.rect.centerx  = x_pos
        self.rect.bottom  = y_pos
        self.speed = speed
        self.pause = False

    def update(self):
        if self.rect.bottom < 0:
        # if bullets goes off screen it remove from all sprites groups
            self.kill()
        if self.pause == False:
            self.rect.y -= self.speed
        else:
            self.rect.y += 0
