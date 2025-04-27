import pygame as pg
from star_prototype import star as st



pg.init()

clock = pg.time.Clock()

screen=pg.display.set_mode((0,0), pg.RESIZABLE)
pg.display.set_caption("Shadows Chasing Stars")
width=0
height=0


while True:
    for ev in pg.event.get():
        if ev.type == pg.VIDEORESIZE:
            width = ev.w
            height = ev.h
        if ev.type == pg.QUIT:
            pg.quit()
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                pg.quit()
                
    pg.display.update()
    clock.tick(60)