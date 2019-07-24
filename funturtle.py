import turtle
turtle.shape('square')
def up():
    turtle.forward(10)
def down():
    turtle.backward(10)
def left():
    turtle.right(90)
def right():
    turtle.left(90)
turtle.onkeypress(up, "w")
turtle.onkeypress(down, "s")
turtle.onkeypress(left, "d")
turtle.onkeypress(right, "a")
turtle.listen()
turtle.meinloop()
