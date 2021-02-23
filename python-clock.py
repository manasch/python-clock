import turtle
import time


wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.title("Analogue Clock")
wn.tracer(0)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)

def draw_circle(h, m, s, pen):
    i=0
    pen.up()
    pen.goto(0,200)
    pen.setheading(180)
    pen.color("Blue")
    pen.pendown()
    pen.circle(200)

    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    while i < 12:
        pen.fd(180)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
        i+=1


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

while True:
    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))

    draw_circle(h,m,s,pen)
    wn.update()
    time.sleep(1)
    pen.clear()

wn.mainloop()