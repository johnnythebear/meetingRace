from turtle import *
from random import randint

def createTrack():
    speed(0)
    penup()
    goto(-140, 140)

    for dist in range(16):
        write(dist, align='center')
        right(90)
        forward(10)
        for n in range(30):
            pendown()
            forward(5)
            penup()
            forward(5)
        backward(310)
        left(90)
        forward(20)

def createTurtles(name, color):
    mate = []
    for i in range(len(name)):
        mate.append(Turtle())
        mate[i].color(color[randint(0, len(color)-1)])
        mate[i].shape('turtle')

        mate[i].penup()
        mate[i].goto(-160, 110-i*30)
        mate[i].write(name[i])
        mate[i].pendown()
    return mate

def raceTurtles(mate):
    for turn in range(100):
        for i in range(len(mate)):
            mate[i].forward(randint(1,5))

names = ['András', 'Bendi', 'Brigi', 'Csabi', 'Dezső', 'Dorián', 'Feri', 'Heni', 'Johnny', 'Katica']
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'black']
createTrack()
mates = createTurtles(names, colors)
raceTurtles(mates)
exitonclick()
