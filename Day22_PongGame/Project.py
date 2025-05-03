import turtle
import padel
import ball
import time
import score_board

screen = turtle.Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_padel = padel.Padel()
right_p = r_padel.move((570, 0))
l_padel = padel.Padel()
left_p = l_padel.move((-570, 0))

screen.listen()
screen.onkey(fun=r_padel.go_up, key="Up")
screen.onkey(fun=r_padel.go_down, key="Down")
screen.onkey(fun=l_padel.go_up, key="w")
screen.onkey(fun=l_padel.go_down, key="s")

ball_padel = ball.Ball()
score_traking = score_board.Scoreboard()


game_on = True
while game_on:

    time.sleep(ball_padel.move_speed)
    screen.update()
    ball_padel.visual()


    #detect colition
    if ball_padel.ycor() > 330 or ball_padel.ycor() < -330:
            ball_padel.bounce_y()

    #detect colition with paddel
    if ball_padel.distance(r_padel) < 70 and ball_padel.xcor() > 540 and ball_padel.xcor() < 560 or ball_padel.distance(l_padel) < 70 and ball_padel.xcor() < -540 and ball_padel.xcor() > -560:
        ball_padel.bounce_x()
    
    if ball_padel.xcor() > 720:
        ball_padel.r_reset_ball()
        score_traking.increase_score_l()
        speed =- 0.01

    elif ball_padel.xcor() < -720:
        ball_padel.l_reset_ball()
        score_traking.increase_score_r()
        speed =- 0.01
    
  
screen.exitonclick()

