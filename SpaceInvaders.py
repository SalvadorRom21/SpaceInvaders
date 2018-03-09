#Sapce Invdavers 
#Python 3.6.3 on Ubuntu Linux
#TheHeartlessOne March 6, 2018

import turtle
import os
import math
import random

#Setting up the window
window=turtle.Screen()
window.bgcolor("black")									#background color 
window.title("Space Invaders Game")						#setting name of window
window.bgpic("space_invaders_background.gif")			#setting background picture (credit pedbad)

#register shapes for enemy and player

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
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


#Set score board
score = 0

score_pen= turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition (-290, 270)
scorestring ="Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Ariel",14,"normal"))
score_pen.hideturtle()


#Creating the player turtle
player = turtle.Turtle()								#create a player turtle
player.color("blue")									#set its color 
player.shape("player.gif")								#set shape 
player.penup()											#not drawing line so pen up
player.speed(0)											#speed as fast as possible
player.setposition(0,-280)								#set the position of the turtle
player.setheading(90)									#sets oriantation of player turtle to face up



#number of enemies
numberOfEnemies = 5										#nubmer of enemies we want on the screen

enemies = []											#list of enemies

#Add enemies to the list 

for i in range(numberOfEnemies):						#for loop to make numberOfEnemies 
	enemies.append(turtle.Turtle())

for enemy in enemies:									#all enemies will have the same characteristics

	#Creating the enemy turtle 
	#comment out bottom line after creating 
	#for loop above 
	#enemy = turtle.Turtle()								#create enemy Turtle
	enemy.color("red")										#set color of the enemy
	enemy.shape("invader.gif")									#set shape of the enemy
	enemy.penup()											#not drawing anything so pen up
	enemy.speed(0)											#speed as fast since its a game	
	x = random.randint (-200,200)							#generate random value of x between -200 and 200
	y = random.randint (100, 250)							#generate random value of y between 100 and 250
	enemy.setposition (x,y)									#set posotion of the enemy to Q1


enemyspeed = 2												#setting movement speed of enemy 





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
		os.system("aplay Beep2.wav&")
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

	for enemy in enemies:
		#Moving the enemy 
		x = enemy.xcor()									#getting x position of the enemy
		x += enemyspeed										#moving the enemy right 
		enemy.setx(x)										#set enemy new position to x 
		
		#moving the enemy down towards the player
		if enemy.xcor()> 280:								#if one enemy the edge do following
			
			for e in enemies:								#do to all enemies	
				y = e.ycor()								#getting y coordinate of enemy
				y -= 40										#lowering the enemy y value by 40
				e.sety(y)									#setting new value for y postition of enemy
			enemyspeed *= -1								#multiply 2*(-1) to make it negative


		if enemy.xcor()< -280:								#setting left boundry for enemy
			
			for e in enemies:
				y = e.ycor()								#get y position of enemy
				y -=40										#lower position -40
				e.sety(y)									#change position of enemy 
			enemyspeed *= -1								#multiply 2*(-1) to make it negative
		

		#checking collision between bullet and enemy
		if isCollision (bullet, enemy):						#if collision occurs
			os.system("aplay SFX_Explosion_01.wav&")		#sound for the system
			bullet.hideturtle()								#hide the bullet 
			bulletstate= "ready"							#change bullet stage to ready
			bullet.setposition(0,-400)						#setting postition of bullet below player
			x = random.randint (-200,200)					#generate random value of x between -200 and 200
			y = random.randint (100, 250)					#generate random value of y between 100 and 250
			enemy.setposition (x,y)							#set posotion of the enemy to Q1
			
			#update the score of the player
			score += 10 									
			scorestring ="Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Ariel",14,"normal"))
		


		#checking collision between player and enemy 
		if isCollision(player, enemy):						#if collision occurs between player and enemy 
			player.hideturtle()								#hide player turtle
			enemy.hideturtle()								#hide enemy turtle 	
			print ("Game Over")								#print game over to console
			break 											#break from game screen. 
	

	if bulletstate == "fire":
		y = bullet.ycor()								#getting bulet y core value
		y += bulletspeed								#adding bullet speed to value
		bullet.sety(y)									#setting y coordinate of bullet


	#What happens when bullet goes out of the screen.
	if bullet.ycor() > 275:								#getting bullet y cordinate
		bullet.hideturtle()								#hide bullet 
		bulletstate = "ready"







#raw_input swtiched to input for python version 3.6.3
delay = input ("Press enter to finish.") 				#stops the window from closing

