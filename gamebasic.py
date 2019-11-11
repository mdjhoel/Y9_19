from tkinter import *
from random import randint

def draw_each_frame():
    c1.delete("all")
    c1.create_oval(herox, heroy, herox + sizehero, heroy + sizehero)
    
def moveright(event):
    global herox # access herox for updating its value
    herox = herox + movepixels
    c1.after(10, draw_each_frame) # redraw

win = Tk()
cwidth = 800
cheight = 600
herox = randint(0,cwidth)
heroy = randint(0,cheight)
sizehero = 30
movepixels = 30
c1 = Canvas(win, width=cwidth, height=cheight)
win.bind('<Right>', moveright)
c1.pack()
c1.after(10, draw_each_frame) # call function after 10ms delay

mainloop()
