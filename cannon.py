from tkinter import *
import math
target =Tk()
canvas = Canvas(width=800,height=600)
canvas.pack()

xy = [(390, 350), (410, 350), (410, 410), (390, 410)]

polygon_item = canvas.create_polygon(xy)
center = 400, 500

def getangle(event):
    dx = canvas.canvasx(event.x) - center[0]
    dy = canvas.canvasy(event.y) - center[1]
    try:
        return complex(dx, dy) / abs(complex(dx, dy))
    except ZeroDivisionError:
        return 0.0 # cannot determine angle

def press(event):
    # calculate angle at start point
    global start
    start = getangle(event)

def motion(event):
    # calculate current angle relative to initial angle
    global start
    angle = getangle(event) / start
    offset = complex(center[0], center[1])
    newxy = []
    for x, y in xy:
        v = angle * (complex(x, y) - offset) + offset
        newxy.append(v.real)
        newxy.append(v.imag)
    canvas.coords(polygon_item, *newxy)

canvas.bind("<Button-1>", press)
canvas.bind("<B1-Motion>", motion)

mainloop()
