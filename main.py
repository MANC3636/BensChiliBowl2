import pygame as pg
import sys
from os import path
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


    def new(self): #helps initialize game
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.floors=pg.sprite.Group()
        self.tables=pg.sprite.Group()

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
            #     self.screen.blit(table_tile.image, table_tile.rect)

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
    g.show_go_screen()