import pygame


class PlayerShip(pygame.sprite.Sprite):

    def __init__(self, screen_width, image_location):
        super().__init__()
        self.image = image_location
        self.screen = screen_width
        self.rect = self.image.get_rect()
        self.image.set_colorkey([255,255,255])          #make bg transparent


    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if pos[0] > (self.screen - self.image.get_rect().width):
            self.rect.x = (self.screen - self.image.get_rect().width)
	

'''		self.speedx = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -5
		if keystate[pygame.K_RIGHT]:
			self.speedx = 5
		self.rect.x += self.speedx
		if self.rect.right > screen_width:
			self.rect.right = screen_width
		if self.rect.left < 0:
			self.rect.left = 0 '''
			
		
		
