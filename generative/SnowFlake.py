import turtle
import math

def resetOrigin(aame, coordinates):
    aame.penup()
    aame.setpos(coordinates[0], coordinates[1])
    aame.pendown()
    aame.pencolor('white')

def nextOrigins(coordinates, length):
    """
         1
       6   2
       5   3
         4  
    """
    result = []
    x,y = coordinates
    cos = math.cos(math.radians(30))
    sin = math.sin(math.radians(30))
    divisionalFactor = 4
    multiplicationFactor = divisionalFactor - 1
    newlength = round(length/divisionalFactor)
    rightX = round(x+multiplicationFactor*cos*newlength)
    leftX = round(x-multiplicationFactor*cos*newlength)
    upY = round(y-multiplicationFactor*sin*newlength)
    downY = round(y+multiplicationFactor*sin*newlength)
    origX = round(x)

    topVertexY = round(y - multiplicationFactor*newlength)
    botVertexY =  round(y + multiplicationFactor*newlength)

    result.append(((origX, topVertexY),newlength))
    result.append(((rightX, upY),newlength)) 
    result.append(((rightX, downY), newlength))
    result.append(((origX, botVertexY), newlength))
    result.append(((leftX, upY),newlength)) 
    result.append(((leftX, downY),newlength))
    return result

def drawHex(aame, coordinates, length):
    aame.setheading(30)
    aame.forward(length)
    resetOrigin(aame, coordinates)

    for i in range(0, 6, 1):
        aame.left(60)
        aame.forward(length)
        resetOrigin(aame, coordinates)

def display():
    aame = turtle.Pen()
    screen = aame.getscreen()
    screen.bgcolor('black')
    aame.pencolor('white')
    aame.pensize(2)
    aame.speed(0)

    pos = aame.position()
    length = 200

    queue = []
    queue.append((pos, length))

    numIterations = 250

    for i in range(0, numIterations, 1):
        (pos, length) = queue.pop(0)
        drawHex(aame, pos, length)
        queue.extend(nextOrigins(pos, length))
    
    while(len(queue) > 0):
        (pos, length) = queue.pop(0)
        drawHex(aame, pos, length)

    turtle.done()

if __name__ == '__main__':
    display()