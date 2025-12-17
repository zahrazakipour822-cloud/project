from turtle import Turtle,Screen
import random
color = ["coral2","DarkGreen","salmon","pink","red","goldenrod1","khaki2","HotPink4","blue","brown","gray70","DeepSkyBlue1"]


luna = Turtle()
luna.shape("turtle")
luna.color("DeepPink4")
luna.penup()
luna.goto(10,200)
luna.pendown()
def draw(num_sides):
    angel = 360 / num_sides
    for _ in range(num_sides):
        luna.forward(100)
        luna.right(angel)

for side in range(3,11):
    luna.color(random.choice(color))
    draw(side)


screen = Screen()
screen.exitonclick()