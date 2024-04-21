from spriteObject import *
from random import randint, random, choice

class NPC(animatedSprites):
    def __init__(self, game, path='resources/sprites/npc/soldier/0.png', pos=(10.5, 5.5),
                 scale=0.6, shift=0.38, animationTime=180):
        super().__init__(game, path, pos, scale, shift, animationTime)
        self.attackImages = self.getImages(self.path + '/attack')
        self.deathImages = self.getImages(self.path + '/death')
        self.idleImages = self.getImages(self.path + '/idle')
        self.painImages = self.getImages(self.path + '/pain')
        self.walkImages = self.getImages(self.path + '/walk')

        self.attackDistance = randint(3, 6)
        self.speed = 0.03
        self.size = 10
        self.health = 100
        self.attackDamage = 10
        self.accuracy = 0.15
        self.alive = True
        self.pain = False
        self.rayCastValue = False

    def update(self):
        self.checkAnimationTime()
        self.getSprite()
        self.runLogic()
        #self.drawRayCast()

    def animatePain(self):
        self.animate(self.painImages)
        if self.animationTrigger:
            self.pain = False

    def checkHit(self):
        if self.rayCastValue and self.game.player.shot:
            if HALF_WIDTH - self.spriteHalfWidth < self.screenX < HALF_WIDTH + self.spriteHalfWidth:
                self.game.sound.npcPain.play()
                self.game.player.shot = False
                self.pain = True

    def runLogic(self):
        if self.alive:
            self.rayCastValue = self.rayCastPlayerNpc()
            self.checkHit()
            if self.pain:
                self.animatePain()
            else:
                self.animate(self.idleImages)

    @property
    def mapPosition(self):
        return int(self.x), int(self.y)

    def rayCastPlayerNpc(self):
        if self.game.player.mapPosition == self.mapPosition:
            return True

        wallDistanceVertical, wallDistanceHorizontal = 0, 0
        playerDistanceVertical, playerDistanceHorizontal = 0, 0

        ox, oy = self.game.player.position
        xMap, yMap = self.game.player.mapPosition

        rayAngle = self.theta
        sinA = math.sin(rayAngle)
        cosA = math.cos(rayAngle)

        # Horizontals
        yHorizontal, dy = (yMap + 1, 1) if sinA > 0 else (yMap - 1e-6, -1)

        depthHorizontal = (yHorizontal - oy) / sinA
        xHorizontal = ox + depthHorizontal * cosA

        deltaDepth = dy / sinA
        dx = deltaDepth * cosA

        for i in range(maxDepth):
            tileHorizontal = int(xHorizontal), int(yHorizontal)
            if tileHorizontal == self.mapPosition:
                playerDistanceHorizontal = depthHorizontal
                break
            if tileHorizontal in self.game.map.worldMap:
                wallDistanceHorizontal = depthHorizontal
                break
            xHorizontal += dx
            yHorizontal += dy
            depthHorizontal += deltaDepth

        # Verticals
        xVertical, dx = (xMap + 1, 1) if cosA > 0 else (xMap - 1e-6, -1)

        depthVertical = (xVertical - ox) / cosA
        yVertical = oy + depthVertical * sinA

        deltaDepth = dx / cosA
        dy = deltaDepth * sinA

        for i in range(maxDepth):
            tileVert = int(xVertical), int(yVertical)
            if tileVert == self.mapPosition:
                playerDistanceVertical = depthVertical
                break
            if tileVert in self.game.map.worldMap:
                wallDistanceVertical = depthVertical
                break
            xVertical += dx
            yVertical += dy
            depthVertical += deltaDepth

        playerDistance = max(playerDistanceVertical, playerDistanceHorizontal)
        wallDistance = max(wallDistanceVertical, wallDistanceHorizontal)

        if 0 < playerDistance < wallDistance or not wallDistance:
            return True
        return False

    def drawRayCast(self):
        pg.draw.circle(self.game.screen, 'red', (100 * self.x, 100 * self.y), 15)
        if self.rayCastPlayerNpc():
            pg.draw.line(self.game.screen, 'orange', (100 * self.game.player.x, 100 * self.game.player.y),
                         (100 * self.x, 100 * self.y), 2)
