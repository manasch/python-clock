import turtle as tr
import time
import tkinter as tk

wn = tr.Screen()
wn.bgcolor("black")
wn.setup(width=1000, height=600)
wn.title("Analogue Clock")
wn.tracer(0)


pen = tr.Turtle()
pen.hideturtle()
pen.speed(0)

def draw_circle(pen,r,fillcolor=False,col="white"): #col - pencolor
    if fillcolor==True:
        pen.up()
        pen.goto(0,r)
        pen.setheading(180)
        pen.pensize(4)
        pen.color(col)
        pen.pendown()
        pen.fillcolor(col)
        pen.begin_fill()
        pen.circle(r)
        pen.end_fill()

        pen.penup()
        pen.goto(0,0)
        pen.setheading(90)
    else:
        pen.up()
        pen.goto(0,r)
        pen.setheading(180)
        pen.pensize(4)
        pen.color(col)
        pen.pendown()
        pen.circle(r)

        pen.penup()
        pen.goto(0,0)
        pen.setheading(90)

def draw_line(pen,col="white"):

    for i in range(60):
        if i % 5 == 0:
            pen.pensize(4)
            pen.up()
            pen.fd(170)
            pen.pendown()
            pen.fd(30)
            pen.penup()
            pen.goto(0,0)
        else:
            pen.pensize(2)
            pen.up()
            pen.fd(190)
            pen.pendown()
            pen.fd(10)
            pen.penup()
            pen.goto(0,0)
        pen.rt(6)




def min_hand(pen,m):
    
    pen.up()
    pen.goto(0,0)
    pen.color("white")
    pen.pensize(3)
    pen.setheading(90)
    angle=(m/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.bk(20)
    pen.fd(140)

def sec_hand(pen,s):

    pen.up()
    pen.goto(0,0)
    pen.color("red")
    pen.pensize(5)
    pen.setheading(90)
    angle=(s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.bk(20)
    pen.fd(160)

def hour_hand(pen,h):

    pen.up()
    pen.goto(0,0)
    pen.color("white")
    pen.pensize(4)
    pen.setheading(90)
    angle=(h/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.bk(20)
    pen.fd(100)



def print_num():
    deg=90
    i=12
    while i > 0:
        pen.goto(0,0)
        pen.setheading(deg)
        pen.up()
        pen.fd(140)
        pen.write(str(i),align="center",font=("Courier",25,"normal"))
        pen.penup()
        deg+=30
        i-=1


while True:
    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))
    h=(h*60 + m)/60

    draw_circle(pen,200)
    draw_circle(pen,220)
    draw_circle(pen,5,True,"white")
    draw_line(pen)
    min_hand(pen,m)
    sec_hand(pen,s)
    hour_hand(pen,h)
    print_num()

    wn.update()
    time.sleep(1)
    pen.clear()

wn.mainloop()