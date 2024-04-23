from turtle import Turtle,Screen
from day22paddleclass import paddle,ball,score
import time
#step 1 to create a screen
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
#step 2 create and move paddle
r_paddle=paddle((375,0))
l_paddle=paddle((-375,0))
r_paddle.move("Up","Down")
l_paddle.move("w","s")
b=ball()
point=score()
game_is=True
while game_is:
    time.sleep(b.move_speed)
    screen.update()
    b.move()
    # step-3 collsion with upper and lower wall
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce1()
    #step 4 collision with right paddle
    if b.distance(r_paddle)<50 and b.xcor()>350 or b.distance(l_paddle)<50 and b.xcor()<-350:
        b.bounce2()
    #step 5 missing the ball
    if b.xcor()>380:
      b.miss()
      point.l_point()
    if b.xcor()<-380:
      b.miss()
      point.r_point()


screen.exitonclick()








