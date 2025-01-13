#setup

import turtle

#middle

t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.color("red")
t.pendown()
t.speed(10)

colors = ["red","blue","pink"]
for i in range(923908):
    t.color( colors[i % 3 ])
    t.forward(10 + i)
    t.left(91)


#ending

turtle.exitonclick()