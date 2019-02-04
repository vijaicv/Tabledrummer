from graph_display import *
import tkinter as tk
from button_row import *


def kr(event):
    if(event.keysym == 'Escape'):
        root.destroy()



root=tk.Tk()
root.configure(bg="white")  #window colour

#upper row of buttons
frame1=framereturn(root)
frame1.pack()
# ------------------------

#graph
canvas=graphplot(root)
canvas.get_tk_widget().pack()
canvas.draw()
# ---------------------------

#bottom row of buttons
bottomframe=bottomframe(root)
bottomframe.pack()
#----------------------------

#Exit button
exit_button=tk.Button(root,text='Exit',command=quit,bg='darkred',fg='white',padx=15,pady=5)
exit_button.configure(bd=4,relief=RAISED,activebackground='red',activeforeground='white')
exit_button.pack()
#----------------------------


#tkinter window config
root.attributes('-fullscreen',True)
root.configure(padx=30,pady=30)
root.title('Tabledrummer')
root.bind_all('<KeyRelease>', kr)#press escape to close
root.mainloop()