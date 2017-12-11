import pygame
from settings import *

class Intro():
    pygame.init()

    def __init__(self, screen, intro_music):
        self.x = 0
        self.y = 0
        self.screen = screen
        self.menu_background = pygame.image.load('img/main_menu_bg.jpg').convert()
        self.title = pygame.image.load('img/Ragnarok_logo.png').convert_alpha()
        self.start_button_image = pygame.image.load('img/start_button.png').convert()
        self.about_button_image = pygame.image.load('img/about_button.png').convert()
        self.back_button_image = pygame.image.load('img/back_button.png').convert()
        self.mute_button_image = pygame.transform.scale(pygame.image.load('img/mute.png').convert_alpha(), (50, 50))
        self.volume_button_image = pygame.transform.scale(pygame.image.load('img/volume.png').convert_alpha(), (50, 50))
        self.spaceship_image = pygame.image.load('img/spaceship.png').convert_alpha()
        self.mob_image = pygame.image.load('img/mob.png').convert_alpha()
        self.meteor_image = pygame.image.load('img/meteor.png').convert_alpha()
        self.thor_image = pygame.image.load('img/thor.png').convert_alpha()
        self.power_up_image = pygame.image.load('img/PowerUps/A1.png').convert_alpha()
        self.intro_music = intro_music

        self.menu_background_x = 0
        self.sb_top_left_x = SCREEN_WIDTH / 2 - self.start_button_image.get_rect().width / 2
        self.sb_top_left_y = SCREEN_HEIGHT / 2
        self.mb_top_left_y = 620
        self.bb_top_left_x = SCREEN_WIDTH / 2 - self.back_button_image.get_rect().width / 2
        self.mb_top_left_x = 130
        self.ss_top_left_x = 50
        self.ss_top_left_y = 50

        self.sb_width, self.sb_height = self.start_button_image.get_rect().size  # start image size (width, height)
        self.ab_width, self.ab_height = self.about_button_image.get_rect().size  # about image size
        self.bb_width, self.bb_height = self.back_button_image.get_rect().size  # back image size
        self.mb_width, self.mb_height = self.mute_button_image.get_rect().size  # mute image size
        # self.vb_width, self.vb_height = self.volume_button_image.get_rect().size  # mute image size , not in use

        self.ss_height = self.spaceship_image.get_rect().height
        self.mo_height = self.mob_image.get_rect().height
        self.mt_height = self.meteor_image.get_rect().height
        # self.th_height = self.thor_image.get_rect().height , not in use
        self.pw_height = self.power_up_image.get_rect().height

        pygame.mixer.Channel(0).get_busy()
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.intro_music),-1)
        pygame.mixer.Channel(0).set_volume(0.3)

        #self.show_intro()
        main = True
        about = False
        mute = False
        unmute = True

        while True:
            self.click_event()
            relative_x = self.menu_background_x % self.menu_background.get_rect().width
            self.draw_img(self.menu_background, relative_x - self.menu_background.get_rect().width, 0)
            if relative_x < SCREEN_WIDTH:
                self.draw_img(self.menu_background, relative_x, 0)
            self.menu_background_x += -0.2
            if main:
                self.main_menu()
                if self.start_button_image.get_rect(topleft=(self.sb_top_left_x, self.sb_top_left_y)).collidepoint(self.x, self.y):
                    pygame.time.wait(100)
                    break
                if self.about_button_image.get_rect(topleft = (self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)).collidepoint(self.x, self.y):
                    main = False
                    about = True
                if unmute:
                    self.unmute()
                    if self.volume_button_image.get_rect(topleft=(self.mb_top_left_x, self.mb_top_left_y)).collidepoint(self.x, self.y):
                        mute = True
                        unmute = False
                if mute:
                    self.mute()
                    if self.mute_button_image.get_rect(topleft=(self.mb_top_left_x, self.mb_top_left_y)).collidepoint(self.x, self.y):
                        mute = False
                        unmute = True
            if about:
                self.about()
                if self.back_button_image.get_rect(topleft = (self.bb_top_left_x, self.sb_top_left_y + 300)).collidepoint(self.x, self.y):
                    main = True
                    about = False

            pygame.display.flip()

    def show_intro(self):
        main = True
        about = False
        # setting = False  # not change, no use
        m_pause = True
        s_pause = True

        def mute():
            if m_pause == True:
                self.draw_img(self.volume_button_image, self.mb_top_left_x, self.mb_top_left_y)
                self.draw_text(40, RED, "MUSIC ON", (200, 635))
            elif m_pause == False:
                self.draw_img(self.mute_button_image, self.mb_top_left_x, self.mb_top_left_y)
                self.draw_text(40, GREY, "MUSIC OFF", (200, 635))


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()

            # --- Looping the background
            relative_x = self.menu_background_x % self.menu_background.get_rect().width
            self.draw_img(self.menu_background, relative_x - self.menu_background.get_rect().width, 0)
            if relative_x < SCREEN_WIDTH:
                self.draw_img(self.menu_background, relative_x, 0)
            self.menu_background_x += -0.2
            if main and not about:
                self.draw_img(self.title, SCREEN_WIDTH / 9, SCREEN_HEIGHT / 6)

            # start button
            if main and self.sb_top_left_x < mouse[0] < self.sb_top_left_x + self.sb_width and self.sb_top_left_y < mouse[1] < self.sb_top_left_y + self.sb_height:
                self.big_start_button_image = pygame.transform.rotozoom(self.start_button_image, 0, 1.2)
                self.draw_img(self.big_start_button_image, self.sb_top_left_x, self.sb_top_left_y)
                self.draw_img(self.about_button_image, self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)
                mute()
                pygame.display.flip()
                if click[0] == 1:
                    pygame.time.wait(100)
                    main = False
                    break

            # mute/ volume button for music setting
            elif main and self.mb_top_left_x < mouse[0] < self.mb_top_left_x + self.mb_width and self.mb_top_left_y < mouse[1] < self.mb_top_left_y + self.mb_width:
                self.big_mute_button_image = pygame.transform.rotozoom(self.mute_button_image, 0, 1.2)
                self.big_volume_button_image = pygame.transform.rotozoom(self.volume_button_image, 0, 1.2)
                self.draw_img(self.start_button_image, self.sb_top_left_x, self.sb_top_left_y)
                self.draw_img(self.about_button_image, self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)
                mute()
                pygame.display.flip()
                if click[0] == 1:
                    pygame.time.wait(100)
                    if m_pause == True:
                        pygame.mixer.Channel(0).pause()
                        m_pause = False
                    else:
                        pygame.mixer.Channel(0).unpause()
                        m_pause = True

            # about button
            elif main and self.sb_top_left_x < mouse[0] < self.sb_top_left_x + self.ab_width and self.sb_top_left_y + 25 + self.ab_height < mouse[1] < self.sb_top_left_y + 25 + self.sb_height + self.ab_height:
                self.big_about_button_image = pygame.transform.rotozoom(self.about_button_image,0,1.2)
                self.draw_img(self.start_button_image, self.sb_top_left_x, self.sb_top_left_y)
                self.draw_img(self.big_about_button_image, self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)
                mute()
                pygame.display.flip()
                if click[0]==1:
                    main = False
                    about = True
                    # setting = False  # not change, no use

            #back button for about
            elif about and self.bb_top_left_x < mouse[0] < self.bb_top_left_x + self.bb_width and self.sb_top_left_y + 300 < mouse[1] < self.sb_top_left_y + 300 + self.bb_height:
                self.draw_img(self.spaceship_image, self.ss_top_left_x, self.ss_top_left_y)
                self.draw_text(20, YELLOW, "Use mouse or trackpad to control", (190, 75))
                self.draw_text(20, YELLOW, "the spacship and destroy Asgard", (190, 85))
                self.draw_img(self.mob_image, self.ss_top_left_x, self.ss_top_left_y + 25 + self.ss_height)
                self.draw_text(20, YELLOW, "Sworn protectors of Asgard,", (190, 175))
                self.draw_text(20, YELLOW, "destroy them to earn points", (190, 185))
                self.draw_img(self.meteor_image, self.ss_top_left_x - 10, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height)
                self.draw_text(20, YELLOW, "Meteorites are indestructable,", (190, 290))
                self.draw_text(20, YELLOW, "avoid them at all cost", (190, 300))
                self.draw_img(self.power_up_image, self.ss_top_left_x, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height + 25 + self.mt_height)
                self.draw_text(20, YELLOW, "Collect to gain awesome powers", (190, 410))
                self.draw_img(self.thor_image, self.ss_top_left_x - 50, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height + 25 + self.mt_height + 25 + self.pw_height)
                self.draw_text(60, YELLOW, "???", (190, 590))
                self.draw_img(self.back_button_image, self.bb_top_left_x, self.sb_top_left_y + 300)
                pygame.display.flip()
                if click[0] == 1:
                    pygame.time.wait(100)
                    main = True
                    about = False
                    # setting = False  # not change, no use

            else:
                if main:
                    self.draw_img(self.start_button_image, self.sb_top_left_x, self.sb_top_left_y)
                    self.draw_img(self.about_button_image, self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)
                    mute()  # there is no mute button why need this?
                elif about:
                    self.draw_img(self.spaceship_image, self.ss_top_left_x, self.ss_top_left_y)
                    self.draw_text(20, YELLOW, "Use mouse or trackpad to control", (190, 75))
                    self.draw_text(20, YELLOW, "the spacship and destroy Asgard", (190, 85))
                    self.draw_img(self.mob_image, self.ss_top_left_x, self.ss_top_left_y + 25 + self.ss_height)
                    self.draw_text(20, YELLOW, "Sworn protectors of Asgard,", (190, 175))
                    self.draw_text(20, YELLOW, "destroy them to earn points", (190, 185))
                    self.draw_img(self.meteor_image, self.ss_top_left_x - 10, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height)
                    self.draw_text(20, YELLOW, "Meteorites are indestructable,", (190, 290))
                    self.draw_text(20, YELLOW, "avoid them at all cost", (190, 300))
                    self.draw_img(self.power_up_image, self.ss_top_left_x, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height + 25 + self.mt_height)
                    self.draw_text(20, YELLOW, "Collect to gain awesome powers", (190, 410))
                    self.draw_img(self.thor_image, self.ss_top_left_x - 50, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height + 25 + self.mt_height + 25 + self.pw_height)
                    self.draw_text(60, YELLOW, "???", (190, 590))
                    self.draw_img(self.back_button_image, self.bb_top_left_x, self.sb_top_left_y + 300)
                pygame.display.flip()

    def main_menu(self):
        self.draw_img(self.title, SCREEN_WIDTH / 9, SCREEN_HEIGHT / 6)
        self.draw_img(self.start_button_image, self.sb_top_left_x, self.sb_top_left_y)
        self.mouse_over_enlarge(self.start_button_image, self.sb_top_left_x, self.sb_top_left_y)
        #if self.start_button_image.get_rect(topleft = (self.sb_top_left_x, self.sb_top_left_y)).collidepoint(pygame.mouse.get_pos()):
        #    self.big_start_button_image = pygame.transform.rotozoom(self.start_button_image, 0, 1.2)
        #    self.draw_img(self.big_start_button_image, self.sb_top_left_x, self.sb_top_left_y)
        self.draw_img(self.about_button_image, self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)
        self.mouse_over_enlarge(self.about_button_image, self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)
        #if self.about_button_image.get_rect(topleft = (self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)).collidepoint(pygame.mouse.get_pos()):
        #    self.big_about_button_image = pygame.transform.rotozoom(self.about_button_image, 0, 1.2)
        #    self.draw_img(self.big_about_button_image, self.sb_top_left_x, self.sb_top_left_y + 25 + self.sb_height)

    def about(self):
        self.draw_img(self.spaceship_image, self.ss_top_left_x, self.ss_top_left_y)
        self.draw_text(20, YELLOW, "Use mouse or trackpad to control", (190, 75))
        self.draw_text(20, YELLOW, "the spacship and destroy Asgard", (190, 85))
        self.draw_img(self.mob_image, self.ss_top_left_x, self.ss_top_left_y + 25 + self.ss_height)
        self.draw_text(20, YELLOW, "Sworn protectors of Asgard,", (190, 175))
        self.draw_text(20, YELLOW, "destroy them to earn points", (190, 185))
        self.draw_img(self.meteor_image, self.ss_top_left_x - 10, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height)
        self.draw_text(20, YELLOW, "Meteorites are indestructable,", (190, 290))
        self.draw_text(20, YELLOW, "avoid them at all cost", (190, 300))
        self.draw_img(self.power_up_image, self.ss_top_left_x, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height + 25 + self.mt_height)
        self.draw_text(20, YELLOW, "Collect to gain awesome powers", (190, 410))
        self.draw_img(self.thor_image, self.ss_top_left_x - 50, self.ss_top_left_y + 25 + self.ss_height + 25 + self.mo_height + 25 + self.mt_height + 25 + self.pw_height)
        self.draw_text(60, YELLOW, "???", (190, 590))
        self.draw_img(self.back_button_image, self.bb_top_left_x, self.sb_top_left_y + 300)
        self.mouse_over_enlarge(self.back_button_image, self.bb_top_left_x, self. sb_top_left_y + 300)
#        if self.back_button_image.get_rect(topleft = (self.bb_top_left_x, self.sb_top_left_y + 300)).collidepoint(pygame.mouse.get_pos()):
#            self.big_back_button_image = pygame.transform.rotozoom(self.back_button_image, 0, 1.2)
#            self.draw_img(self.big_back_button_image, self.bb_top_left_x, self.sb_top_left_y + 300)

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
                    self.x, self.y = event.pos
                #    if img.collideoint(event.pos): ???

    def mute(self):
        pygame.mixer.Channel(0).pause()
        self.draw_img(self.volume_button_image, self.mb_top_left_x, self.mb_top_left_y)
        self.draw_text(40, RED, "MUSIC ON", (200, 635))

    def unmute(self):
        pygame.mixer.Channel(0).unpause()
        self.draw_img(self.mute_button_image, self.mb_top_left_x, self.mb_top_left_y)
        self.draw_text(40, GREY, "MUSIC OFF", (200, 635))

    def draw_img(self, img, x, y, area = None):
        self.screen.blit(img, (x, y), area)

    def draw_text(self, size, color, text, text_rect):
        font = pygame.font.SysFont("'freesansbold.ttf'", size, True)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, text_rect)

##        clock.tick(FPS)