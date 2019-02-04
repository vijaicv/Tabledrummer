from graph_display import *
import tkinter as tk


root=tk.Tk()
root.configure(bg="white")

canvas=graphplot(root)
canvas.get_tk_widget().pack()
canvas.draw()
exit_button=tk.Button(root,text='Exit',command=quit,bg='red',fg='white',padx=15,pady=5)
exit_button.pack()


root.attributes('-fullscreen',True)
root.title('Tabledrummer')
root.mainloop()