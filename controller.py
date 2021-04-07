import sys

import pygame as pg

class Controller():
    def __init__(self, plate):
        self.plate = plate

    def play(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    self.plate.move_plate_left = True
                elif e.key == pg.K_RIGHT:
                    self.plate.move_plate_right = True
            elif e.type == pg.KEYUP:
                if e.key == pg.K_LEFT:
                    self.plate.move_plate_left = False
                elif e.key == pg.K_RIGHT:
                    self.plate.move_plate_right = False
