import pygame

class Intro():
    pygame.init()
    

    def __init__(self, screen,screen_width,screen_height, intro_music):
        self.screen = screen
        self.menu_background = pygame.image.load('img/main_menu_bg.jpg').convert()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title = pygame.image.load('img/Ragnarok_logo.png').convert_alpha()
        self.start_button_image = pygame.image.load('img/start_button.png').convert()
        self.about_button_image = pygame.image.load('img/about_button.png').convert()
        self.back_button_image = pygame.image.load('img/back_button.png').convert()
        self.mute_button_image = pygame.transform.scale(pygame.image.load('img/mute.png').convert_alpha(), (50,50))
        self.volume_button_image = pygame.transform.scale(pygame.image.load('img/volume.png').convert_alpha(), (50,50))
        self.intro_music = intro_music
        
        
    def show_intro(self,screen):
        main = True
        about = False
        setting = False
        m_pause = True
        s_pause = True
        menu_background_x = 0
        sb_top_left_x = self.screen_width / 2 - self.start_button_image.get_rect().width / 2
        sb_top_left_y = self.screen_height / 2
        mb_top_left_y = 620
        bb_top_left_x = self.screen_width / 2 - self.back_button_image.get_rect().width / 2
        mb_top_left_x = 130    
        sb_height = self.start_button_image.get_rect().height
        sb_width = self.start_button_image.get_rect().width
        ab_height = self.about_button_image.get_rect().height
        ab_width = self.about_button_image.get_rect().width
        bb_height = self.back_button_image.get_rect().height
        bb_width = self.back_button_image.get_rect().width 
        mb_height = self.mute_button_image.get_rect().height
        mb_width = self.mute_button_image.get_rect().width
        vb_height = self.volume_button_image.get_rect().height
        vb_width = self.volume_button_image.get_rect().width       
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.intro_music),-1)
        pygame.mixer.Channel(0).set_volume(0.5)
        
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
            menu_background_x += -0.3
            if main and not about:
                screen.blit(self.title, [self.screen_width / 9, self.screen_height / 6])

                
            # start button
            if main and sb_top_left_x < mouse[0] < sb_top_left_x+sb_width and sb_top_left_y < mouse[1] < sb_top_left_y + sb_height:
                self.big_start_button_image = pygame.transform.rotozoom(self.start_button_image,0,1.2)
                screen.blit(self.big_start_button_image, [sb_top_left_x, sb_top_left_y])
                screen.blit(self.about_button_image, [sb_top_left_x, sb_top_left_y + 25 + sb_height])
                if m_pause == True:
                    screen.blit(self.volume_button_image, [mb_top_left_x, mb_top_left_y])
                    screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 40, True).render("MUSIC ON", 1, (91, 109, 131)), (200, 635))
                elif m_pause == False:
                    screen.blit(self.mute_button_image, [mb_top_left_x, mb_top_left_y])
                    screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 40, True).render("MUSIC OFF", 1, (91, 109, 131)), (200, 635))
                pygame.display.flip()
                if click[0] == 1:
                    pygame.time.wait(100)
                    main = False
                    break
                
            # about button
            elif main and sb_top_left_x < mouse[0] < sb_top_left_x+ab_width and sb_top_left_y + 25 + ab_height < mouse[1] < sb_top_left_y + 25 + sb_height + ab_height:
                self.big_about_button_image = pygame.transform.rotozoom(self.about_button_image,0,1.2)
                screen.blit(self.start_button_image, [sb_top_left_x, sb_top_left_y])
                screen.blit(self.big_about_button_image, [sb_top_left_x, sb_top_left_y + 25 + sb_height])
                if m_pause == True:
                    screen.blit(self.volume_button_image, [mb_top_left_x, mb_top_left_y])
                    screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 40, True).render("MUSIC ON", 1, (91, 109, 131)), (200, 635))
                elif m_pause == False:
                    screen.blit(self.mute_button_image, [mb_top_left_x, mb_top_left_y])
                    screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 40, True).render("MUSIC OFF", 1, (91, 109, 131)), (200, 635))
                pygame.display.flip()
                if click[0]==1:
                    main = False
                    about = True
                    setting = False
            
            #back button for about                   
            elif about and bb_top_left_x < mouse[0] < bb_top_left_x + bb_width and sb_top_left_y + 200 < mouse[1] < sb_top_left_y + 200 + bb_height:
                self.big_back_button_image = pygame.transform.rotozoom(self.back_button_image,0,1.2)
                screen.blit(self.big_back_button_image, [bb_top_left_x, sb_top_left_y + 200])
                pygame.display.flip()
                if click[0] == 1:
                    pygame.time.wait(100)
                    main = True
                    about = False
                    setting = False
                    
            # mute/ volume button for music setting
            elif main and mb_top_left_x < mouse[0] < mb_top_left_x + mb_width and mb_top_left_y < mouse[1] < mb_top_left_y + mb_height:
                self.big_mute_button_image = pygame.transform.rotozoom(self.mute_button_image,0,1.2)
                self.big_volume_button_image = pygame.transform.rotozoom(self.volume_button_image,0,1.2)
                screen.blit(self.start_button_image, [sb_top_left_x, sb_top_left_y])
                screen.blit(self.about_button_image, [sb_top_left_x, sb_top_left_y + 25 + sb_height])
                if m_pause == True:
                    screen.blit(self.big_volume_button_image, [mb_top_left_x, mb_top_left_y])
                    screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 40, True).render("MUSIC ON", 1, (91, 109, 131)), (200, 635))
                elif m_pause == False:
                    screen.blit(self.big_mute_button_image, [mb_top_left_x, mb_top_left_y])
                    screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 40, True).render("MUSIC OFF", 1, (91, 109, 131)), (200, 635))
                pygame.display.flip()
                if click[0] == 1:
                    pygame.time.wait(100)
                    if m_pause == True:
                        pygame.mixer.Channel(0).pause()
                        m_pause = False
                    else:
                        pygame.mixer.Channel(0).unpause()
                        m_pause = True
                
            else:
                if main:
                    screen.blit(self.start_button_image, [sb_top_left_x, sb_top_left_y])
                    screen.blit(self.about_button_image, [sb_top_left_x, sb_top_left_y + 25 + sb_height])
                    if m_pause == True:
                        screen.blit(self.volume_button_image, [mb_top_left_x, mb_top_left_y ])
                        screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 40, True).render("MUSIC ON", 1, (91, 109, 131)), (200, 635))
                    elif m_pause == False:
                        screen.blit(self.mute_button_image, [mb_top_left_x, mb_top_left_y ])
                        screen.blit(pygame.font.SysFont("'freesansbold.ttf'", 40, True).render("MUSIC OFF", 1, (91, 109, 131)), (200, 635))
                elif about:
                    screen.blit(self.back_button_image, [bb_top_left_x,sb_top_left_y+200 ]);
                pygame.display.flip()
            

##        clock.tick(FPS)
    
