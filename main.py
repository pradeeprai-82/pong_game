from turtle  import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((320, 0))
l_paddle = Paddle((-320, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    b_y = ball.ycor()
    
    if b_y > 280 or b_y < -280:
        ball.bounce_y()
    
    b_r_paddle = ball.distance(r_paddle)
    b_l_paddle = ball.distance(l_paddle)
    
    b_x = ball.xcor()
    
    if b_r_paddle < 50 and b_x > 340 or b_l_paddle < 50:
        ball.bounce_x()
        
    #detect r paddle misses
    if b_x > 300:
        ball.reset_position()
        
    #detect l paddle misses
    if b_x < -300:
        ball.reset_position()
        
screen.exitonclick()
