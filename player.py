from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = playerPosition
        self.angle = playerAngle

    def movement(self):
        pass

    def update(self):
        self.movement()

    @property
    def position(self):
        return self.x, self.y

    @property
    def mapPosition(self):
        return int(self.x), int(self.y)