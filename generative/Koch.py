import turtle
from math import sqrt

class Koch:

    def __init__(self, baseLength=1200, iterations=5, bgcolor='black', pencolor='green'):
        self.t = turtle.Pen()
        screen = self.t.getscreen()
        screen.bgcolor(bgcolor)
        self.bgcolor = bgcolor
        self.pencolor = pencolor
        self.baseLength = baseLength
        self.iterations = iterations
        self.t.speed(0)
        self.t.color(bgcolor)
        self.t.setpos(-200,100)
        self.t.color(pencolor)

    def drawKoch(self,levels):
        distance = self.baseLength/(3**levels)
        if levels == self.iterations:
            self.t.forward(distance)
            return
        self.drawKoch(levels+1)
        self.t.left(60)
        self.drawKoch(levels+1)
        self.t.right(120)
        self.drawKoch(levels+1)
        self.t.left(60)
        self.drawKoch(levels+1)

    def endThis(self):
        turtle.done()    

    def display(self):
        self.drawKoch(1)
        self.t.right(120)
        self.drawKoch(1)
        self.t.right(120)
        self.drawKoch(1)
        self.endThis()

if __name__ == '__main__':
    k = Koch()
    k.display()