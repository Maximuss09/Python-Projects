import turtle
import snake_class
import time
import food
import scoreboard

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)

snake = snake_class.Snake()
food = food.Food()
score = scoreboard.Scoreboard()

screen.listen()
screen.onkeypress(fun=snake.up, key="w")
screen.onkeypress(fun=snake.down, key="s")
screen.onkeypress(fun=snake.left, key="a")
screen.onkeypress(fun=snake.right, key="d")


game_on = True
while game_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #Detect collisions with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extention()
        score.increase_score()
    #Detect collision with wall
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        game_on = False
        score.game_over()
    #Detect collition with snake
    for segment in snake.new_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
