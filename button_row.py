

from tkinter import *

def framereturn(root):
    frame1 = Frame(root)
    b1 = Button(frame1, text="BASS")
    b1.pack(side=LEFT)
    b2 = Button(frame1, text="SNEAR")
    b2.pack(side=LEFT)
    b3 = Button(frame1, text="HIGH HAT")
    b3.pack(side=LEFT)

    return frame1

def bottomframe(root):
    bframe=Frame(root)
    b1=Button(bframe,text="MODE")
    b1.pack(side=LEFT)
    b2=Button(bframe,text="RESET")
    b2.pack(side=RIGHT)
    return bframe








