import pygame

#Game Settings
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
FPS = 120
GAME_TITLE = 'Ragnarok The Game'
BACKGROUND_IMG = 'img/background.jpg'
FONT = 'Courier'
HIGHSCORE = 'highscore.txt'

#COLORS
RED = (214, 72, 72)
GREY = (91, 109, 131)
BLACK = (0, 0, 0)
YELLOW = (240, 255, 0)

#Music
pygame.mixer.set_num_channels(15)

ARCADE_FUNK = 'Sound/Arcade Funk.ogg'  # Channel 0
EXPLOSION = pygame.mixer.Sound('Sound/explo.ogg') # Channel 1
COIN = pygame.mixer.Sound('Sound/coin.ogg')  # Channel 2
KILLED = pygame.mixer.Sound('Sound/killed_explo.ogg')  # Channel 3
COMET = pygame.mixer.Sound('Sound/comet.ogg')  # Channel 4
LASER = pygame.mixer.Sound('Sound/laser.ogg')  # Channel 5
BOSS_LASER = pygame.mixer.Sound('Sound/Boss_laser.ogg')  # Channel 6


#Gameplay Properties
DIFFICULTY = 10
METEOR_SPAWN_RATE = 4
POWERUP_PERCENTAGE = 10
POWER_UP_ID_LIST = ['A', 'B', 'C']
#SPEED_POWER_UP_ID = 'A'
#DAMAGE_POWER_UP_ID = 'B'
#DOUBLE_POWER_UP_ID = 'C'
