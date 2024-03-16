from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = playerPosition
        self.angle = playerAngle

    def movement(self):
        sinA = math.sin(self.angle)
        cosA = math.cos(self.angle)
        dx, dy = 0, 0
        speed = playerSpeed * self.game.deltaTime
        speedSin = speed * sinA
        speedCos = speed * cosA

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speedCos
            dy += speedSin
        if keys[pg.K_s]:
            dx -= speedCos
            dy -= speedSin
        if keys[pg.K_a]:
            dx += speedSin
            dy -= speedCos
        if keys[pg.K_d]:
            dx -= speedSin
            dy += speedCos

        self.checkWallCollision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= playerRotationSpeed * self.game.deltaTime
        if keys[pg.K_RIGHT]:
            self.angle += playerRotationSpeed * self.game.deltaTime
        self.angle %= math.tau

    def checkWall(self, x, y):
        return (x, y) not in self.game.map.worldMap

    def checkWallCollision(self, dx, dy):
        if self.checkWall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.checkWall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        #pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
        #             (self.x * 100 + WIDTH * math.cos(self.angle), self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()

    @property
    def position(self):
        return self.x, self.y

    @property
    def mapPosition(self):
        return int(self.x), int(self.y)