import pygame as pg

class star(pg.sprite.Sprite):

    def __init__(self,velocity,width, height ):
        self.image = pg.Surface([width, height])
        spriteexample = pg.image.load("")
        pg.Surface.blit(spriteexample, self.image)