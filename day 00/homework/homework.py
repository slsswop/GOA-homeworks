from turtle import *
# we want to paint a house


#step 1: draw a square
shape("turtle")
speed(10)
width(5)

color("brown")
begin_fill()

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("black")
begin_fill()
left(90)
forward(90) #height of the door
right(90)
forward(50)
right(90)
forward(90)
end_fill()

#end of door

#drawing a roof
penup()
goto(200,200)
pendown()
color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof 

#drawing windows
penup()
goto(40,170)
pendown()
color("grey")

left(30)
forward(50)#height of the window
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(25)
right(180)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(50)



penup()
goto(120,170)
pendown()

left(180)
forward(50)#height of the window
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(25)
right(180)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(50)



exitonclick() 
