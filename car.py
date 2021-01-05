from turtle import Turtle
import random
COLOR =["red","orange","yellow","blue","purple"]

class Car:
    def __init__(self):
        self.all_cars =[]
        self.car_speed  = 5
    
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLOR))
            new_car.setheading(180)
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += 10
