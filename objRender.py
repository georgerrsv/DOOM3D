import pygame as pg
from settings import *


class objectRender:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wallTextures = self.loadWallTextures()
        self.skyImage = self.getTexture('resources/textures/sky.png', (WIDTH, HALF_HEIGHT))
        self.skyOffset = 0

    def draw(self):
        self.drawBackground()
        self.renderGameObjects()

    def drawBackground(self):
        self.skyOffset = (self.skyOffset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.skyImage, (-self.skyOffset, 0))
        self.screen.blit(self.skyImage, (-self.skyOffset + WIDTH, 0))
        pg.draw.rect(self.screen, floorColor, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

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