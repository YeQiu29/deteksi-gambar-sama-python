import turtle as t 
#importing the module as "t"

def spiral_shape(p,c):
 #creating a function with parameters "p" and "c"
	if p > 0:
 #if the p is less than 0,
		t.forward(p)
#moving the turtle forward at p units
		t.right(c)
 #setting the turtle right at an angle of c
		spiral_shape(p-5,c)
 #calling the function with the arguments as given


t.shape('classic')
 #setting the shape of the turtle as "classic"
t.reset()
 #resetting the turtle
t.pen(speed=25)
 #setting the speed of the pen to 25
length = 400
 #declaring a variable "length" to 400
turn_by = 121
 #declaring a varibale "turn_by" to 121
t.penup()
 #the drawing is not ready
t.setpos(-length/2, length/2)
 #setting the position as given
t.pendown()
 #starting to draw
spiral_shape(length, turn_by)
 #calling the function with the given arguments