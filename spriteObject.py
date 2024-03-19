import pygame as pg
from settings import *

class spriteObject:
    def __init__(self, game, path='resources/sprites/staticSprites/candlebra.png', pos=(10.5, 3.5)):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.imageWidth = self.image.get_width()
        self.imageHalfWidth = self.image.get_width() // 2
        self.imageRatio = self.imageWidth / self.image.get_height()
        self.dx, self.dy, self.theta, self.screenX, self.distance, self.normalDistance = 0, 0, 0, 0, 1, 1
        self.spriteHalfWidth = 0

    def getSpriteProjection(self):
        proj = screenDistance / self.normalDistance
        projWidth, projHeight = proj * self.imageRatio, proj

        image = pg.transform.scale(self.image, (projWidth, projHeight))

        self.spriteHalfWidth = projWidth // 2
        pos = self.screenX - self.spriteHalfWidth, HALF_HEIGHT - projHeight // 2

        self.game.raycasting.objectsToRender.append((self.normalDistance, image, pos))

    def getSprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        deltaRays = delta / deltaAngle
        self.screenX = (halfNumRays + deltaRays) * scale

        self.distance = math.hypot(dx, dy)
        self.normalDistance = self.distance * math.cos(delta)
        if -self.imageHalfWidth < self.screenX < (WIDTH + self.imageHalfWidth) and self.normalDistance > 0.5:
            self.getSpriteProjection()

    def update(self):
        self.getSprite()