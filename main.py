import turtle as tr
import time
import tkinter as tk
from pytz import timezone
import menu
from menu import colors

wn = tr.Screen()
wn.setup(width=1200, height=750,starty=20)
wn.title("Analogue Clock")
wn.tracer(0)
def init():
    wn.bgcolor(colors["bg_col"])
init()
pen = tr.Turtle()
pen1 = tr.Turtle()
pen1.hideturtle()
pen.hideturtle()
pen.speed(0)
pen1.speed(0)


def draw_circle(pen,r,col,fillcolor=False,size=4): #col - pencolor
    pen.up()
    pen.goto(0,r)
    pen.setheading(180)
    pen.pensize(size)
    pen.color(col)
    pen.pendown()
    if fillcolor==True:
        pen.begin_fill()
        pen.circle(r)
        pen.end_fill()
    else:
        pen.circle(r)

def draw_line(pen,col):
    pen.color(col)
    for i in range(60):
        psize = 2
        pfd = 190
        pfd2 = 10
        # Prints longer stripes for 1-12
        if i % 5 == 0:
            psize = 4
            pfd = 170
            pfd2 = 30

        pen.pensize(psize)
        pen.up()
        pen.fd(pfd)
        pen.pendown()
        pen.fd(pfd2)
        pen.penup()
        pen.goto(0,0)
        pen.rt(6)

"""
h_type: hand type (hour,min,sec)
size: width of the pen
length: length of the hand
"""

def draw_hands(pen,h_type,size,length,col,v=True): # Set v as False to get the angle for hour, default is True for min & sec

    pen.up()
    pen.goto(0,0)
    pen.color(col)
    pen.pensize(size)
    pen.setheading(90)
    # determine hand position based on type for hour and minute/second 
    if v:
        angle=(h_type/60)*360
    else:
        angle=(h_type/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.bk(20)
    pen.fd(length)

def print_num(pen,col):
    deg=90
    i=12
    while i > 0:
        pen.color(col)
        pen.up()
        pen.goto(0,-20)
        pen.setheading(deg)
        pen.up()
        pen.fd(145)
        pen.write(str(i),align="center",font=("Comic Sans MS",25,"normal"))
        deg+=30
        i-=1

def print_time(h,m,s):
    pen.color('white')
    pen.up()
    pen.goto(0,240)
    pen.write(f"{'%02d'%h}:{'%02d'%m}:{'%02d'%s} {time.strftime('%p')}",align="center",font=("Comic Sans MS",25,"normal"))
    pen.up()
    pen.goto(0,-290)
    pen.write(f"{time.strftime('%d')}/{time.strftime('%b')}/{time.strftime('%Y')}, {time.strftime('%A')}",align="center",font=("Comic Sans MS",25,"normal"))

'''
t_zones = [
    "IST",
    "UTC",
]

clicked=tk.StringVar()
clicked.set(t_zones[0])

canvas=wn.getcanvas()
drop_down=tk.OptionMenu(canvas.master, clicked, *t_zones)
canvas.create_window(-300,-200,window=drop_down)
'''
def draw():
    # drawing the inner circle
    draw_circle(pen1,200,col=colors["i_circle"])

    # drawing the outer circle
    draw_circle(pen1,220,col=colors["o_circle"])

    # drawing the gear in the center 
    draw_circle(pen1,5,fillcolor=True,col=colors["gear"])

    # drawing the stripes 
    draw_line(pen1,col=colors["line"])

    print_num(pen1,col=colors["num"])

draw()

canvas=wn.getcanvas()

but=tk.Button(canvas.master, text="Customise",command=menu.menu)
canvas.create_window(450, 200, window=but)

# Infinite loop to keep the clock running until stopped
while True:
    print(colors["bg_col"])
    # Returns the hour in 12 hour format
    h=int(time.strftime("%I"))

    # Returns the minute
    m=int(time.strftime("%M"))

    # Returns the second
    s=int(time.strftime("%S")) 

    # hour hand position (position the handle between 3 & 4 when it's 3:30) 
    h1=(h*60 + m)/60    

    #Drawing the hour, minute and second hand
    draw_hands(pen,h1,4,100,v=False,col=colors["hour"]) # hour
    draw_hands(pen,m,2,140,col=colors["min"]) # minute
    draw_hands(pen,s,5,160,v=True,col=colors["sec"]) # second
    print_time(h,m,s)

    init()
    wn.update()
    time.sleep(1)
    pen.clear()






# mainloop() used to keep the screen running, closes instantly otherwise
#wn.mainloop()

