import turtle
def teken_kaart():
    kaart = turtle.Turtle()
    kaart.speed(0)
    kaart.color("white")
    kaart.penup()

    kaart.goto(-290,290)

    kaart.pendown()
    #Draw 4 sides
    for _ in range(4):
        kaart.forward(580)
        kaart.right(90)

    kaart.hideturtle()
