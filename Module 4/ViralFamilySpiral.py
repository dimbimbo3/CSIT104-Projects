import turtle     # Set up turtle graphics

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange",
        "purple", "white", "brown", "gray", "pink" ]
family = []       # Set up an empty list for family names

# Ask for the first name
name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
# Keep asking for names
while name != "":
    # Add their name to the family list
    family.append(name)
    # Ask for another name, or end
    name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
    
# outer spiral loop
for x in range(100):
    t.forward(x*4)          # Just move the turtle on the screen
    position = t.position() # remember this corner of the spiral
    heading = t.heading()   # remember the direction we were heading
    # "inner" spiral loop
    for n in range(len(family)):
        t.pendown()
        t.pencolor(colors[n%len(family)%10])
        t.write(family[n%len(family)], font=("Arial", int((x+4)/4), "bold") )
        t.right(360/len(family) - 2)
        t.width(x/20)
        t.penup()
        t.forward(x)
    #end loop
    t.setx(position[0]) # go back to the big spiral's x location
    t.sety(position[1]) # go back to the big spiral's y location
    t.setheading(heading) # point in the big spiral's heading
    t.left(360/len(family) + 2)  # aim at the next point on the big spiral
