from tkinter import *
from tkinter.ttk import *
import sys
import os

class GUI(Frame, width, height):
	global master

	master = Tk()

	def start(self):
		mainloop()

	def create_label(self, name, r, c):
		e = Entry(Label(master, text=name).grid(row=r))
		e.grid(row=r, column=c)
		print(e)

	def __init__(self, name):
		master.title(name)
		master.geometry(f"{width}x{height}")