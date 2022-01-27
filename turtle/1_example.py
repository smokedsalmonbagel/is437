import turtle

#setup the window
turtle.setup(width=0.5, height=0.5)
screen = turtle.Screen()
width, height = screen.window_width(), screen.window_height()
canvas = screen.getcanvas()

#this controls where the window will pop up - use 0,0 if you dont see anything
left, top = 3000, 100
geom = '{}x{}+{}+{}'.format(width, height, left, top)
canvas.master.geometry(geom)

#Your turtle code below:

t = turtle.Turtle()

t.speed(1)
t.forward(100)
t.rt(90)
t.forward(5)
t.rt(90)
t.forward(100)
t.lt(90)
t.forward(5)
t.lt(90)
t.forward(100)


n=10
while n <= 40:
    t.circle(n)
    n = n+1
    
    
   
#keep this at the bottom:
turtle.exitonclick()