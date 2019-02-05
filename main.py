from tkinter import Tk,font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import button_row as bt
import wave
import numpy as np


root = tk.Tk()

class App:

    buttons=["KICK","SNARE" ,"HI-HAT"]

    def __init__(self, root):
        self.f = Figure(figsize=(10, 4))
        self.a = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, root)

        #title
        title=tk.Label(height=1,text="TableDrummer",bg='white',fg='darkblue')
        title.configure(relief=tk.FLAT,font='Times 28 bold italic',width=15,)
        title.pack()


        # upper row of buttons
        self.frame1 = bt.framereturn(root,self)
        self.frame1.pack()
        self.frame1.place(relx=.32, rely=.1)
        # ------------------------

        # graph
        self.graphplot()
        self.canvas.get_tk_widget().pack()
        # ---------------------------

        # bottom row of buttons
        bottomframe = bt.bottomframe(root,self)
        bottomframe.pack()
        # ----------------------------

        # Exit button
        exit_button = tk.Button(root, text='Exit', command=quit, bg='darkred', fg='white', padx=15, pady=5)
        exit_button.configure(bd=4, relief=tk.RAISED, activebackground='red', activeforeground='white')
        exit_button.pack()
        # ----------------------------
        root.mainloop()

    def callback(self,selection):
        if selection=="TABALA":
            self.instrumentupdate(1)
        elif selection=="JAZZ":
            self.instrumentupdate(2)


    def wavread(self,filename):
        wavefile = wave.open(filename, 'r')
        signal = wavefile.readframes(-1)
        signal = np.fromstring(signal, 'Int16')
        return signal

    def graphplot(self):
        soundwave = self.wavread('samples/bass1.wav')
        self.waveform=self.a.plot(soundwave)
        self.canvas.draw()

    def graphupdate(self,s_wave):
        self.a.clear()
        soundwave = self.wavread('samples/bass1.wav')
        if(s_wave==0):
            soundwave = self.wavread('samples/bass1.wav')
        elif (s_wave == 1):
            soundwave = self.wavread('samples/bass2.wav')
        elif (s_wave == 2):
            soundwave = self.wavread('samples/snr1.wav')
        elif (s_wave == 3):
            soundwave = self.wavread('samples/snr2.wav')
        self.a.plot(soundwave)
        self.canvas.draw()

    def instrumentupdate(self,inst_n):
        if inst_n==1:
            self.buttons=["LEFT" , "RIGHT", "RIM"]
            self.frame1.pack_forget()
            self.frame1=bt.framereturn(root,self)
            self.frame1.pack()
            self.frame1.place( relx=.32, rely=.1)
        elif inst_n==2:
            self.buttons = ["KICK","SNARE" ,"HI-HAT"]
            self.frame1.pack_forget()
            self.frame1 = bt.framereturn(root, self)
            self.frame1.pack()
            self.frame1.place(relx=.32, rely=.1)


# tkinter window config
def kr(event):
    print("esc")
    if (event.keysym == 'Escape'):
        exit(0)



# root.attributes('-fullscreen',True)
root.configure(bg="white")  # window colour
root.configure(padx=30, pady=30)
root.title('Tabledrummer')
root.bind_all('<KeyRelease>', kr)  # press escape to close
app = App(root)
root.mainloop()


