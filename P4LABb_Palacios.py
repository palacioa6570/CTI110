import turtle

t = turtle.Turtle()

t.color("blue")
t.pensize(10)
t.penup()
t.goto(-150,50)

t.pendown()
t.right(65)
t.forward(200)

t.setpos(-150,50)
t.right(50)
t.forward(200)

t.penup()
t.setpos(-200,-70)
t.right(65)
t.pendown()
t.backward(100)

t.penup()
t.goto(-20,50)
t.pendown()
t.left(90)
t.forward(180)
t.goto(-20,-10)
t.circle(60,360)

