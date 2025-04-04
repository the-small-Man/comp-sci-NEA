import pygame as pg
from star_prototype import star as st


class mainGame():

    def __init__(self):
        pg.init()

        self.clock = pg.time.Clock()

        self.screen=pg.display.set_mode((0,0), pg.RESIZABLE)
        pg.display.set_caption("Shadows Chasing Stars")
        self.width=0
        self.height=0
        self.isRunning = True



while isRunning:
    for ev in pg.event.get():
        if ev.type == pg.VIDEORESIZE:
            width = ev.w
            height = ev.h
        if ev.type == pg.QUIT:
            isRunning = False
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                isRunning = False
    pg.display.update()
    mainGame.clock.tick(60)