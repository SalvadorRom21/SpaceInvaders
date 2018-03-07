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

#Creating the enemy turtle 
enemy = turtle.Turtle()									#create enemy Turtle
enemy.color("red")										#set color of the enemy
enemy.shape("circle")									#set shape of the enemy
enemy.penup()											#not drawing anything so pen up
enemy.speed(0)											#speed as fast since its a game	
enemy.setposition (-200, 250)							#set posotion of the enemy to Q1
enemyspeed = 2											#setting movement speed of enemy 

playerspeed = 15
#setting up player movement
def move_left():										#moving player left 								
	x = player.xcor()									#getting player x coordinate
	x -= playerspeed									#setting player speed x = x-playerspeed

	if x < -280:										#bouncry checking left side
		x = -280

	player.setx(x)										#setting player position to x 
	
def move_right():										#moving player right 
	x = player.xcor()									#getting player x coordinate
	x += playerspeed									#setting player speed x = x + playerspeed

	if x > 280:											#boundry checking for right side						
		x = 280

	player.setx(x)										#setting player position to x 

#create keyboard binding 
turtle.listen()											#listen for keyinputs 
turtle.onkey(move_left, "Left")							#calls move_left when left key is pressed
turtle.onkey(move_right, "Right")						#calls move_right when right key is pressed 







#raw_input swtiched to input for python version 3.6.3
delay = input ("Press enter to finish.") 				#stops the window from closing

