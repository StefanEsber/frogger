from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car_sleep_time = random.randint(1, 6)
        if car_sleep_time == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-300, 300)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        else:
            pass

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
