import random
import turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    

   
    def position(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = turtle.Turtle("square")
            new_car.turtlesize(1, 2)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-210, 210)
            new_car.speed("fastest")
            new_car.setpos([300, random_y])
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

