import pygame

class PlayerShip(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height, *group):
        super().__init__(*group)
        self.image = pygame.image.load('img/spaceship.png').convert_alpha()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = self.image.get_rect()
        self.rect.y = (self.screen_height - self.rect.y)*0.9
        self.pause = False

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.pause == False:
            self.rect.x = pos[0]
            if pos[0] > (self.screen_width - self.image.get_rect().width):
                self.rect.x = (self.screen_width - self.image.get_rect().width)





