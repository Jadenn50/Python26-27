import turtle
from random import *
bob = turtle.Turtle()
bob.speed(0)
turtle.colormode(255)
turtle.bgcolor(0,0,0)
bob.shape("turtle")
bob.color(255,165,0)
# ________________________________________________
# Sun function
def sun(dist,angle):
    for times in range(37):
        bob.circle(dist)
        bob.left(angle)
# ________________________________________________
# Star function
def star(distance,angles):
         for times in range(5):
            bob.forward(distance)
            bob.left(angles)
# ________________________________________________
# Jump function
def jump(x,y):
      bob.penup()
      bob.goto(x,y)
      bob.pendown()
# ________________________________________________
# Random turn function
def turn(angle1,angle2):
    bob.left(angle1)
    bob.right(angle2)
    












    


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
