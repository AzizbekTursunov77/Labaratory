import turtle

turtle.shape('turtle')

rotations_number = 10
step = 10
length = step
for i in range(2*rotations_number):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    length += step