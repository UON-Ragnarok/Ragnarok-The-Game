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
ARCADE_FUNK = pygame.mixer.Sound('Sound/Arcade Funk.ogg')
MOB_DYING = pygame.mixer.Sound('Sound/killed_explo.ogg')
EXPLOSION = pygame.mixer.Sound('Sound/explo.ogg')
COIN = pygame.mixer.Sound('Sound/coin.ogg')
KILLED = pygame.mixer.Sound('Sound/killed_explo.ogg')
COMET = pygame.mixer.Sound('Sound/comet.ogg')
LASER = pygame.mixer.Sound('Sound/laser.ogg')
BOSS_LASER = pygame.mixer.Sound('Sound/Boss_laser.ogg')
pygame.mixer.Channel(1).set_volume(0.1)
pygame.mixer.Channel(2).set_volume(0.3)
pygame.mixer.Channel(3).set_volume(0.5)
pygame.mixer.Channel(4).set_volume(0.5)
pygame.mixer.Channel(4).set_volume(1.0)
pygame.mixer.Channel(6).set_volume(0.3)
pygame.mixer.Channel(7).set_volume(0.2)

#Gameplay Properties
DIFFICULTY = 10
METEOR_SPAWN_RATE = 4
POWERUP_PERCENTAGE = 10
POWER_UP_ID_LIST = ['A', 'B', 'C']
#SPEED_POWER_UP_ID = 'A'
#DAMAGE_POWER_UP_ID = 'B'
#DOUBLE_POWER_UP_ID = 'C'
