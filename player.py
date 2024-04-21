from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = playerPosition
        self.angle = playerAngle
        self.shot = False

    def singleFireEvent(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgunSound.play()
                self.shot = True
                self.game.weapon.reloading = True
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

        #if keys[pg.K_LEFT]:
        #    self.angle -= playerRotationSpeed * self.game.deltaTime
        #if keys[pg.K_RIGHT]:
        #    self.angle += playerRotationSpeed * self.game.deltaTime
        self.angle %= math.tau

    def checkWall(self, x, y):
        return (x, y) not in self.game.map.worldMap

    def checkWallCollision(self, dx, dy):
        scale = playerSizeScale / self.game.deltaTime
        if self.checkWall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.checkWall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        #pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
        #             (self.x * 100 + WIDTH * math.cos(self.angle), self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def mouseControl(self):
        mx, my = pg.mouse.get_pos()
        if mx < mouseBorderLeft or mx > mouseBorderRight:
            pg.mouse.set_pos(HALF_WIDTH, HALF_HEIGHT)
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-mouseMaxRel, min(mouseMaxRel, self.rel))
        self.angle += self.rel * mouseSensitivity * self.game.deltaTime

    def update(self):
        self.movement()
        self.mouseControl()

    @property
    def position(self):
        return self.x, self.y

    @property
    def mapPosition(self):
        return int(self.x), int(self.y)