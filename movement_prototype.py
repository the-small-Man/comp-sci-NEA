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
        self.movement = [False, False]
        self.charpos = [100,100]
        self.gravspd = [False, True]
        self.gravconst = 0.5

    def run(self):
        while True:
            self.screen.blit(self.img, (0,0))
            self.screen.blit(self.chartemp, self.charpos)
            self.charpos[0] += self.movement[0]
            self.charpos[0] -= self.movement[1]
            self.charpos[1] += self.gravspd[1]
#            while self.gravspd < 10:
#                self.gravspd[1] += self.gravconst
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
                        self.movement[0] = True
                    if ev.key == pg.K_a:
                        self.movement[1] = True
                #batch commands for when a key is UP
                if ev.type == pg.KEYUP:
                    if ev.key == pg.K_d:
                        self.movement[0] = False
                    if ev.key == pg.K_a:
                        self.movement[1] = False
            pg.display.update()
            self.clock.tick(60)

mainGame().run()
