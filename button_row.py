

from tkinter import *


class b_row:
    def framereturn(s,root, self):
        btns = self.button_labels
        frame1 = Frame(root)
        frame1.config(bg="white")
        i = 0

        while i < 3:
            b = Button(frame1, text=btns[i], width=10, font="sans 10 bold", command=lambda i=i: self.graphupdate(i),)
            b.pack(side=LEFT, padx=10)
            i += 1
        return frame1

    def bottomframe(s,root, self):
        ##bottom frame
        bframe = Frame(root)
        bframe.config(bg="white")
        #top of bottom frame

        tframe=Frame(bframe)
        tframe.config(bg="white")
        #slider
        l = Label(tframe, text='SENSITIVITY:')
        l.config(bg="white")
        l.pack(side=TOP)
        w = Scale(tframe, from_=0, to=50, orient=HORIZONTAL, bg="white")
        w.pack(side=TOP)
        l1 = Label(tframe, text='INSTRUMENT:')
        l1.config(bg="white")
        l1.pack(side=TOP)
        optionList = ["JAZZ", "TABALA"]
        b1 = StringVar(root)
        b1.set('JAZZ')
        instrument = OptionMenu(tframe, b1, *optionList, command=self.callback)
        instrument.configure(width=10, relief=FLAT, bg='yellow', fg='black', font=('helvetica', 10, 'bold'), activebackground='pale green')
        instrument.pack(side=RIGHT,padx=10)
        tframe.pack(pady=10)

        #bottom of bottom frame
        subframe=Frame(bframe)
        subframe.config(bg="white")
        b3 = Button(subframe, text='RE-MAP', bg='blue', fg='white', font='sans 10 bold')
        b3.config(bd=4, relief=RAISED, activebackground="darkblue",width=8)
        b3.pack(side=LEFT)
        b2 = Button(subframe, text="RESET",bg='tomato')
        b2.config(bd=4, relief=RAISED,width=8)
        b2.pack(side=LEFT,padx=30)
        subframe.pack(pady=5)
        # Exit button
        exit_button = Button(subframe, text='Exit', command=quit, bg='darkred', fg='white', padx=15, pady=5)
        exit_button.configure(bd=4, relief=RAISED, activebackground='red', activeforeground='white',width=8)
        exit_button.pack(side=RIGHT)

        return bframe











