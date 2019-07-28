import turtle
def up():
    turtle.forward(5)
def down():
    turtle.backward(10)
def left():
    turtle.right(90)
def right():
    turtle.left(90)
def num():
	turtle.speed(0)
	colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
	for x in range(360):
	    turtle.pencolor(colors[x % 6])
	    turtle.pencolor()
	    turtle.begin_fill()
	    turtle.forward(1)
	    turtle.right(1)
	    turtle.end_fill()
def num1():
    turtle.penup()
    turtle.goto(0,0)
    turtle.speed(0)
    turtle.pencolor('red')
    turtle.pendown
    for x in range(360):
        turtle.forward(x)
        turtle.right(90)

turtle.onkeypress(up, "w")
turtle.onkeypress(down, "s")
turtle.onkeypress(left, "d")
turtle.onkeypress(right, "a")
turtle.onkeypress(num, "q")
turtle.onkeypress(num1, "1")
turtle.listen()

turtle.mainloop()
