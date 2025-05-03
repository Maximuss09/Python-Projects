import time
from turtle import Screen
import player
import car_manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

"---- TURTLE ----"
ready_player = player.Player()
ready_player.movement()
screen.listen()
screen.onkeypress(fun=ready_player.walking, key="w")

"---- CARS ----"
cars = car_manager.CarManager()

score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.position()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(ready_player) < 30:
            game_is_on = False
            score.game_over()


    if ready_player.is_at_finish_line():
        ready_player.start_position()            
        cars.level_up()
        score.increse_level()


screen.exitonclick()