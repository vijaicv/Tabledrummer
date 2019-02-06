

from tkinter import *

class b_row:
    def framereturn(s,root, self):
        btns = self.buttons
        frame1 = Frame(root)
        frame1.config(bg="white")
        i = 0
        while i < 3:
            b = Button(frame1, text=btns[i], width=10, font="sans 10 bold", command=lambda i=i: self.graphupdate(i))
            b.pack(side=LEFT, padx=10)
            i += 1
        return frame1

    def bottomframe(s,root, self):
        bframe = Frame(root)
        bframe.config(bg="white")
        l1 = Label(bframe, text='INSTRUMENT:')
        l1.config(bg="white")
        l1.pack(side=LEFT, padx=10)
        optionList = ["JAZZ", "TABALA"]
        b1 = StringVar(root)
        b1.set('JAZZ')
        instrument = OptionMenu(bframe, b1, *optionList, command=self.callback)
        instrument.configure(width=10, relief=FLAT, bg='darkgreen', fg='white', font='sans 10 bold',activeforeground='white', activebackground='green')
        instrument.pack(side=LEFT)
        b2 = Button(bframe, text="RESET")
        # b2.config(bd=4,relief=RAISED)
        b2.pack(side=LEFT, padx=10, pady=10)
        return bframe








