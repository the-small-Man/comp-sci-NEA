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

    def update(self):

        for ev in pg.event.get():
            match ev.type:
                case pg.QUIT:
                    return False
                case pg.VIDEORESIZE:
                    self.width = ev.w
                    self.height = ev.h
                case pg.KEYDOWN:
                    match ev.key:
                        case pg.K_ESCAPE:
                           pg.quit()

    def run(self):
        while True:
            
            self.update()

            pg.display.update()
            self.clock.tick(60)

MainGame().run()