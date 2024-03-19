import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from objRender import *
from spriteObject import *
from objectHandler import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RESOLUTION)
        self.clock = pg.time.Clock()
        self.deltaTime = 1
        self.newGame()

    def newGame(self):
        self.map = Map(self)
        self.player = Player(self)
        self.objRender = objectRender(self)
        self.raycasting = Raycasting(self)
        self.objectHandler = objectHandler(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.objectHandler.update()
        pg.display.flip()
        self.deltaTime = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self):
        #self.screen.fill('black')
        self.objRender.draw()
        #self.map.draw()
        #self.player.draw()

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    def run(self):
        while True:
            self.checkEvents()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()