import pygame as pg
from settings import *
import os
from collections import deque

class spriteObject:
    def __init__(self, game, path='resources/sprites/staticSprites/candlebra.png', pos=(10.5, 3.5), scale=0.7, shift=0.27):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.imageWidth = self.image.get_width()
        self.imageHalfWidth = self.image.get_width() // 2
        self.imageRatio = self.imageWidth / self.image.get_height()
        self.dx, self.dy, self.theta, self.screenX, self.distance, self.normalDistance = 0, 0, 0, 0, 1, 1
        self.spriteHalfWidth = 0
        self.spriteScale = scale
        self.spriteShift = shift

    def getSpriteProjection(self):
        proj = screenDistance / self.normalDistance * self.spriteScale
        projWidth, projHeight = proj * self.imageRatio, proj

        image = pg.transform.scale(self.image, (projWidth, projHeight))

        self.spriteHalfWidth = projWidth // 2
        heightShift = projHeight * self.spriteShift
        pos = self.screenX - self.spriteHalfWidth, HALF_HEIGHT - projHeight // 2 + heightShift

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

class animatedSprites(spriteObject):
    def __init__(self, game, path='resources/sprites/animatedSprites/greenLight/0.png', pos=(11.5, 3.5), scale=0.8, shift=0.15, animationTime=120):
        super().__init__(game, path, pos, scale, shift)
        self.animationTime = animationTime
        self.path = path.rsplit('/', 1)[0]
        self.images = self.getImages(self.path)
        self.animationTimePrev = pg.time.get_ticks()
        self.animationTrigger = False

    def update(self):
        super().update()
        self.checkAnimationTime()
        self.animate(self.images)

    def animate(self, images):
        if self.animationTrigger:
            images.rotate(-1)
            self.image = images[0]

    def checkAnimationTime(self):
        self.animationTrigger = False
        timeNow = pg.time.get_ticks()
        if timeNow - self.animationTimePrev > self.animationTime:
            self.animationTimePrev = timeNow
            self.animationTrigger = True

    def getImages(self, path):
        images = deque()
        for fileName in os.listdir(path):
            if os.path.isfile(os.path.join(path, fileName)):
                img = pg.image.load(path + '/' + fileName).convert_alpha()
                images.append(img)
        return images