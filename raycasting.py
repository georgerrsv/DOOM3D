import pygame as pg
import math
from settings import *

class Raycasting:
    def __init__(self, game):
        self.game = game
        self.rayCastResult = []
        self.objectsToRender = []
        self.textures = self.game.objRender.wallTextures

    def getObjectsToRender(self):
        self.objectsToRender = []
        for ray, values in enumerate(self.rayCastResult):
            depth, projHeight, texture, offset = values

            wallColumn = self.textures[texture].subsurface(offset * (textureSize - scale), 0, scale, textureSize)
            wallColumn = pg.transform.scale(wallColumn, (scale, projHeight))
            wallPos = (ray * scale, HALF_HEIGHT - projHeight // 2)

            self.objectsToRender.append((depth, wallColumn, wallPos))

    def rayCast(self):
        self.rayCastResult = []
        ox, oy = self.game.player.position
        xMap, yMap = self.game.player.mapPosition

        rayAngle = self.game.player.angle - halfFieldOfView + 0.0001
        for ray in range(numRays):
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
                if tileHorizontal in self.game.map.worldMap:
                    textureHorizontal = self.game.map.worldMap[tileHorizontal]
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
                if tileVert in self.game.map.worldMap:
                    textureVertical = self.game.map.worldMap[tileVert]
                    break
                xVertical += dx
                yVertical += dy
                depthVertical += deltaDepth

            # depth, textures offset
            if depthVertical < depthHorizontal:
                depth, texture = depthVertical, textureVertical
                yVertical %= 1
                offset = yVertical if cosA > 0 else (1 - yVertical)
            else:
                depth, texture = depthHorizontal, textureHorizontal
                xHorizontal %= 1
                offset = (1 - xHorizontal) if sinA < 0 else xHorizontal

            # remove fish eye effect
            depth *= math.cos(self.game.player.angle - rayAngle)

            # projection
            projHeight = screenDistance / (depth + 0.0001)

            # ray casting result
            self.rayCastResult.append((depth, projHeight, texture, offset))

            rayAngle += deltaAngle

    def update(self):
        self.rayCast()
        self.getObjectsToRender()