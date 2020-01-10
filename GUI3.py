from tkinter import *

master = Tk()
master.title('Freeeeeee')
master.geometry(f"{400}x{300}")

canvas = Canvas(master, width=400, height=300)
canvas.pack()

entry = Entry(master)
canvas.create_window(200,140, window = entry)

test = 4

def retest():
	return test

def chtest(num):
	test = num
	master.destroy
	print(retest())

print(retest())

button = Button(text='Reee', command=chtest(entry.get()))
canvas.create_window(200, 180, window=button)


mainloop()