#Simple Snake Game in python 3
#By somya
#Part 1:Getting Started

import turtle
import time
import random
import calendar

delay= 0.1

#score
score=0
high_score=0

#Set up the bscreen
wn=turtle.Screen()
wn.title("HUNGRY SOLIS")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)
#turns off the screen updates
print(calendar.monthcalendar(2020,3))
print()

# Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score:  0  High score:  0",align="center",font=("Courier",24,"normal"))


#Functions
def go_up():
	if head.direction!="down":
		head.direction = "up"

def go_down():
	if head.direction!="up":
		head.direction = "down"

def go_left():
	if head.direction!="right":
		head.direction = "left"

def go_right():
	if head.direction!="left":
		head.direction = "right"

def move():
	if head.direction=="up":
		y = head.ycor()
		head.sety(y+20)

	if head.direction=="down":
		y=head.ycor()
		head.sety(y-20)
    
	if head.direction=="left":
		x=head.xcor()
		head.setx(x-20)

	if head.direction=="right":
	    	x=head.xcor()
	    	head.setx(x+20)
	
#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

#MAIN GAME LOOP
while True:
	wn.update()

	#collision with border
	if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
		time.sleep(1)
		head.goto(0,0)
		head.direction="stop"

		#hide segments
		for segment in segments:
			segment.goto(1000,1000)

		#clear segments
		segments.clear()

		#reset
		score=0

		pen.clear()
		pen.write("Score:  {}  High Score:  {}  ".format(score,high_score),align="center",font=("Courier",24,"normal"))


	if head.distance(food)<20:
		#move food to random pos
		x=random.randint(-290,290)
		y=random.randint(-290,290)
		food.goto(x,y)

		new_segment=turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("triangle")
		new_segment.color("light green")
		new_segment.penup()
		segments.append(new_segment)

		#increase score
		score += 10

		if score>high_score:
			high_score=score


		pen.clear()
		pen.write("Score:  {}  High Score:  {}  ".format(score,high_score),align="center",font=("Courier",24,"normal"))

		#move the end segment in reverse order
	for index in range(len(segments)-1,0,-1):
		x=segments[index-1].xcor()
		y=segments[index-1].ycor()
		segments[index].goto(x,y)

	#move segment 0 to head
	if len(segments)>0:
		x=head.xcor()
		y=head.ycor()
		segments[0].goto(x,y)
	

	move()

	#check for collision
	for segment in segments:
		if segment.distance(head)<20:
			time.sleep(1)
			head.goto(0,0)
			head.direction="stop"

			#hide segments
			for segment in segments:
				segment.goto(1000,1000)

			#clear segments
			segments.clear()

	time.sleep(delay)
    

wn.mainloop()