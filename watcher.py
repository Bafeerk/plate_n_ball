class Watcher():
    def __init__(self, ball, plate, brick, options):
        self.ball = ball
        self.plate = plate
        self.brick = brick
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

    def check_brick_collision(self):
         if (self.ball.y + self.ball.radius >= self.brick.y)\
            and (self.ball.y - self.ball.radius <= self.brick.y + self.brick.height)\
            and (self.ball.x + self.ball.radius >= self.brick.x)\
            and (self.ball.x - self.ball.radius <= self.brick.x + self.brick.width):
             self.ball.speedy = self.ball.speedy * (-2)

    def check_lose(self):
        if self.ball.y + self.ball.radius > self.options.height:
            print('YOU LOSE')
            ## Уничтожить шар
