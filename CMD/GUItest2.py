import tkinter as tk
from tkinter import simpledialog

from tkinter import *

root = tk.Tk()

USER_INP = simpledialog.askstring(prompt="typ uw naam:", title="Uw naam alstublieft")

gui = Tk(className='Python Examples - Window Color')
gui.configure(bg='blue')

gui.mainloop()


print("hello", USER_INP)