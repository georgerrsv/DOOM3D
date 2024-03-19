from spriteObject import *

class objectHandler:
    def __init__(self, game):
        self.game = game
        self.spriteList = []
        self.staticSpritePath = 'resources/sprites/staticSprites/'
        self.animatedSpritePath = 'resources/sprites/animatedSprites/'
        addSprite = self.addSprite

        addSprite(spriteObject(game))
        addSprite(animatedSprites(game))

    def update(self):
        [sprite.update() for sprite in self.spriteList]

    def addSprite(self, sprite):
        self.spriteList.append(sprite)