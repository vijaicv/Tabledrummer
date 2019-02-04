from button_row import *
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import wave


def wavread(filename):
    wavefile = wave.open(filename, 'r')
    signal = wavefile.readframes(-1)
    signal = np.fromstring(signal, 'Int16')
    return signal



root=tk.Tk()
root.configure(bg="white")

frame1= tk.Frame(root)
frame1.pack()


soundwave=wavread('samples/bass1.wav')
f=Figure(figsize=(6,6))
a=f.add_subplot(111)
a.plot(soundwave)


b1.pack(side = LEFT)


canvas = FigureCanvasTkAgg(f,root)
canvas.get_tk_widget().pack()
canvas.draw()


exit_button=tk.Button(root,text='Exit',command=quit,bg='red',fg='white',padx=15,pady=5)
exit_button.pack()


root.attributes('-fullscreen',True)
root.title('Tabledrummer')
root.mainloop()


