import tkinter


m=tkinter.Tk()
m.title('Tabledrummer')
def play():
	print("hello")
button=tkinter.Button(m,text='kick',width='20',command=play)

button=tkinter.Button(m,text='Stop',width=25,command=m.destroy)
button.pack()
m.mainloop()

