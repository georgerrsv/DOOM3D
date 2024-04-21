import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgunSound = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.npcPain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npcDeath = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npcAttack = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.playerPain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.theme = pg.mixer.Sound(self.path + 'theme.mp3')