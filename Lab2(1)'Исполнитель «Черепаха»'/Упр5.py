import turtle

turtle.shape('turtle')

length = 5
n = 5
k = 0
while k != n:
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)

    turtle.penup()

    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)

    turtle.pendown()
    k += 1
    length += 10