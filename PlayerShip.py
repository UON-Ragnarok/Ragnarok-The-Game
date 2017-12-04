import pygame

class PlayerShip(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height, image_location, *group):
        super().__init__(*group)
        self.image = image_location
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = self.image.get_rect()
        self.rect.y = (self.screen_height - self.rect.y)*0.95
        self.image.set_colorkey([255,255,255])          #make bg transparent
        self.pause = False

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.pause == False:
            self.rect.x = pos[0]
            if pos[0] > (self.screen_width - self.image.get_rect().width):
                self.rect.x = (self.screen_width - self.image.get_rect().width)





