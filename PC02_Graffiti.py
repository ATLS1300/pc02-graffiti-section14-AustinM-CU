#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author:  Austin McClendon
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

    #GLASSES
turtle.up()
turtle.goto(-20, 90)
turtle.down()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()
turtle.up()
turtle.goto(43, 100)
turtle.down()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.up()
#glasses lines
turtle.color(0,0,0)
turtle.goto(43, 125)
turtle.down()
turtle.pensize(6)
turtle.goto(-20, 115)
turtle.goto(-45,115)
turtle.goto(-90 ,115)
#glasses design (red trianlge LEFT)
turtle.up()
turtle.pensize(2)
turtle.goto(-20,95)
turtle.color(200,50,50)
turtle.setheading(90)
turtle.forward(25)
turtle.forward(10)
turtle.right(150)
turtle.down()
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
#blue trianlge LEFT
turtle.up()
turtle.goto(-20,100)
turtle.color(20,100,200)
turtle.setheading(270)
turtle.right(150)
turtle.down()
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.up()
#red triangle RIGHT
turtle.up()
turtle.pensize(2)
turtle.goto(43,105)
turtle.color(200,50,50)
turtle.setheading(90)
turtle.forward(25)
turtle.forward(10)
turtle.right(150)
turtle.down()
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
#blue trianlge RIGHT
turtle.up()
turtle.goto(43,110)
turtle.color(20,100,200)
turtle.setheading(270)
turtle.right(150)
turtle.down()
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.up()

    #TOP HAT
turtle.color(0,0,0)
turtle.up()
turtle.goto(-120, 170)
turtle.down()
turtle.pensize(1)
turtle.begin_fill()
#right side of brim
turtle.goto(70, 190)
turtle.goto(68, 205)
#left side of brim
turtle.goto(-122, 185)
turtle.goto(-120, 170)
turtle.end_fill()
turtle.up()
#top of hat 
turtle.goto(-90, 189)
turtle.down()
turtle.begin_fill()
turtle.goto(-95, 275)
turtle.goto(41,291)
turtle.goto(48,188)
turtle.end_fill()

    #WAND
turtle.up()
turtle.goto(50,-70)
turtle.down()
turtle.begin_fill()
turtle.goto(115,95) 
turtle.goto(130,90)
turtle.goto(68,-70)
turtle.goto(50,-70)
turtle.end_fill()



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
