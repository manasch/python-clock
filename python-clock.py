import turtle as tr
import time
import tkinter as tk

wn = tr.Screen()
wn.bgcolor("black")
wn.setup(width=1200, height=800)
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
        pen.up()
        pen.goto(0,-20)
        pen.setheading(deg)
        pen.up()
        pen.fd(145)
        pen.write(str(i),align="center",font=("Comic Sans MS",25,"normal"))
        pen.penup()
        deg+=30
        i-=1

def print_time(h,m,s):
    pen.up()
    pen.goto(0,240)
    pen.write(f"{'%02d'%h}:{'%02d'%m}:{'%02d'%s} {time.strftime('%p')}",align="center",font=("Comic Sans MS",25,"normal"))
    pen.up()
    pen.goto(0,-290)
    pen.write(f"{time.strftime('%d')}/{time.strftime('%b')}/{time.strftime('%Y')}, {time.strftime('%A')}",align="center",font=("Comic Sans MS",25,"normal"))


#def onclick():

while True:
    h=int(time.strftime("%I")) #returns the hour in 12 hour format
    m=int(time.strftime("%M")) #returns the minute
    s=int(time.strftime("%S")) #returns the second
    h1=(h*60 + m)/60

    draw_circle(pen,200)
    draw_circle(pen,220)
    draw_circle(pen,5,True,"white")
    draw_line(pen)
    min_hand(pen,m)
    sec_hand(pen,s)  
    hour_hand(pen,h1)
    print_num()
    print_time(h,m,s)


    wn.update()
    time.sleep(1)
    pen.clear()


#canvas=wn.getcanvas()
#button=tk.Button(canvas.master, text="Click Here",command=onclick)
#canvas.create_window(-300,-200,window=button)


wn.mainloop()