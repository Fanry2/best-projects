import tkinter
import tkinter as tk

window=tkinter.Tk()
canvas=tkinter.Canvas(window,width=1525, height=850, bg ="white")
canvas.pack()

lastX, lastY=0,0
colour="black"

def store_position(event):
    global lastX, lastY
    lastX=event.x
    lastY=event.y

def on_Click(event):
    store_position(event)

def on_drag(event):
    canvas.create_line(lastX, lastY,event.x,event.y, fill=colour, width=7)
    store_position(event)

canvas.bind("<Button-1>", on_Click)
canvas.bind("<B1-Motion>", on_drag)

red_id=canvas.create_rectangle(100,10,20,30,fill="red")
blue_id=canvas.create_rectangle(100,35,20,55,fill="blue")
green_id=canvas.create_rectangle(100,60,20,80,fill="green")
pink_id=canvas.create_rectangle(100,85,20,105,fill="pink")
yellow_id=canvas.create_rectangle(100,110,20,130,fill="yellow")
white_id=canvas.create_rectangle(100,135,20,155,fill="white")
gray_id=canvas.create_rectangle(100,160,20,180,fill="gray")
black_id=canvas.create_rectangle(100,185,20,205,fill="black")
purple_id=canvas.create_rectangle(100,210,20,230,fill="purple")

def set_colour_blue(event):
    global colour
    colour="blue"

def set_colour_green(event):
    global colour
    colour="green"

def set_colour_pink(event):
    global colour
    colour="pink"

def set_colour_yellow(event):
    global colour
    colour="yellow"

def set_colour_white(event):
    global colour
    colour="white"

def set_colour_black(event):
    global colour
    colour="black"

def set_colour_red(event):
    global colour
    colour="red"

def set_colour_gray(event):
    global colour
    colour="gray"

def set_colour_purpl(event):
    global colour
    colour="purple"

canvas.tag_bind(blue_id, "<Button-1>", set_colour_blue)
canvas.tag_bind(red_id, "<Button-1>", set_colour_red)
canvas.tag_bind(green_id, "<Button-1>", set_colour_green)
canvas.tag_bind(pink_id, "<Button-1>", set_colour_pink)
canvas.tag_bind(yellow_id, "<Button-1>", set_colour_yellow)
canvas.tag_bind(white_id, "<Button-1>", set_colour_white)
canvas.tag_bind(black_id, "<Button-1>", set_colour_black)
canvas.tag_bind(purple_id, "<Button-1>", set_colour_purpl)
canvas.tag_bind(gray_id, "<Button-1>", set_colour_gray)

window.mainloop()
