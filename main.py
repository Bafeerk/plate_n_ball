import pygame as pg

from options import Options
from ball import Ball
from plate import Plate
from watcher import Watcher
from controller import Controller
         
def main():
    pg.init()
    options = Options()
    sc = pg.display.set_mode((options.width, options.height))
    pg.display.set_caption('Plate and ball')
    plate = Plate(options, sc)
    plate.draw()
    ball = Ball(options, sc)
    ball.draw()
    controller = Controller(plate)
    watcher = Watcher(ball, plate, options)

    pg.display.update()
   
    while True:
        controller.play()

        plate.move()
        watcher.check_screen_collision()
        watcher.check_plate_collision()
        watcher.check_lose()

        ball.y += ball.speedy
        ball.x += ball.speedx
        
        sc.fill((0, 0, 0))
        plate.draw()
        ball.draw()
        pg.display.update()

        pg.time.delay(20)

if __name__ == '__main__':
    main()
