import random
import time
import turtle


#Bewegingsfuncties
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





