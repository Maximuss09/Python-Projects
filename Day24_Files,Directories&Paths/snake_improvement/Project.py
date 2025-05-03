import turtle
import snake_class
import time
import food
import scoreboard

def setup_controls():
    screen.listen()
    screen.onkeypress(fun=snake.up, key="w")
    screen.onkeypress(fun=snake.down, key="s")
    screen.onkeypress(fun=snake.left, key="a")
    screen.onkeypress(fun=snake.right, key="d")


def new_game():
    snake.start_again()
    food.refresh()
    score.restore()
    global game_on
    game_on = True
    setup_controls()
    


screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)

snake = snake_class.Snake()
food = food.Food()
score = scoreboard.Scoreboard()
setup_controls()



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
        info = screen.textinput(title="GAME OVER", prompt="Do you want to play again?  ").lower()
        if info == "yes":
            new_game()
        else:
            game_on = False

    #Detect collition with snake
    for segment in snake.new_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
            info = screen.textinput(title="GAME OVER", prompt="Do you want to play again?  ").lower()
            if info == "yes":
                new_game()
            else:
                game_on = False



screen.exitonclick()
