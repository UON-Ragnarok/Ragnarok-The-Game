import pygame

class Boss(pygame.sprite.Sprite):
    def __init__(self, width, image_location, speed, health, *groups):
        super().__init__(*groups)
        self.image = image_location
        self.image.set_colorkey((255,255,255))
        self.range = width
        self.speed = speed
        self.health = health
        self.rect = self.image.get_rect()

    def update(self):
        pass
#        self.rect.x += self.speed
#        if self.rect.left > self.range or self.rect.right < 1:
#            self.speed = -self.speed

class hammer(pygame.sprite.Sprite):
    def __init__(self, image_location):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_location
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = 100
        self.rect.y = random.randrange(-150, -100)
        self.speedy = 5
        self.speedx = 5
        self.rot = 0
        self.rot_speed = 10
        self.last_update = pygame.time.get_ticks()
	
    def update(self):
        self.rotate()
	
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
