import pygame as pg
from settings import *

class spriteObject:
    def __init__(self, game, path='resources/sprite/staticSprites/candlebra.png', pos=(10.5, 3.5)):
        self.game game
        self.player. game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.imageWidth = self.image.get_width()
        self.imageHalfWidth = self.image.get_width() // 2

    def getSprite(self):
        pass

    def update(self):
        self.getSprite()