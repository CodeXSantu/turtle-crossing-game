from turtle import Turtle,Screen
from player import Player
from car import Car
from score import Score
import random
import time
screen =Screen()
screen.setup(width=600,height=600)
screen.title("TURTLE CROSSING GAME")
screen.tracer(0)

player = Player()
car = Car()
score = Score()



screen.listen()
screen.onkeypress(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    
    car.create_car()
    car.move()
    
    # !Detect collision with car
    for square in car.all_cars:
        if square.distance(player) < 20:
            game_is_on = False
            score.game_over()
        
    # !Detect the succcessfull crossing
    if player.is_at_finish():
        player.goto_start()
        car.level_up()
        score.increse_level()


screen.exitonclick()