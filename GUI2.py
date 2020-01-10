import tkinter as tk

master = tk.Tk()

canvas = tk.Canvas(master, width=400, height=300)
canvas.pack()

entry = tk.Entry(master)
canvas.create_window(200,140, window = entry)

def setConstants():
	x = entry.get()

	label = tk.Label(master, text='Values Set')
	canvas.create_window(200, 230, window=label)

button = tk.Button(text='Set Values', command=setConstants)
canvas.create_window(200, 180, window=button)

master.mainloop()