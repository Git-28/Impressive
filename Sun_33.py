import turtle as t

# Set up the screen
s = t.Screen()
s.bgcolor("white")

# Create a turtle
ipl_logo = t.Turtle()
ipl_logo.speed(0)
ipl_logo.color("orange")
ipl_logo.pensize(2)

# Draw a cricket ball (circle)
ipl_logo.begin_fill()
ipl_logo.circle(50)
ipl_logo.end_fill()

# Hide the turtle
ipl_logo.hideturtle()

# Display the logo
s.exitonclick()
