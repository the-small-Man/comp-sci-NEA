import pygame as pg

class MainGame:
    def __init__(self):
        pg.init

        self.clock = pg.time.Clock()

        self.screen=pg.display.set_mode((0,0), pg.RESIZABLE)
        pg.display.set_caption("Shadows Chasing Stars")
        self.width = 0
        self.height = 0
        self.bg = pg.image.load("bg1.png")
