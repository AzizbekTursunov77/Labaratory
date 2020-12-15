import turtle

turtle.shape('turtle')

n=12
k=0
while k!=n:
    turtle.right(360/n)
    turtle.forward(70)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(70)
    turtle.right(180)
    k+=1