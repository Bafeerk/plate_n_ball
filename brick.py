import pygame as pg


class Brick():
    def __init__(self, screen, options):
        self.options = options
        self.screen = screen
        self.x = options.width // 2
        self.y = options.height // 2
        self.width = 50
        self.height = 10

    def draw(self):
        pg.draw.rect(self.screen, (0, 255, 0),
                     (self.x, self.y, self.width, self.height))
