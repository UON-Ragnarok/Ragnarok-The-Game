import pygame

class PowerUp(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height, speed, *group):
        super().__init__(*group)
        self.images_list = ["img/PowerUps/" + str(number) + ".png" for number in range(1,6)]
        self.images = []
        #Load all images
        for file in self.images_list:
            image = pygame.image.load(file).convert_alpha()
            image = pygame.transform.scale(image, (50,50))
            self.images.append(image)

        self.index = 0
        self.image = self.images[self.index]
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = self.image.get_rect()

        self.animation_frames = 10
        self.current_frame = 0

        self.speed = speed

        self.pause = False

    def update(self):
        if self.pause == False:
            self.current_frame += 1
            if self.current_frame >= self.animation_frames:
                self.current_frame = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]
            self.rect.y += self.speed
        else:
            self.current_frame += 0
            self.rect.y += 0

