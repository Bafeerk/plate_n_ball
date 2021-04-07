import pygame as pg

class Ball():
    def __init__(self, options, screen):
        self.options = options
        self.screen = screen
        self.radius = 5
        self.color = (255, 255, 255)
        self.x = options.width // 2
        self.y = 40
        self.speedy = 5
        self.speedx = 5
        self.move_down = True
        self.move_up = True

    def draw(self):
        pg.draw.circle(self.screen, self.color,
                       (self.x, self.y), self.radius)
