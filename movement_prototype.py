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
        self.SCD = 1

    def run(self):
        while True:
            #self.screen.blit(self.img, (0,0))
            self.screen.fill((0,0,0))
            self.screen.blit(self.chartemp, self.charpos)
            pg.draw.rect(self.screen, (50,50,50), width = 1500, rect = (1500, 20))
            self.charpos[0] += self.velo[0]
            self.charpos[0] -= self.velo[1]
            self.charpos[1] += self.gravspd
            self.floorcollision = False
            pg.key.set_repeat(1)
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
                        self.velo[0] += 0.05
                    elif ev.key == pg.K_a:
                        self.velo[1] += 0.05
            if self.SCD > 0.9:
                self.SCD -= 0.01
            elif ev.type == pg.KEYUP:
                if ev.key == pg.K_d:
                    self.SCD = 1
                if ev.key == pg.K_a:
                    self.SCD = 1
            if self.floorcollision == True:
                self.gravspd = 0
            else:
                self.gravspd = 1
            self.velo[0] *= self.SCD
            self.velo[1] *= self.SCD
            
            pg.display.update()
            self.clock.tick(60)

mainGame().run()
