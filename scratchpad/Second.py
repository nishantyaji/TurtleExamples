import turtle

aame = turtle.Turtle()
for i in range(100, 1, -1):
    aame.forward(i)
    aame.left(135)
    aame.forward(i)
    aame.right(45)
    
turtle.done()
#aame.getscreen().getcanvas().postscript(file="second.eps")