import turtle

def resetPos(coordinates, turtle):
    x,y = coordinates
    turtle.up()
    turtle.hideturtle()
    turtle.setpos(x,y)
    turtle.showturtle()
    turtle.down()

def display():
    colors = ['red','purple','blue','white','green','orange','yellow']
    t = turtle.Pen()
    t.speed(0)
    screen = t.getscreen()
    screen.bgcolor('black')

    pos = t.position()
    for x_scalar in range(0,5):
        x = pos[0]+(x_scalar-2)*100
        for y_scalar in range(0,5):
            y = pos[1]+(y_scalar-2)*100
            for i in range(120,0,-1):
                resetPos((x,y),t)
                t.pencolor(colors[i%7])
                t.forward(100)
                t.left(3)
    
    t.down()


if __name__ == '__main__':
    display()