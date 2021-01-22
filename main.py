
import pygame as pg
import sys

from settings import *
from sprites import *


class Game:
    def __init__(self): #helps initialize game
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        #pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self): #helps initialize game
        #game_folder = path.dirname(__file__)
        self.map_data = []
        print(pg.font.get_fonts())

        with open('revised_map.txt', 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def text_box(self, text, x, y):#--------------------------->this func is new
        self.font=pg.font.SysFont("arial",20)
        self.text_surface=self.font.render(text, True, (20,100,100))
        self.text_rect=self.text_surface.get_rect(center=(x,y))
        self.screen.blit(self.text_surface, self.text_rect)

    def new(self): #helps initialize game
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.floors=pg.sprite.Group()
        self.tables=pg.sprite.Group()
        self.menu=Menu(self, WIDTH-96,96)#-------------------------->this call is new 


        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == "2":
                    Table(self, col, row)

                if tile == 'P':
                    self.player= Player(self, col, row)


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events() #collects user input
            self.update() #2 processes that input
            self.draw() #3blits the results of the input to the screen
            # for table_tile in self.tables:



    def quit(self):
        pg.quit()
        sys.exit()

    def update(self): #1 process user input
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):#part of the blit results
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
        self.text_box("Need's fixing", 78, 160)#------------------->also new

    def draw(self):#part of blit results
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # collect user inputs here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
