from graph_display import *
import tkinter as tk
from button_row import *


root=tk.Tk()
root.configure(bg="white")


frame1=framereturn(root)
frame1.pack()
canvas=graphplot(root)
canvas.get_tk_widget().pack()
canvas.draw()
bottomframe=bottomframe(root)
bottomframe.pack()
exit_button=tk.Button(root,text='Exit',command=quit,bg='red',fg='white',padx=15,pady=5)
exit_button.pack()


root.attributes('-fullscreen',True)
root.title('Tabledrummer')
root.mainloop()