import pygame as pg
import math
from settings import *

class Raycasting:
    def __init__(self, game):
        self.game = game

    def rayCast(self):
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
                    break
                xVertical += dx
                yVertical += dy
                depthVertical += deltaDepth

            # depth
            if depthVertical < depthHorizontal:
                depth = depthVertical
            else:
                depth = depthHorizontal

            # draw
            #pg.draw.line(self.game.screen, 'yellow', (100 * ox, 100 * oy),
            #             (100 * ox + 100 * depth * cosA, 100 * oy + 100 * depth * sinA), 2)

            # projection
            projHeight = screenDistance / (depth + 0.0001)

            # draw walls
            pg.draw.rect(self.game.screen, 'white',
                         (ray * scale, HALF_HEIGHT - projHeight // 2, scale, projHeight))

            rayAngle += deltaAngle

    def update(self):
        self.rayCast()