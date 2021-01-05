from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto_start()

    def move(self):
        self.forward(10)
    
    def goto_start(self):
        self.goto(0,-280)

    def is_at_finish(self):
        if self.ycor() > 290:
            return True
        else:
            return False