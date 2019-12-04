
from tkinter import *

def deleteme(data):
    global mylist
    mylist.remove(data)
    redraw()

def redraw():
    for widget in widgetlist:
        widget.destroy()

    count = 0
    for i in mylist:
        #l.config(text=l.cget("text") + i[0] + " " + i[1] + "\n" )
        b = Button(listframe,text=str(count),command=lambda i=i: deleteme(i))
        widgetlist.append(b)
        b.grid(row=count,column=0)
        l = Label(listframe,text=i[0] + " " + i[1])
        widgetlist.append(l)
        l.grid(row=count,column=1)
        count = count + 1

def addme():
    global mylist
    mylist.append([e1.get(),e2.get()])
    redraw()

widgetlist = []
win = Tk()

e1 = Entry(win)
e1.pack()
e2 = Entry(win)
e2.pack()

b1 = Button(win,text="submit",command=addme)
b1.pack()

listframe = Frame(win)
listframe.pack()

mylist = []
mainloop()
