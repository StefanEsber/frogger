import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
car = CarManager()
level = Scoreboard()

screen.listen()
screen.onkeypress(turtle.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for cars in car.all_cars:
        if cars.distance(turtle) < 20:
            game_is_on = False
            screen.clear()
            level.game_over()

    if turtle.is_at_finish():
        turtle.start_position()
        level.increase_level()
        car.increase_speed()

screen.exitonclick()
