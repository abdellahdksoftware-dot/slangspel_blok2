import random
import time
import turtle

# Snelheid van de game loop (0.3 langzaam )
vertraging = 0.3

# Score bijhouden
score = 0
hoogste_score = 0

scherm = turtle.Screen()
scherm.title("Klassieke Snake Game (Rustig Tempo)")
scherm.bgcolor("black")
scherm.setup(width=600, height=600)
scherm.tracer(0)

#Het Eten
eten = turtle.Turtle()
eten.speed(0)
eten.shape("circle")
eten.color("red")
eten.penup()
eten.goto(0, 100)


Bewegingsfuncties
def ga_omhoog():
    if kop.direction != "down":
        kop.direction = "up"


def ga_omlaag():
    if kop.direction != "up":
        kop.direction = "down"


def ga_links():
    if kop.direction != "right":
        kop.direction = "left"


def ga_rechts():
    if kop.direction != "left":
        kop.direction = "right"


def beweeg():
    if kop.direction == "up":
        y = kop.ycor()
        kop.sety(y + 20)

    if kop.direction == "down":
        y = kop.ycor()
        kop.sety(y - 20)

    if kop.direction == "left":
        x = kop.xcor()
        kop.setx(x - 20)

    if kop.direction == "right":
        x = kop.xcor()
        kop.setx(x + 20)


#Toetsenbord Koppelingen
scherm.listen()
scherm.onkeypress(ga_omhoog, "Up")
scherm.onkeypress(ga_omlaag, "Down")
scherm.onkeypress(ga_links, "Left")
scherm.onkeypress(ga_rechts, "Right")


