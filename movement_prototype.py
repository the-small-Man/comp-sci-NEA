import pygame as pg
from star_prototype import star as st


class mainGame:
    def __init__(self):
        pg.init()

        self.clock = pg.time.Clock()

        self.screen=pg.display.set_mode((0,0), pg.RESIZABLE)
        pg.display.set_caption("Shadows Chasing Stars")
        self.width=0
        self.height=0
        self.img = pg.image.load("bg1.png")
        self.chartemp = pg.image.load("longword.png")
        self.charpos = [100,100]
        self.gravspd = 1
        self.gravconst = 0.1
        self.velo = [0,0]
        self.collision_floor = pg.Rect(0, 500, 500, 500)

    def run(self):
        while True:
            #self.screen.blit(self.img, (0,0))
            self.screen.fill((0,0,0))
            self.screen.blit(self.chartemp, self.charpos)
            self.charpos[0] += self.velo[0]
            self.charpos[0] -= self.velo[1]
            self.charpos[1] += self.gravspd
#            while self.gravspd < 10:
#               self.gravspd += self.gravconst
            for ev in pg.event.get():
                if ev.type == pg.VIDEORESIZE:
                    self.width = ev.w
                    self.height = ev.h
                if ev.type == pg.QUIT:
                    pg.quit()
                # batch commands for when a key is DOWN
                if ev.type == pg.KEYDOWN:
                    if ev.key == pg.K_ESCAPE:
                        pg.quit()
                    if ev.key == pg.K_d:
                        self.velo[0] += 1
                    elif ev.key == pg.K_a:
                        self.velo[1] += 1
                    else:
                        self.velo[0] *= 0.9
                        self.velo[1] *= 0.9

            pg.display.update()
            self.clock.tick(60)

mainGame().run()
