import pygame as pg
from star_prototype import star as st


class mainGame:
    def __init__(self):
        pg.init()

        self.clock = pg.time.Clock()

        screen=pg.display.set_mode((0,0), pg.RESIZABLE)
        pg.display.set_caption("Shadows Chasing Stars")
        width=0
        height=0

    def run(self):
        while True:
            for ev in pg.event.get():
                if ev.type == pg.VIDEORESIZE:
                    self.width = ev.w
                    self.height = ev.h
                if ev.type == pg.QUIT:
                    pg.quit()
                if ev.type == pg.KEYDOWN:
                    if ev.key == pg.K_ESCAPE:
                        pg.quit()
                        
            pg.display.update()
            self.clock.tick(60)

mainGame().run()