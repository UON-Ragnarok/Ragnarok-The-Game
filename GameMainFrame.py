import pygame as pg
import random
import time
import math
import sys
from os import path
from settings import *  # * make it doesnt need prepen such as settings.xxx
from sprites import *


class Game:
    def __init__(self):  # for programme to start up, initialize game window, etc
        self.running = True
        pg.init()
        self.screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # pg.key.set_repeat(500, 100)  # set_repeat(delay, interval)
        self.load_data()

    def new(self):
        self.score = 0
        self.sprites_list = pg.sprite.Group()
        self.run()

    def load_data(self):
        # load high score
        self.game_folder = path.dirname(__file__)
        with open(path.join(self.game_folder, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        # load images
        img_folder = path.join(path.dirname(__file__), 'img')
        self.bg = pg.image.load(path.join(img_folder, 'background.jpg')).convert()
        self.ship_img = pg.image.load(path.join(img_folder, "spaceship.png")).convert_alpha()
        # Sound
        self.sound_folder = path.join(self.game_folder, 'Sound')


    def run(self):
        # game loop - set self.playing = False to end the game == go to menu
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.sprites_list.update()

    def draw(self):
        # game loop
        # self.screen.fill(BGCOLOR)  # no longer needed
        self.screen.blit(self.bg, self.bg.get_rect())
        self.sprites_list.draw(self.screen)
        # after drawing everything, flip the display
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                self.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()


    def show_start_screen(self):  # == intro
        pass

    def show_go_screen(self):  # the game over screen == menu
        pass


    def New_high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(path.join(self.game_folder, HS_FILE), 'w') as f:
                f.write(str(self.score))


# create the game object
Ragnarok = Game()
Ragnarok.show_start_screen()
while Ragnarok.running:
    Ragnarok.new()
    Ragnarok.show_go_screen()
