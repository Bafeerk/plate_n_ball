import pygame as pg

class Plate():
    def __init__(self, options, screen):
        self.width = 60
        self.height = 10
        self.screen = screen
        self.options = options
        self.x = self.options.width //2 - self.width // 2
        self.y = self.options.height - 20
        self.move_plate_left = False
        self.move_plate_right = False

    def move(self):
        if self.move_plate_left:
            self.x -= 5
        elif self.move_plate_right:
            self.x += 5

    def draw(self):
        pg.draw.rect(self.screen, (255, 255, 255),
                     (self.x, self.y, self.width, self.height))
