import pygame
from Constants import *
from os import path

#pygame.init()
#game_folder = path.dirname(__file__)
#img_folder = path.join(game_folder, 'img')
#IMG_NAMES 	= ["menu_background", "title", "start_button", "about_button", "back_button", "mute_button", "volume_button",
#				"player_ship", "mob", "meteor", "thor", "powerup"]
#IMGS 		= {f"{name}_img": pygame.image.load(path.join(img_folder, f"{name}.png")).convert_alpha()
#				for name in IMG_NAMES}

class Intro:

    def __init__(self, game, screen):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.game = game
        self.menu_background_img = pygame.image.load(path.join(img_folder, 'menu_background.png')).convert()
        self.title = pygame.image.load(path.join(img_folder, 'title.png')).convert_alpha()
        self.start_button_img = pygame.image.load(path.join(img_folder, 'start_button.png')).convert()
        self.about_button_img = pygame.image.load(path.join(img_folder, 'about_button.png')).convert()
        self.back_button_img = pygame.image.load(path.join(img_folder, 'back_button.png')).convert()
        self.mute_button_img = pygame.image.load(path.join(img_folder, 'mute_button.png')).convert_alpha()
        self.volume_button_img = pygame.image.load(path.join(img_folder, 'volume_button.png')).convert_alpha()
        self.player_ship_img = pygame.image.load(path.join(img_folder, 'player_ship.png')).convert_alpha()
        self.mob_img = pygame.image.load(path.join(img_folder, 'mob.png')).convert_alpha()
        self.meteor_img = pygame.image.load(path.join(img_folder, 'meteor.png')).convert_alpha()
        self.thor_img = pygame.image.load(path.join(img_folder, 'thor.png')).convert_alpha()
        self.powerup_img = pygame.image.load(path.join(img_folder, 'powerup.png')).convert_alpha()
