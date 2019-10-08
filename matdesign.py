from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

def test(event):
    global myimg # global keyword allows access to a variable from outside of function
    global can2
    root.filename =  filedialog.askopenfilename(initialdir = "/Users/mhoel/Pictures",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    myimage = Image.open(root.filename)
    myimage = myimage.resize((200, 150), Image.ANTIALIAS)
    myimg = ImageTk.PhotoImage(myimage)
    can2.create_image(0, 0, image = myimg, anchor = NW)

root = Tk()
root.title("photo tagger")
root.geometry("500x350")

# make 'navbar' frame - info http://effbot.org/tkinterbook/frame.htm
topframe = Frame(root,bg="blue")
topframe.pack(fill=X) # make as wide as root

# make a small canvas hamburger icon that binds as a button to a function
can1 = Canvas(topframe,height="20",bg="blue",highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill="white")
can1.create_line(0, 10, 20, 10,fill="white")
can1.create_line(0, 15, 20, 15,fill="white")
can1.bind("<Button-1>",test )
can1.pack(side=LEFT, padx=5, pady=5)

# create some space between bar and image frame
spaceframe = Frame(root,height=10)
spaceframe.pack(fill=X)

# create image 'card' frame
imgframe = Frame(root,borderwidth = 1.5, relief=RAISED, width=400,height=150)
imgframe.pack(fill=None, expand=False)

# use .grid within a packed (one on top of each other)
l1 = Label(imgframe,text="Welcome to photo tagger\nA test of Material Design in Tkinter",fg="blue")
l1.grid(row=0,column=1)
can2 = Canvas(imgframe,height=150,width=200)
can2.grid(row=0,column=0)

myimage = Image.open("/Users/mhoel/Desktop/matdesign/bremners.jpg")
myimage = myimage.resize((200, 150), Image.ANTIALIAS)
myimg = ImageTk.PhotoImage(myimage)
can2.create_image(0, 0, image=myimg, anchor = NW)

# create some space
spaceframe2 = Frame(root,height=20)
spaceframe2.pack(fill=X)

# data input frame
inputframe = Frame(root,borderwidth = 1.5, relief=RAISED, width=445,height=100)
inputframe.pack()
inputframe.pack_propagate(0) # don't let children of frame decide how big it will be

# use pack layout with side attribute instead of grid to show another layout method
l2 = Label(inputframe, text="Review",fg="blue")
l2.pack(side=LEFT)
txt = Text(inputframe,borderwidth = 1, relief=RAISED,height=80)
txt.pack(side=LEFT)

