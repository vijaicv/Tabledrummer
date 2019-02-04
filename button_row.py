

from tkinter import *

def framereturn(root):
    frame1 = Frame(root)
    frame1.config(bg="white")
    b1 = Button(frame1, text="BASS",width=10)
    b1.pack(side=LEFT)
    b2 = Button(frame1, text="SNEAR",width=10)
    b2.pack(side=LEFT,padx=10,pady=20)

    b3 = Button(frame1, text="HIGH HAT",width=10)
    b3.pack(side=LEFT)
    return frame1

def bottomframe(root):
    bframe = Frame(root)
    bframe.config(bg="white")
    b1 = Menubutton(bframe, text="MODE")
    b1.menu = Menu(b1, tearoff=0)
    b1["menu"] = b1.menu
    TBLAVar=IntVar()
    JAZZVar=IntVar()
    b1.menu.add_checkbutton(label="TABALA",variable=TBLAVar)
    b1.menu.add_checkbutton(label="JAZZ", variable=JAZZVar)
    b1.pack(side=LEFT,padx=50)
    b2 = Button(bframe, text="RESET")
    b2.pack(side=RIGHT,padx=50)
    return bframe








