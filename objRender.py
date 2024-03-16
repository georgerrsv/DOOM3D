import pygame as pg
from settings import *


class objectRender:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wallTextures = self.loadWallTextures()

    def draw(self):
        self.renderGameObjects()

    def renderGameObjects(self):
        listObjects = self.game.raycasting.objectsToRender
        for depth, image, pos in listObjects:
            self.screen.blit(image, pos)

    @staticmethod
    def getTexture(path, resolution=(textureSize, textureSize)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, resolution)

    def loadWallTextures(self):
        return {
            1: self.getTexture('resources/textures/1.png'),
            2: self.getTexture('resources/textures/2.png'),
            3: self.getTexture('resources/textures/3.png'),
            4: self.getTexture('resources/textures/4.png'),
            5: self.getTexture('resources/textures/5.png'),
        }