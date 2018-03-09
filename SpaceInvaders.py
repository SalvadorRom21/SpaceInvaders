#Sapce Invdavers 
#Python 3.6.3 on Ubuntu Linux
#TheHeartlessOne March 6, 2018

import turtle
import os
import math


#Setting up the window
window=turtle.Screen()
window.bgcolor("black")									#background color 
window.title("Space Invaders Game")						#setting name of window

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
player.setposition(0,-280)								#set the position of the turtle
player.setheading(90)									#sets oriantation of player turtle to face up

#Creating the enemy turtle 
enemy = turtle.Turtle()									#create enemy Turtle
enemy.color("red")										#set color of the enemy
enemy.shape("circle")									#set shape of the enemy
enemy.penup()											#not drawing anything so pen up
enemy.speed(0)											#speed as fast since its a game	
enemy.setposition (-200, 250)							#set posotion of the enemy to Q1
enemyspeed = 2											#setting movement speed of enemy 

#Creating player bullet
bullet = turtle.Turtle()								#create turtle bullet
bullet.color("yellow")									#give it yellow color 
bullet.shape("triangle")								#set its shape 
bullet.penup()											#not drawing line so penup
bullet.speed(0)											#speed of the bullet 0 for fastest
bullet.setheading(90)									#direction of bullet
bullet.shapesize(0.5,0.5)								#scale down by 1/2 
bullet.hideturtle()										#hiding turtle before we need it

bulletspeed = 20 

#Define bullet state
#ready - raedy to fire
#fire - bullet is moving 

bulletstate = "ready"									#the state of the bullet 


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

def fire_bullet():
	global bulletstate
	
	if bulletstate == "ready":							#after fire change state to fire
		bulletstate = "fire"

		x = player.xcor()								#x coordinate of player
		y = player.ycor() + 10							#y cordinate plus 10
		bullet.setposition(x,y)		
		bullet.showturtle()								#turle appearss

#detecting if bullet collided with an enemy
def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False







#create keyboard binding 
turtle.listen()											#listen for keyinputs 
turtle.onkey(move_left, "Left")							#calls move_left when left key is pressed
turtle.onkey(move_right, "Right")						#calls move_right when right key is pressed 
turtle.onkey(fire_bullet, "space")


#Main Game Loop 
while True:

	#Moving the enemy 
	x = enemy.xcor()									#getting x position of the enemy
	x += enemyspeed										#moving the enemy right 

	enemy.setx(x)										#set enemy new position to x 

	if enemy.xcor()> 280:								#setting right boundry for enemy
		y = enemy.ycor()								#getting y coordinate of enemy
		y -= 40											#lowering the enemy y value by 40
		enemyspeed *= -1								#multiply 2*(-1) to make it negative
		enemy.sety(y)									#setting new value for y postition of enemy

	if enemy.xcor()< -280:								#setting left boundry for enemy
		y = enemy.ycor()
		y -=40
		enemyspeed *= -1								#mutipply -2*(-1) to mae it positive
		enemy.sety(y)
	if bulletstate == "fire":
		y = bullet.ycor()								#getting bulet y core value
		y += bulletspeed								#adding bullet speed to value
		bullet.sety(y)									#setting y coordinate of bullet

	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"


#checking for collsiion between bullet and enemy
	if isCollision (bullet, enemy):
		bullet.hideturtle()
		bulletstate= "ready"
		bullet.setposition(0,-400)
		enemy.setposition(-200, 250)

	if isCollision(player, enemy):
		player.hideturtle()
		enemy.hideturtle()
		print ("Game Over")
		break 

#comment


#raw_input swtiched to input for python version 3.6.3
delay = input ("Press enter to finish.") 				#stops the window from closing

