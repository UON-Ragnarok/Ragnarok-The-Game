import pygame

class Intro():
    pygame.init()
    

    def __init__(self, screen, menu_background,screen_width,screen_height, title, start_button_image, about_button_image, back_button_image, setting_button_image, volume_button_image, mute_button_image):
        self.screen = screen
        self.menu_background = menu_background
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title = title
        self.start_button_image = start_button_image
        self.about_button_image = about_button_image
        self.back_button_image = back_button_image
        self.setting_button_image = setting_button_image
        self.mute_button_image = pygame.transform.scale(mute_button_image,(100,100))
        self.volume_button_image = pygame.transform.scale(volume_button_image,(100,100)) 
        
    def show_intro(self,screen):

        main = True
        about = False
        setting = False
        menu_background_x = 0
        sb_top_left_x = self.screen_width / 2 - self.start_button_image.get_rect().width / 2
        stb_top_left_x = self.screen_width / 2 - self.setting_button_image.get_rect().width / 2
        sb_top_left_y = self.screen_height / 2
        mb_top_left_y = 100
        bb_top_left_x = self.screen_width / 2 - self.back_button_image.get_rect().width / 2
        mb_top_left_x = 100 - self.mute_button_image.get_rect().width /2
        vb_top_left_x = 100 - self.volume_button_image.get_rect().width /2         
        sb_height = self.start_button_image.get_rect().height
        sb_width = self.start_button_image.get_rect().width
        stb_height = self.setting_button_image.get_rect().height
        stb_width = self.setting_button_image.get_rect().width
        ab_height = self.about_button_image.get_rect().height
        ab_width = self.about_button_image.get_rect().width
        bb_height = self.back_button_image.get_rect().height
        bb_width = self.back_button_image.get_rect().width 
        mb_height = self.mute_button_image.get_rect().height
        mb_width = self.mute_button_image.get_rect().width
        vb_height = self.volume_button_image.get_rect().height
        vb_width = self.volume_button_image.get_rect().width       

        
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

            #mute
           # if pressedkeys[pygame.K_m]:
             #   pygame.mixer.pause()
                #pygame.mixer.unpause()

                
            # start button
            if main and sb_top_left_x < mouse[0] < sb_top_left_x+sb_width and sb_top_left_y < mouse[1] < sb_top_left_y + sb_height:
                self.big_start_button_image = pygame.transform.rotozoom(self.start_button_image,0,1.2)
                screen.blit(self.big_start_button_image, [sb_top_left_x, sb_top_left_y])
                screen.blit(self.about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
                screen.blit(self.setting_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height + 20 + stb_height])
                pygame.display.flip()
                if click[0] == 1:
                    main = False
                    break
                
            # about button
            elif main and sb_top_left_x < mouse[0] < sb_top_left_x+ab_width and sb_top_left_y + 20 + ab_height < mouse[1] < sb_top_left_y + 20 + sb_height+ab_height:
                self.big_about_button_image = pygame.transform.rotozoom(self.about_button_image,0,1.2)
                screen.blit(self.start_button_image, [sb_top_left_x, sb_top_left_y])
                screen.blit(self.big_about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
                screen.blit(self.setting_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height + 20 + stb_height])
                pygame.display.flip()
                if click[0]==1:
                    pygame.time.wait(100)
                    main = False
                    about = True
                    setting = False

            # setting button
            elif main and stb_top_left_x < mouse[0] < stb_top_left_x+ab_width and sb_top_left_y + 20 + ab_height + 20 + stb_height < mouse[1] < sb_top_left_y + 20 + sb_height + ab_height + 20 + stb_height:
                self.big_setting_button_image = pygame.transform.rotozoom(self.setting_button_image,0,1.2)
                screen.blit(self.start_button_image, [sb_top_left_x, sb_top_left_y])
                screen.blit(self.about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
                screen.blit(self.big_setting_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height + 20 + stb_height])                
                pygame.display.flip()
                if click[0]==1:
                    pygame.time.wait(100)
                    main = False
                    about = False
                    setting = True
            
            #back button for about                   
            elif about and bb_top_left_x < mouse[0] < bb_top_left_x+bb_width and sb_top_left_y+200 < mouse[1] < sb_top_left_y+200 + bb_height:
                self.big_back_button_image = pygame.transform.rotozoom(self.back_button_image,0,1.2)
                screen.blit(self.big_back_button_image, [bb_top_left_x, sb_top_left_y + 200])
                pygame.display.flip()
                if click[0] == 1:
                    main = True
                    about = False
                    setting = False
                    
            #back button for settings
            elif setting and bb_top_left_x < mouse[0] < bb_top_left_x+bb_width and sb_top_left_y+200 < mouse[1] < sb_top_left_y+200 + bb_height:
                self.big_back_button_image = pygame.transform.rotozoom(self.back_button_image,0,1.2)
                screen.blit(self.big_back_button_image, [bb_top_left_x, sb_top_left_y + 200])
                screen.blit(self.mute_button_image, [mb_top_left_x, mb_top_left_y])
                screen.blit(self.volume_button_image, [mb_top_left_x, mb_top_left_y + 20 + mb_height])
                pygame.display.flip()
                if click[0] == 1:
                    pygame.time.wait(100)
                    main = True
                    about = False
                    setting = False
                    
            # mute button for setting
            elif setting and mb_top_left_x < mouse[0] < mb_top_left_x + mb_width and mb_top_left_y < mouse[1] < mb_top_left_y + mb_height:
                self.big_mute_button_image = pygame.transform.rotozoom(self.mute_button_image,0,1.2)
                screen.blit(self.big_mute_button_image, [mb_top_left_x, mb_top_left_y])
                screen.blit(self.volume_button_image, [mb_top_left_x, mb_top_left_y + 20 + mb_height])
                screen.blit(self.back_button_image, [bb_top_left_x,sb_top_left_y+200 ]);
                pygame.display.flip()
                if click[0] == 1:
                    pygame.time.wait(100)
                    pygame.mixer.unpause()
                    
            # volume button for setting
            elif setting and mb_top_left_x < mouse[0] < mb_top_left_x + vb_width and mb_top_left_y + 20 + vb_height < mouse[1] < mb_top_left_y + 20 + mb_height + vb_height:
                self.big_volume_button_image = pygame.transform.rotozoom(self.volume_button_image,0,1.2)
                screen.blit(self.mute_button_image, [mb_top_left_x, mb_top_left_y])
                screen.blit(self.big_volume_button_image, [mb_top_left_x, mb_top_left_y + 20 + mb_height])
                screen.blit(self.back_button_image, [bb_top_left_x,sb_top_left_y+200 ]);
                pygame.display.flip()
                if click[0]==1:
                    pygame.time.wait(100)
                    pygame.mixer.pause()

            else:
                if main:
                    screen.blit(self.start_button_image, [sb_top_left_x, sb_top_left_y])
                    screen.blit(self.about_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height])
                    screen.blit(self.setting_button_image, [sb_top_left_x, sb_top_left_y + 20 + sb_height + 20 + stb_height])
                elif about:
                    screen.blit(self.back_button_image, [bb_top_left_x,sb_top_left_y+200 ]);
                elif setting:
                    screen.blit(self.mute_button_image, [mb_top_left_x, mb_top_left_y])
                    screen.blit(self.volume_button_image, [mb_top_left_x, mb_top_left_y + 20 + mb_height])
                    screen.blit(self.back_button_image, [bb_top_left_x,sb_top_left_y+200 ]);
                pygame.display.flip()
            

##        clock.tick(FPS)
    
