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
