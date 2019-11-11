from tkinter import *
from random import randint

def makeblocklist(numblocks,cwidth,cheight,wblock,hblock):
    blocklist = []
    margin = 50
    for block in range(numblocks):
        randx = randint(0,wblock - margin)
        randy = randint(0,hblock - margin)
        blockinfo = [randx,randy,randx+cwidth,randy+cheight]
        blocklist.append(blockinfo)
    return blocklist
        
def draw_each_frame():
    c1.delete("all")
    c1.create_oval(herox, heroy, herox + sizehero, heroy + sizehero)
    for block in blocks:
        c1.create_rectangle(block[0], block[1], block[2], block[3])

def hitcheck(x,y,blocks):
    count = 0
    for block in blocks:
        if (x >= block[0] and x <= block[2] and y >= block[1] and y <= block[3]):
            return count # return which block was hit
        count = count + 1
    return -99 # no hit detected

def moveright(event):
    global herox
    herox = herox + movepixels
    didithit = hitcheck(herox,heroy,blocks)
    if (didithit != -99):
        blocks.pop(didithit) # remove block from blocks list
    c1.after(10, draw_each_frame) # redraw

win = Tk()
cwidth = 800
cheight = 600
herox = 50
heroy = 50
sizehero = 30
movepixels = 30
blocks = makeblocklist(10,50,50,cwidth,cheight)
c1 = Canvas(win, width=800, height=600)
win.bind('<Right>', moveright)
c1.pack()
c1.after(10, draw_each_frame)

mainloop()
