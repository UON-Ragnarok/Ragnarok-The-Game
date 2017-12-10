import pygame

#Game Settings
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
FPS = 120
GAME_TITLE = 'Ragnarok The Game'
BACKGROUND_IMG = 'img/background.jpg'
FONT = 'Courier'

#COLORS
RED = (214, 72, 72)
GREY = (91, 109, 131)
BLACK = (0, 0, 0)

#Music
pygame.mixer.set_num_channels(15)
ARCADE_FUNK = 'Sound/Arcade Funk.ogg'
MOB_DYING = pygame.mixer.Sound('Sound/killed_explo.ogg')
EXPLOSION = pygame.mixer.Sound('Sound/explo.ogg')

#Gameplay Properties
POWERUP_PERCENTAGE = 30
SPEED_POWER_UP_ID = 'A'
DAMAGE_POWER_UP_ID = 'B'
DOUBLE_POWER_UP_ID = 'C'
