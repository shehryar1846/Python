import turtle
turtle.Screen().setup(300,400)
turtle.Screen().bgcolor("orange")
polygon=turtle.Turtle()
num_sides=6
side_lenght=70
angle=360/num_sides
for i in range(num_sides):
    polygon.forward(side_lenght)
    polygon.right(angle)
turtle.done()