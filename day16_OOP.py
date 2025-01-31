# from turtle import Turtle, Screen

# # !creating an object with the Turtle class, timmy is the object here,#!Turtle is the class written inside turtle module.
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue", "green")

# for steps in range(10):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(50)

# my_screen = Screen()
# print(my_screen.canvheight)  # ! it also printed the canvas height
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
table.align = "r"
print(table)