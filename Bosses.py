import pygame

class Boss(pygame.sprite.Sprite):
    def __init__(self, width, image_location, speed, health, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((150,150))
        self.image.fill((255,255,0))
        self.range = width
        self.speed = speed
        self.health = health
        self.rect = self.image.get_rect()

    def update(self):
        pass
#        self.rect.x += self.speed
#        if self.rect.left > self.range or self.rect.right < 1:
#            self.speed = -self.speed

    def draw_health_bar(surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, GREEN, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)

		
class blot(pygame.sprite.Sprite):
	pass
	
class electric_ball(pygame.sprite.Sprite):

    def __init__(self, game, velocity):
        super(Ball, self).__init__()

        self.image = pygame.Surface((BALL_RADIUS*2, BALL_RADIUS*2))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK, RLEACCEL)
        self.rect = self.image.get_rect()

        screen = pygame.display.get_surface()
        self.area = screen.get_rect().inflate(-GAP*2, 0)

        self.velocity = velocity
        self.game = game
        self.start_to_the = random.choice(['left', 'right'])
        self._draw_ball(BALL_COLOR)
        self.reinit()		


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
