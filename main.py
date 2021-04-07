import sys

import pygame as pg

from options import Options
from ball import Ball
from plate import Plate
from watcher import Watcher
           
def main():
    pg.init()
    options = Options()
    sc = pg.display.set_mode((options.width, options.height))
    pg.display.set_caption('Plate and ball')

    plate = Plate(options, sc)
    plate.draw()
    ball = Ball(options, sc)
    ball.draw()
    watcher = Watcher(ball, plate, options)

    pg.display.update()
   
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                return
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    plate.move_plate_left = True
                elif e.key == pg.K_RIGHT:
                    plate.move_plate_right = True
            elif e.type == pg.KEYUP:
                if e.key == pg.K_LEFT:
                    plate.move_plate_left = False
                elif e.key == pg.K_RIGHT:
                    plate.move_plate_right = False
 
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
