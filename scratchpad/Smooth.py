import turtle
import math
import random

def resetOrigin(aame, coordinates):
    aame.penup()
    aame.setpos(coordinates[0], coordinates[1])
    aame.pendown()
    aame.pencolor('white')

aame = turtle.Pen()
screen = aame.getscreen()
screen.bgcolor('black')
aame.pencolor('white')
aame.pensize()
aame.speed(0)

(x,y) = aame.position()
xo,yo = (x,y)
aame.left(90)

numIterations = 35
colors = ['red','purple','blue','white','green','orange','yellow']

for i in range(0, numIterations, 1):
    resetOrigin(aame, (xo,yo))
    x,y = xo,yo
    aame.pencolor(colors[i%len(colors)])
    while (x < 200) and (y < 200):
        aame.forward(1)
        if aame.heading() > 120:
            randAngle = -3
        elif aame.heading() < 60:
            randAngle = 3
        else:   
            randAngle = random.randrange(-300,300,3)/100
        print(randAngle)
        aame.left(randAngle)
        (x,y) = aame.position()

aame.down()