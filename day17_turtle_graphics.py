from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("classic")
s = Screen()
s.colormode(255)

#! Draw a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# #! Draw dotted lines
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# #! Harder Shapes

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
# "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(number_of_side):
#     angle = 360/number_of_side
#     for _ in range(number_of_side):
#         tim.forward(100)
#         tim.right(angle)

# for shape_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_n)


# #! Generate a random walk
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#            "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# random.choice(colours)
# directions = [0, 90, 270, 360, -90, -270]

# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.width(10)
#     tim.forward(10)
#     tim.speed(10)
#     tim.setheading(random.choice(directions))

#! Draw a spirograph


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")

for _ in range(100):
    tim.color(random_colour())
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)
    print(current_heading)
    tim.circle(100)


my_screen = Screen()
my_screen.exitonclick()
