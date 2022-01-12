import tkinter as tk
from tkinter import messagebox

#creates main window
window = tk.Tk()

def getSquare():
    num1 = entry.get()
    num = str(float(num1)**0.5)
    messagebox.showinfo('Message', num)


inputN = tk.Label(text='please input a number')
inputN.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(text='click to calculate', command=getSquare)
button.pack()
window.mainloop()
