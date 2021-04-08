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
        """
        Меняет координаты объекта, для движения вправо-влево в пределах окна экрана
        """
        if self.move_plate_left and self.x > 0:
            self.x -= 5
        elif self.move_plate_right and self.x + self.width < self.options.width:
            self.x += 5

    def draw(self):
        """
        Отрисовывает объект на рассчитанных координатах
        """
        pg.draw.rect(self.screen, (255, 255, 255),
                     (self.x, self.y, self.width, self.height))
