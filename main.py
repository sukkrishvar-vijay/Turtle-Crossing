import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#print('Hello')
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
turtle=Player()
car=CarManager()

screen.listen()
screen.onkey(turtle.move, "Up")
screen.onkey(turtle.back, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()
    car.create_car()
    car.move_car()
    
    for cars in car.all_cars:
        if cars.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on=False
    
    if turtle.at_finish():
        turtle.start()
        car.level_up()
        print(car.car_speed)
        scoreboard.level_score += 1


screen.exitonclick()
