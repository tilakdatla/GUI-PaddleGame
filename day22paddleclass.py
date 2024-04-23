from turtle import Turtle,Screen
class paddle(Turtle):
    def __init__(self,tuple):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(tuple)
        self.speed(10)
    def move(self,key1,key2):
        def Up():
            new_y = self.ycor() + 30
            self.goto(x=self.xcor(), y=new_y)
        def Down():
            new_y = self.ycor() - 30
            self.goto(x=self.xcor(), y=new_y)
        screen=Screen()
        screen.listen()
        screen.onkey(key=key1, fun=Up)
        screen.onkey(key=key2, fun=Down)

class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y=10
        self.x=10
        self.move_speed=0.1
    def move(self):
        new_x=self.xcor()+self.x
        new_y=self.ycor()+self.y
        self.goto(new_x,new_y)
    def bounce1(self):
        self.y*=-1
    def bounce2(self):
        self.x*=-1
        self.move_speed*=0.9
    def miss(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce2()

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score+=1
        self.clear()
        self.update()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update()
