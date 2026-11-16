from myFunctions import *

# Puts the sun in the top right
bob.penup()
bob.goto(850,350)
bob.pendown()
sun(100,50)

bob.pensize(10)
# ________________________________________________
# Puts 100 stars in random positions with random angle
for times in range(100):
    x = randint(-1000,550)
    y = randint(-700,525)
    jump(x,y)
    star(25,144)
    angle1 = randint(1,359)
    angle2 = randint(1,359)
    turn(angle1,angle2)
    jump(x,y)
