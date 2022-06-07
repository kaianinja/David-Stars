import turtle #importer turtle pour pouvoir l'utiliser
from random import random, randrange, getrandbits, randint #importer random pour pouvoir laisser le choix à l'ordinateur. Le choix sera aléatoire.
from turtle import Screen, Turtle  #pour pouvoir utiliser screen turtle, demander des questions à l'utilisateur

window = Screen()

colorb = None

while True:
    colorb = window.textinput("Choose a background color between pink,white and teal", "pink,white or teal:")
    if colorb=="pink" or colorb=="teal" or colorb=="white":
        break
    else:
        continue
window.bgcolor(colorb)

color = None
while True :
    color=window.textinput("Choose a color between red,black and blue for the border color.","red,blue or black:")
    if color=="red" or color=="blue" or color=="black":
        break
    else:
        continue
turtle.pencolor(color)

z=window.textinput("Name your file(you can only use letters)",'name:')

if z.isalpha():
    window.title(z)
else:
    while(not z.isalpha()):
        z=window.textinput("Name your file with letters only.",'name:')
    window.title(z)

turtle.setup(width=1, height=1)#makes Screen bigger
turtle.screensize(10000,10000)#to let user scroll to find the stars

import turtle
from random import random


x=y=nb=s=0

while x==0 and y==0 and nb==0 and s==0:
    try:
        x=int(window.textinput("Please choose an x coordinate.","x:"))
        y=int(window.textinput("please choose a y coordinate.","y:"))
        s=int(window.textinput("choisissez l'épaisseur de l'étoilee","epaisseur"))
        nb=int(window.textinput("combien d'étoile","nb:"))
    
    except:
        x=y=s=nb=0

    
p=0



turtle.hideturtle()
turtle.pensize(s)
turtle.hideturtle()           #make the turtle invisible
turtle.penup()                #don't draw when turtle moves
turtle.goto(x,y)              #move the turtle to a location
turtle.showturtle()           #make the turtle visible
turtle.pendown()     
turtle.pencolor(color)



while p<nb:
    if p==0:
        turtle.right(60)
        turtle.forward(50)
        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()
        turtle.forward(100)

        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()
        turtle.forward(100)

        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()
        turtle.forward(100)

        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()
        turtle.forward(100)

        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()
        turtle.forward(100)

        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()

        turtle.pencolor(colorb)
        turtle.up()
        turtle.right(90)
        turtle.forward(1000)
        turtle.down()
        p+=1


    else:
        turtle.right(60)
        turtle.forward(50)
        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()
        turtle.forward(100)

        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()
        turtle.forward(100)

        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()
        turtle.forward(100)

        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()
        turtle.forward(100)

        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()
        turtle.forward(100)

        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()# next part is for doing another triangle to complete missing triangle

        turtle.right(60)
        turtle.forward(50)
        turtle.color(random(), random(), random())
        turtle.pencolor(color)
        turtle.begin_fill() 
        turtle.left(120)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(180)
        turtle.end_fill()
        turtle.forward(100)
        
        turtle.right(180)
        turtle.forward(50)
        turtle.pencolor(colorb)
        turtle.up()
        turtle.right(randint(1,360))#met que ce soit un random chiffre ici
        turtle.forward(randint(1,500))
        turtle.down()
      
        p+=1
