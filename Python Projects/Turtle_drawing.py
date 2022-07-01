# Method	        Parameter	    Description

# Turtle()	        None	        Creates and returns a new turtle object
# forward()	        amount	        Moves the turtle forward by the specified amount
# backward()	    amount      	Moves the turtle backward by the specified amount
# right()           angle       	Turns the turtle clockwise
# left()	        angle	        Turns the turtle counterclockwise
# penup()	        None	        Picks up the turtle’s Pen
# pendown()   	    None        	Puts down the turtle’s Pen
# up()	            None	        Picks up the turtle’s Pen
# down()        	None    	    Puts down the turtle’s Pen
# color()	        Color name  	Changes the color of the turtle’s pen
# fillcolor() 	    Color name	    Changes the color of the turtle will use to fill a polygon
# heading()	        None	        Returns the current heading
# position()    	None	        Returns the current position
# goto()      	    x, y	        Move the turtle to position x,y
# begin_fill()	    None	        Remember the starting point for a filled polygon
# end_fill()	    None	        Close the polygon and fill with the current fill color
# dot()	            None	        Leave the dot at the current position
# stamp()     	    None	        Leaves an impression of a turtle shape at the current location
# shape()	        shapename	    Should be ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’

import turtle
t=turtle.Turtle()
t.shape("arrow")
t.color ("red")
# begin_fill()
t.pensize(5)
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)

# end_fill()