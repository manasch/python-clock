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
pen.pensize(2)

def draw_circle(pen,r,fillcolor=False,col="#2F76C8"): #col - pencolor
    if fillcolor==True:
        pen.up()
        pen.goto(0,r)
        pen.setheading(180)
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
        pen.color(col)
        pen.pendown()
        pen.circle(r)

        pen.penup()
        pen.goto(0,0)
        pen.setheading(90)

def draw_line(pen,col="#2F76C8"):

    i=0
    while i < 12:
        pen.color(col)
        pen.fd(180)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
        i+=1
    
    j=0
    while j < 60:
        pen.color(col)
        pen.fd(190)
        pen.pendown()
        pen.fd(10)
        pen.penup()
        pen.goto(0,0)
        pen.rt(6)
        j+=1


def draw_hands(h, m, s, pen):
    

    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = (h/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(80)

    pen.penup()
    pen.goto(0,0)
    pen.color("green")
    pen.setheading(90)
    angle = (m/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

    pen.penup()
    pen.goto(0,0)
    pen.color("yellow")
    pen.setheading(90)
    angle = (s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(30)

#def print_num():



while True:
    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))

    draw_circle(pen,200)
    draw_circle(pen,220)
    draw_circle(pen,20,True,"#58636f")
    draw_line(pen)
    draw_hands(h,m,s,pen)
    
    wn.update()
    time.sleep(1)
    pen.clear()

wn.mainloop()