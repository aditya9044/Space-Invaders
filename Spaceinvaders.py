import turtle
import os
import winsound
import math
import random

#Set up screen
wn= turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("background.gif")

turtle.register_shape("invaders.gif")
turtle.register_shape("player.gif")

#draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.up() 
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score=0
#Draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring= "Score:%s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14,"normal"))
score_pen.hideturtle()

#Create the player turtle
player= turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)


playerspeed=15

number_of_enemies=5
enemies=[]

for i in range (number_of_enemies):
    #create enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:

    enemy.color("red")
    enemy.shape("invaders.gif")
    enemy.penup()
    enemy.speed(0)
    x= random.randint(-200,200)
    y= random.randint(100,250)
    enemy.setposition(x,y)

enemyspeed=2

#create the players bullet

bullet= turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)             
bullet.hideturtle()             

bulletspeed=20

#define bullet state
#ready- ready to fire             
#fire - bullet is firing
bulletstate ="ready"             


#move player left and right
def move_left():
    x = player.xcor()
    x= x-playerspeed
    if x<-280:
        x=-280
    player.setx(x)
def move_right():
    x=player.xcor()
    x=x+playerspeed
    if x>280:
        x=280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        winsound.PlaySound("laser",winsound.SND_ASYNC)
        bulletstate="fire"     
        x=player.xcor()
        y=player.ycor()+10        
        bullet.setposition(x,y)
        bullet.showturtle()

def iscollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+ math.pow(t1.ycor()-t2.ycor(),2))
    if distance <15:
        return True
    else:
        return False

#Create keyboard bindings
    
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")             


#main game loop
while True :

   for enemy in enemies:
       
       
       #Move The Enemy
       x=enemy.xcor()
       x=x+enemyspeed
       enemy.setx(x)

       #move the enemy back and down
       if enemy.xcor() > 280:
          for e in enemies:
              y=e.ycor()
              y=y-40
              e.sety(y)
          enemyspeed= enemyspeed*-1
       if enemy.xcor() < -280:
          for e in enemies:
              y=e.ycor()
              y=y-40
              e.sety(y)
          enemyspeed= enemyspeed*-1
       if iscollision(bullet,enemy):
          winsound.PlaySound("explosion",winsound.SND_ASYNC) 
          bullet.hideturtle()
          bulletstate= "ready"
          bullet.setposition(0,-400)
          x=random.randint(-200,200)
          y=random.randint(100,250)
          enemy.setposition(x,y)
          score =score + 10
          scorestring= "Score: %s" %score
          score_pen.clear()
          score_pen.write(scorestring, False, align="left", font=("Arial", 14,"normal"))
       if iscollision(player,enemy):
          player.hideturtle()
          enemy.hideturtle()
          print("GAME OVER")
          break


   if bulletstate=="fire":
       y=bullet.ycor()
       y=y+bulletspeed
       bullet.sety(y)
          
   if bullet.ycor()>275:
       bullet.hideturtle()
       bulletstate="ready"

      
   
   
delay = input("Press enter to finish.")
