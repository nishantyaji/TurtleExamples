import turtle
from math import sqrt as sqrt

def resetOrigin(aame, coordinates):
    aame.penup()
    aame.setpos(coordinates[0], coordinates[1])
    aame.pendown()
    aame.pencolor('white')

def fillTriangle(aame, coordinates, color):
    resetOrigin(aame,coordinates[0])
    aame.fillcolor(color)
    aame.begin_fill()
    aame.down()
    aame.goto(coordinates[1])
    aame.goto(coordinates[2])
    aame.goto(coordinates[0])
    aame.up()
    aame.end_fill()
    
def draw4Sections(aame, coordinates, color, depth, depthRequired):
    if depth == depthRequired:
        return
    mid = []
    length = len(coordinates)
    for i in range(0, length, 1):
        midpoint = ((coordinates[i][0] + coordinates[(i+1) % length][0])/2, (coordinates[i][1] + coordinates[(i+1) % length][1])/2)
        mid.append(midpoint)
    fillTriangle(aame, mid, color)
    for i in range(0, length,1):
        draw4Sections(aame, [ coordinates[i], mid[i], mid[(i-1+length)%length]], color, depth+1, depthRequired)
    
def firstTriangle(aame, length):
    pos = aame.position()
    coordinates = []
    coordinates.append((pos[0], pos[1] + length/sqrt(3)))
    coordinates.append((pos[0]-length/2, pos[1] - length/(2*sqrt(3))))
    coordinates.append((pos[0]+length/2, pos[1] - length/(2*sqrt(3))))
    return(coordinates)

def display():
    aame = turtle.Pen()
    screen = aame.getscreen()
    screen.bgcolor('black')
    aame.pencolor('white')
    aame.pensize(1)
    aame.speed(0)

    baseColor = 'green'
    removecolor = 'black'
    length = 400
    depthRequired = 6

    baseTriangle = firstTriangle(aame, length)
    fillTriangle(aame, baseTriangle, baseColor)
    draw4Sections(aame, baseTriangle, removecolor, 0, depthRequired)

    turtle.done()

if __name__ == '__main__':
    display()