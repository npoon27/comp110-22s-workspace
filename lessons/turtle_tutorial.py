from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.begin_fill()
i: int = 0
leo.speed(50)
leo.hideturtle()
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.penup()
leo.goto(45, 60)
leo.pendown()
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color("black")
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.speed(60)
side_length: float = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

bob.color("black")
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.speed(60)

i: int = 0
while (i < 3):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(122)
    i = i + 1
done()