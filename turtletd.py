import turtle #importer turtle pour pouvoir l'utiliser
from random import random, randrange, getrandbits, randint #importer random pour pouvoir laisser le choix à l'ordinateur. Le choix sera aléatoire.
from turtle import Screen, Turtle  #pour pouvoir utiliser screen turtle, demander des questions à l'utilisateur

window = Screen()

colorb = None

while colorb is None:
    colorb = window.textinput("Choose a background color between black, red or yellow", "Color:")
window.bgcolor(colorb)

color = None
while color is None:
    color=window.textinput("quelle couleur voulez vous que les bords soit?","couleur:")
    turtle.pencolor(color)

z=window.textinput("nommez votre fichier(vous ne pouvez qu'utiliser des lettres",'name:')
window.title(z)

turtle.setup(width=1, height=1)#agrandit le screen
turtle.screensize(10000,10000)#pour que l'utilisateur puisse scrooll

import turtle
from random import random

x=int(window.textinput("choisissez les coordonnées où commencer.","x:"))
y=int(window.textinput("choisissez les coordonnées où commencer.","y:"))
s=window.textinput("choisissez l'épaisseur de l'étoilee","epaisseur")
nb=int(window.textinput("combien d'étoile","nb:"))
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
