from spriteObject import *
from npc import *

class objectHandler:
    def __init__(self, game):
        self.game = game
        self.spriteList = []
        self.npcList = []
        self.npcSpritePath = 'resources/sprites/npc/'
        self.staticSpritePath = 'resources/sprites/staticSprites/'
        self.animatedSpritePath = 'resources/sprites/animatedSprites/'
        addSprite = self.addSprite
        addNpc = self.addNpc

        addSprite(spriteObject(game))
        addSprite(animatedSprites(game))
        addSprite(animatedSprites(game, path=self.animatedSpritePath + 'redLight/0.png', pos=(14.5, 7.5)))
        addSprite(animatedSprites(game, path=self.animatedSpritePath + 'redLight/0.png', pos=(4.5, 7.5)))
        addSprite(animatedSprites(game, path=self.animatedSpritePath + 'greenLight/0.png', pos=(11.5, 7.5)))
        addSprite(animatedSprites(game, path=self.animatedSpritePath + 'redLight/0.png', pos=(3.5, 7.5)))
        addSprite(animatedSprites(game, path=self.animatedSpritePath + 'redLight/0.png', pos=(2.5, 7.5)))
        addSprite(animatedSprites(game, path=self.animatedSpritePath + 'redLight/0.png', pos=(1.5, 7.5)))
        addSprite(animatedSprites(game, path=self.animatedSpritePath + 'redLight/0.png', pos=(8.5, 7.5)))
        addSprite(animatedSprites(game, path=self.animatedSpritePath + 'greenLight/0.png', pos=(6.5, 7.5)))
        addSprite(animatedSprites(game, path=self.animatedSpritePath + 'greenLight/0.png', pos=(1.5, 1.5)))

        addNpc(NPC(game))


    def update(self):
        [sprite.update() for sprite in self.spriteList]
        [npc.update() for npc in self.npcList]

    def addNpc(self, npc):
        self.npcList.append(npc)

    def addSprite(self, sprite):
        self.spriteList.append(sprite)