import pygame

class PlayerShip(pygame.sprite.Sprite):

    def __init__(self, screen_width, image_location):
        super().__init__()
        self.image = image_location
        self.screen = screen_width
        self.rect = self.image.get_rect()
        self.image.set_colorkey([255,255,255])          #make bg transparent
        self.pause = False

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.pause == False:
            self.rect.x = pos[0]
            if pos[0] > (self.screen - self.image.get_rect().width):
                self.rect.x = (self.screen - self.image.get_rect().width)





