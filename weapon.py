from spriteObject import *


class Weapon(animatedSprites):
    def __init__(self, game, path='resources/sprites/weapon/shotgun/0.png', scale=0.4, animationTime=90):
        super().__init__(game=game, path=path, scale=scale, animationTime=animationTime)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weaponPosition = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.numImages = len(self.images)
        self.frameCounter = 0
        self.damage = 50

    def animatedShot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animationTrigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frameCounter += 1
                if self.frameCounter == self.numImages:
                    self.reloading = False
                    self.frameCounter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weaponPosition)

    def update(self):
        self.checkAnimationTime()
        self.animatedShot()