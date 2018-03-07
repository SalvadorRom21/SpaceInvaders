#Sapce Invdavers 
#Python 3.6.3 on Ubuntu Linux
#TheHeartlessOne March 6, 2018

import turtle
import os

#Setting up the window
window=turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders Game")

#Set up to drawing boarder
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")								#set color of the line
border_pen.penup()										#lift turlte from board	
border_pen.setposition(-300,-300)						#set it to position -300,-300
border_pen.pendown()									#set turtle down to new position
border_pen.pensize(3)									#set width of the turtle 3 


#Draw the Boarder
for side in range(4):							
	border_pen.fd(600)									#forward 600 units
	border_pen.lt(90)									#turn left 90 degrees 
border_pen.hideturtle()									#hide turtle (could maybe do earlier in program)

#Creating the player turtle
player = turtle.Turtle()								#create a player turtle
player.color("blue")									#set its color 
player.shape("triangle")								#set shape 
player.penup()											#not drawing line so pen up
player.speed(0)											#speed as fast as possible
player.setposition(0,-250)								#set the position of the turtle
player.setheading(90)									#sets oriantation of player turtle to face up

playerspeed = 15
#setting up player movement
def move_left():
	x = player.xcor()
	x -= playerspeed

	if x < -280:
		x = -280

	player.setx(x)
	
def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280

	player.setx(x)


#create keyboard binding 
turtle.listen()	
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")







#raw_input swtiched to input for python version 3.6.3
delay = input ("Press enter to finish.") 

