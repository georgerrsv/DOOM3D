import pygame as pg


class Car(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("car.png")
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += 1
        if self.rect.left > 800:
            self.rect.right = 0


pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
all_sprites = pg.sprite.Group()
car = Car(400, 300)
all_sprites.add(car)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    all_sprites.update()
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(60)
pg.quit()