#        IMG_NAMES = ["menu_background", "title", "start_button", "about_button", "back_button", "mute_button",
#                    "volume_button", "player_ship", "mob", "meteor", "thor", "powerup"]
#        self.IMGS = {f"{name}_img": pygame.image.load(path.join(img_folder, f"{name}.png")).convert_alpha() for name in IMG_NAMES}
        self.screen = screen
        self.music_on_off_img = [self.mute_button_img.copy(), self.volume_button_img.copy()]
        self.mute_text = ["MUSIC ON", "MUSIC OFF"]
        self.is_mute = False
        self.on_off = 0
        self.click_x = 0  # to store the x_pos of click
        self.click_y = 0  # to store the y_pos of click

        self.menu_background_img_x = 0
        self.sb_top_left_x = SCREEN_WIDTH / 2 - self.start_button_img.get_rect().centerx
        self.sb_top_left_y = SCREEN_HEIGHT / 2
        self.mb_top_left_y = 620
        self.bb_top_left_x = SCREEN_WIDTH / 2 - self.back_button_img.get_rect().centerx
        self.mb_top_left_x = 130
        self.ss_top_left_x = 50
        self.ss_top_left_y = 50

        self.sb_width, self.sb_height = self.start_button_img.get_rect().size  # start image size (width, height)
        self.ab_width, self.ab_height = self.about_button_img.get_rect().size  # about image size
        self.bb_width, self.bb_height = self.back_button_img.get_rect().size  # back image size
        self.mb_width, self.mb_height = self.mute_button_img.get_rect().size  # mute/volume image size

        self.ss_height = self.player_ship_img.get_rect().height
        self.mo_height = self.mob_img.get_rect().height
        self.mt_height = self.meteor_img.get_rect().height
        self.pw_height = self.powerup_img.get_rect().height

        main = True
        about = False
        while True:
            self.click_event()
            relative_x = self.menu_background_img_x % self.menu_background_img.get_rect().width
            self.draw_img(self.menu_background_img, relative_x - self.menu_background_img.get_rect().width, 0)
            if relative_x < SCREEN_WIDTH:
                self.draw_img(self.menu_background_img, relative_x, 0)
            self.menu_background_img_x += -0.2
            if main:
                # It will start off loading the main page
                self.main_menu()
                if self.start_button_img.get_rect(topleft=(self.sb_top_left_x, self.sb_top_left_y)).collidepoint(self.click_x, self.click_y):
                    # If clicked the start button, exit this loop and enter the game
                    pygame.time.wait(100)
                    break
                if self.about_button_img.get_rect(topleft=(self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)).collidepoint(self.click_x, self.click_y):
                    # If clicked the about button, bring you to the about / game explaintion page
                    main = False
                    about = True
                self.bg_music()  # music mute/ volume down and up
            if about:
                self.about()
                self.menu_background_img_x += -0.7
                if self.back_button_img.get_rect(topleft=(self.bb_top_left_x, self.sb_top_left_y + 300)).collidepoint(self.click_x, self.click_y):
                    main = True
                    about = False

            pygame.display.flip()


    def main_menu(self):
        # draw and write a bunck of stuff
        self.draw_img(self.title, SCREEN_WIDTH / 9, SCREEN_HEIGHT / 6)
        self.draw_img(self.start_button_img, self.sb_top_left_x, self.sb_top_left_y)
        self.mouse_over_enlarge(self.start_button_img, self.sb_top_left_x, self.sb_top_left_y)
        self.draw_img(self.about_button_img, self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)
        self.mouse_over_enlarge(self.about_button_img, self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)

    def about(self):
        # draw and write a bunck of stuff
        self.draw_img(self.player_ship_img, self.ss_top_left_x, self.ss_top_left_y)
        self.draw_text(20, YELLOW, "Use mouse or trackpad to control", (190, 75))
        self.draw_text(20, YELLOW, "the spaceship and destroy Asgard", (190, 85))
        self.draw_img(self.mob_img, self.ss_top_left_x, self.ss_top_left_y + 25 + self.ss_height)
        self.draw_text(20, YELLOW, "Sworn protectors of Asgard,", (190, 175))
        self.draw_text(20, YELLOW, "destroy them to earn points", (190, 185))
        self.draw_img(self.meteor_img, self.ss_top_left_x - 10, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height)
        self.draw_text(20, YELLOW, "Meteorites are indestructable,", (190, 290))
        self.draw_text(20, YELLOW, "avoid them at all cost", (190, 300))
        self.draw_img(self.powerup_img, self.ss_top_left_x, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height + 25 + self.mt_height)
        self.draw_text(20, YELLOW, "Collect to gain awesome powers", (190, 410))
        self.draw_img(self.thor_img, self.ss_top_left_x - 50, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height + 25 + self.mt_height + 25 + self.pw_height)
        self.draw_text(60, YELLOW, "???", (190, 590))
        self.draw_img(self.back_button_img, self.bb_top_left_x, self.sb_top_left_y + 300)
        self.mouse_over_enlarge(self.back_button_img, self.bb_top_left_x, self. sb_top_left_y + 300)

    def mouse_over_enlarge(self, img_in, pos_x, pos_y):
        if img_in.get_rect(topleft=(pos_x, pos_y)).collidepoint(pygame.mouse.get_pos()):
            self.big_img_in = pygame.transform.rotozoom(img_in, 0, 1.2)
            self.draw_img(self.big_img_in, pos_x, pos_y)

    def click_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                # Get the x, y postions of the mouse left click
                    self.click_x, self.click_y = event.pos

    def bg_music(self):
        if self.game.is_mute:
            self.on_off = 1
        else:
            self.on_off = 0
        self.draw_img(self.music_on_off_img[self.on_off], self.mb_top_left_x, self.mb_top_left_y)
        self.draw_text(40, WHITE, self.mute_text[self.on_off], (200, 635))
        if self.music_on_off_img[self.on_off].get_rect(topleft=(self.mb_top_left_x, self.mb_top_left_y)).collidepoint(self.click_x, self.click_y):
            # click on the image will either turn the volume down or up/ silening it
            self.on_off = (self.on_off + 1) % 2
            self.game.is_mute = not self.game.is_mute
            self.game.set_volume(not self.game.is_mute)
            self.click_x, self.click_y = 0, 0  # reset click position, should actually really do for all(after the click start / about/ back) buttons click

    def draw_img(self, img, x, y, area = None):
        self.screen.blit(img, (x, y), area)

    def draw_text(self, size, color, text, text_rect):
        font = pygame.font.SysFont("'freesansbold.ttf'", size, True)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, text_rect)
