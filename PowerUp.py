import pygame

class PowerUp(pygame.sprite.Sprite):

    def __init__(self, power_ups_id, power_ups_id_list, images, *group):
        super().__init__(*group)
        self.power_ups_id = power_ups_id
        self.power_ups_id_list = power_ups_id_list
        self.images = images
        self.index = 0
        self.image = self.images[self.power_ups_id_list.index(self.power_ups_id)][self.index]
        self.rect = self.image.get_rect()
        self.animation_frames = 10
        self.current_frame = 0
        self.speed = 5
        self.pause = False

    def update(self):
        if self.pause == False:
            self.current_frame += 1
            if self.current_frame >= self.animation_frames:
                self.current_frame = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.power_ups_id_list.index(self.power_ups_id)][self.index]
            self.rect.y += self.speed
        else:
            self.current_frame += 0
            self.rect.y += 0
