

from tkinter import *

def framereturn(root):
    frame1 = Frame(root)
    frame1.config(bg="white")
    b1 = Button(frame1, text="BASS",width=10)
    b1.pack(side=LEFT)
    b1.config(bd=5,relief=RAISED)
    b2 = Button(frame1, text="SNEAR",width=10)
    b2.pack(side=LEFT,padx=10,pady=20)
    b2.config(bd=5, relief=RAISED)
    b3 = Button(frame1, text="HIGH HAT",width=10)
    b3.pack(side=LEFT)
    b3.config(bd=5, relief=RAISED)
    return frame1

def bottomframe(root):
    bframe = Frame(root)
    bframe.config(bg="white")
    b1=StringVar(root)
    b1.set('JAZZ')
    instrument=OptionMenu(root,b1,"JAZZ","TABALA")
    instrument.pack()
    b2 = Button(bframe, text="RESET")
    b2.config(bd=4,relief=RAISED)
    b2.pack(side=RIGHT,pady=10)
    return bframe








