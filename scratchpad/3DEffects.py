import turtle
import math
import random

def resetOrigin(aame, coordinates):
    aame.penup()
    aame.setpos(coordinates[0], coordinates[1])
    aame.pendown()

def drawRectangle(aame, coordinates, heading, height, width, fillColor, bool3D):
    aame.color(fillColor)
    aame.begin_fill()
    resetOrigin(aame,coordinates)
    aame.setheading(heading)
    aame.forward(width)
    aame.left(90)
    aame.forward(height)
    aame.left(90)
    aame.forward(width)
    aame.left(90)
    aame.forward(height)
    aame.end_fill()

    if bool3D:
        minDistance = min(255-fillColor[0], 255-fillColor[1], 255-fillColor[2])
        widthSteps = (width//4)+1
        step = minDistance // widthSteps
        while width > 3:
            coordinates = (coordinates[0]+2, coordinates[1]+2)
            height = height - 4
            width = width - 4
            fillColor = lighterShade(fillColor, step=step)
            drawRectangle(aame, coordinates, heading, height, width, fillColor, False)

def lighterShade(rgb,step=1):
    r,g,b = rgb
    return (r+step, g+step, b+step)

def display():
    t = turtle.Pen()
    t.speed(0)
    coordinates = -200, -200
    resetOrigin(t,coordinates)
    heading = t.heading()
    height = 270
    width = 130
    screen = t.getscreen()
    screen.bgcolor('black')
    screen.colormode(255)
    color = (random.randrange(0,255,1),random.randrange(0,255,1),random.randrange(0,255,1))
    drawRectangle(t, coordinates, heading, height, width, color, True)
    turtle.done()

if __name__ == '__main__':
    display()