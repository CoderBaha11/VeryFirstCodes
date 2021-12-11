from turtle import *
from random import randint

for step in range(20):
    write(step, align='center')
    forward(5)

speed(2)
penup()
goto(-140, 140)

bani = Turtle()
bani.color('green')
bani.shape('turtle')
bani.penup()
bani.goto(-160, 90)

niba = Turtle()
niba.color('blue')
niba.shape('turtle')
niba.penup()
niba.goto(-160, 80)
pendown()

diay = Turtle()
diay.color('yellow')
diay.shape('turtle')
diay.penup()
diay.goto(-160, 70)
pendown()

aydi = Turtle()
aydi.color('red')
aydi.shape('turtle')
aydi.penup()
aydi.goto(-160, 60)
pendown()

haba = Turtle()
haba.color('black')
haba.shape('turtle')
haba.penup()
haba.goto(-160, 50)
pendown()

for turn in range(100):
    bani.forward(randint(1, 5))
    niba.forward(randint(2, 5))
    diay.forward(randint(3, 5))
    aydi.forward(randint(4, 5))
    haba.forward(randint(5, 5))

for step in range(15):
    write(step, align='center')

    forward(20)
    right(90)

    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(10)