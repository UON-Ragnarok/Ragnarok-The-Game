import pygame
from Constants import *

class Intro():
    pygame.init()

    def __init__(self, screen, screen_width, screen_height, intro_music):
        self.screen = screen
        self.menu_background = pygame.image.load('img/main_menu_bg.jpg').convert()
        self.screen_width = screen_width
        self.screen_height = screen_height
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
        self.sb_top_left_x = self.screen_width / 2 - self.start_button_image.get_rect().width / 2
        self.sb_top_left_y = self.screen_height / 2
        self.mb_top_left_y = 620
        self.bb_top_left_x = self.screen_width / 2 - self.back_button_image.get_rect().width / 2
        self.mb_top_left_x = 130
        self.ss_top_left_x = 50
        self.ss_top_left_y = 50

        self.sb_width, self.sb_height = self.start_button_image.get_rect().size  # start image size (width, height)
        self.ab_width, self.ab_height = self.about_button_image.get_rect().size  # about image size
        self.bb_width, self.bb_height = self.back_button_image.get_rect().size  # back image size
        self.mb_width, self.mb_height = self.mute_button_image.get_rect().size  # mute image size
        self.vb_width, self.vb_height = self.volume_button_image.get_rect().size  # mute image size

        self.ss_width, self.ss_height = self.spaceship_image.get_rect().size
        self.mo_width, self.mo_height = self.mob_image.get_rect().size
        self.mt_width, self.mt_height = self.meteor_image.get_rect().size
        self.th_width, self.th_height = self.thor_image.get_rect().size
        self.pw_width, self.pw_height = self.power_up_image.get_rect().size
        self.show_intro()

    def show_intro(self):
        pass

    def show_about(self):
        pass

    def back(self):
        pass

    def mute(self):
        pass

    def unmute(self):
        pass



    def show_intro(self, screen):
        main = True
        about = False
        setting = False
        m_pause = True
        s_pause = True


        if not pygame.mixer.Channel(0).get_busy():
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.intro_music),-1)
            pygame.mixer.Channel(0).set_volume(0.3)

        def mute():
                if m_pause == True:
                    screen.blit(self.volume_button_image, [mb_top_left_x, mb_top_left_y])
                    screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 40, True).render("MUSIC ON", 1, (91, 109, 131)), (200, 635))
                elif m_pause == False:
                    screen.blit(self.mute_button_image, [mb_top_left_x, mb_top_left_y])
                    screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 40, True).render("MUSIC OFF", 1, (91, 109, 131)), (200, 635))

        def draw_text(size, text, text_rect):
            font = pygame.font.SysFont("'freesansbold.ttf'", size, True)
            text_surface = font.render(text, True, (240,255,0))
            screen.blit(text_surface, text_rect)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()
          #  pressedkeys = pygame.key.get_pressed()

            # --- Looping the background
            relative_x = menu_background_x % self.menu_background.get_rect().width
            screen.blit(self.menu_background, [relative_x - self.menu_background.get_rect().width, 0])
            if relative_x < self.screen_width:
                screen.blit(self.menu_background, [relative_x, 0])
            menu_background_x += -0.2
            if main and not about:
                screen.blit(self.title, [self.screen_width / 9, self.screen_height / 6])


            # start button
            if main and sb_top_left_x < mouse[0] < sb_top_left_x + sb_width and sb_top_left_y < mouse[1] < sb_top_left_y + sb_height:
                self.big_start_button_image = pygame.transform.rotozoom(self.start_button_image,0,1.2)
                screen.blit(self.big_start_button_image, [sb_top_left_x, sb_top_left_y])
                screen.blit(self.about_button_image, [sb_top_left_x, sb_top_left_y + 25 + sb_height])
                mute()
                pygame.display.flip()
                if click[0] == 1:
                    pygame.time.wait(100)
                    main = False
                    break

            # mute/ volume button for music setting
            elif main and mb_top_left_x < mouse[0] < mb_top_left_x + mb_width and mb_top_left_y < mouse[1] < mb_top_left_y + mb_height:
                self.big_mute_button_image = pygame.transform.rotozoom(self.mute_button_image,0,1.2)
                self.big_volume_button_image = pygame.transform.rotozoom(self.volume_button_image,0,1.2)
                screen.blit(self.start_button_image, [sb_top_left_x, sb_top_left_y])
                screen.blit(self.about_button_image, [sb_top_left_x, sb_top_left_y + 25 + sb_height])
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
            elif main and sb_top_left_x < mouse[0] < sb_top_left_x+ab_width and sb_top_left_y + 25 + ab_height < mouse[1] < sb_top_left_y + 25 + sb_height + ab_height:
                self.big_about_button_image = pygame.transform.rotozoom(self.about_button_image,0,1.2)
                screen.blit(self.start_button_image, [sb_top_left_x, sb_top_left_y])
                screen.blit(self.big_about_button_image, [sb_top_left_x, sb_top_left_y + 25 + sb_height])
                mute()
                pygame.display.flip()
                if click[0]==1:
                    main = False
                    about = True
                    setting = False

            def about(


            #back button for about
            elif about and bb_top_left_x < mouse[0] < bb_top_left_x + bb_width and sb_top_left_y + 300 < mouse[1] < sb_top_left_y + 300 + bb_height:
                self.big_back_button_image = pygame.transform.rotozoom(self.back_button_image,0,1.2)
                screen.blit(self.spaceship_image, [ss_top_left_x, ss_top_left_y])
                screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Use mouse or trackpad to control", 1, (91, 109, 131)), (190, 75))
                screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("the spacship and destroy Asgard", 1, (91, 109, 131)), (190, 85))
                screen.blit(self.mob_image, [ss_top_left_x, ss_top_left_y + 25 + ss_height])
                screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Sworn protectors of Asgard,", 1, (91, 109, 131)), (190, 175))
                screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("destroy them to earn points", 1, (91, 109, 131)), (190, 185))
                screen.blit(self.meteor_image, [ss_top_left_x - 10, ss_top_left_y + 25 + ss_height + 25 + mo_height])
                screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Meteorites are indestructable,", 1, (91, 109, 131)), (190, 290))
                screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("avoid them at all cost", 1, (91, 109, 131)), (190, 300))
                screen.blit(self.power_up_image, [ss_top_left_x, ss_top_left_y + 25 + ss_height + 25 + mo_height + 25 + mt_height])
                screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 20, True).render("Collect to gain awesome powers", 1, (91, 109, 131)), (190, 410))
                screen.blit(self.thor_image, [ss_top_left_x - 50, ss_top_left_y + 25 + ss_height + 25 + mo_height + 25 + mt_height + 25 + pw_height])
                screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 60, True).render("???", 1, (91, 109, 131)), (190, 590))
                screen.blit(self.big_back_button_image, [bb_top_left_x, sb_top_left_y + 300])
                pygame.display.flip()
                if click[0] == 1:
                    pygame.time.wait(100)
                    main = True
                    about = False
                    setting = False

            else:
                if main:
                    screen.blit(self.start_button_image, [sb_top_left_x, sb_top_left_y])
                    screen.blit(self.about_button_image, [sb_top_left_x, sb_top_left_y + 25 + sb_height])
                    mute()  # there is no mute button why need this?
                elif about:
                    screen.blit(self.spaceship_image, [ss_top_left_x, ss_top_left_y])
                    draw_text(20, "Use mouse or trackpad to control", (190, 75))
                    draw_text(20, "the spacship and destroy Asgard", (190, 85))
                    screen.blit(self.mob_image, [ss_top_left_x, ss_top_left_y + 25 + ss_height])
                    draw_text(20, "Sworn protectors of Asgard,", (190, 175))
                    draw_text(20, "destroy them to earn points", (190, 185))
                    screen.blit(self.meteor_image, [ss_top_left_x - 10, ss_top_left_y + 25 + ss_height + 25 + mo_height])
                    draw_text(20, "Meteorites are indestructable,", (190, 290))
                    draw_text(20, "avoid them at all cost", (190, 300))
                    screen.blit(self.power_up_image, [ss_top_left_x, ss_top_left_y + 25 + ss_height + 25 + mo_height + 25 + mt_height])
                    draw_text(20, "Collect to gain awesome powers", (190, 410))
                    screen.blit(self.thor_image, [ss_top_left_x - 50, ss_top_left_y + 25 + ss_height + 25 + mo_height + 25 + mt_height + 25 + pw_height])
                    draw_text(60, "???", (190, 590))
                    screen.blit(self.back_button_image, [bb_top_left_x,sb_top_left_y + 300 ]);
                pygame.display.flip()


##        clock.tick(FPS)
