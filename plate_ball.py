import sys

import pygame as pg

class Options():
        def __init__(self):
            self.width = 600
            self.height = 400

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
        
class Watcher():
    def __init__(self, ball, plate, options):
        self.ball = ball
        self.plate = plate
        self.options = options
        self.score = 0

    def check_plate_collision(self):
        if (self.ball.y + self.ball.radius > self.plate.y)\
           and(self.ball.x + self.ball.radius > self.plate.x\
               and self.ball.x - self.ball.radius < self.plate.x + self.plate.width)\
           and self.ball.speedy > 0:
            self.ball.speedy = -3
            self.score += 1
            print(self.score)    

    def check_screen_collision(self):
        if self.ball.x + self.ball.radius > self.options.width:
            self.ball.speedx = -3
        elif self.ball.x - self.ball.radius < 0:
            self.ball.speedx = +3
        elif self.ball.y - self.ball.radius < 0 and self.ball.speedy < 0:
            self.ball.speedy = 3

    def check_lose(self):
        if self.ball.y + self.ball.radius > self.options.height:
            print('YOU LOSE')
            ## Уничтожить шар
           
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
