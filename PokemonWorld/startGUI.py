import os
os.chdir('/Users/jpollack/Desktop/CodingFiles/PokemonWorld')
import tkinter as tk
from PIL import ImageTk, Image
def print(*args, **kwargs):
  from inspect import currentframe
  import os, builtins
  builtins.print(' '.join(args),'{}:{}'.format(os.path.basename(__file__), currentframe().f_back.f_lineno), **kwargs)
def setPokemon(poke):
  pass
def begin(window, root):
  window.withdraw()
  root.deiconify()
def close():
  exit()
def start(root):
  images = []
  startWindow = tk.Toplevel(root, width=640, height=640)
  startWindow.bind('<Return>', lambda event:begin(startWindow, root))

  background = tk.Canvas(startWindow, width=640, height=320)
  images.append(ImageTk.PhotoImage(Image.open('./images/dex/chimchar.png').convert('RGBA')))
  background.create_image(0, 0, anchor='nw', image=images[-1])
  images.append(ImageTk.PhotoImage(Image.open('./images/dex/piplup.png').convert('RGBA')))
  background.create_image(320, 0, anchor='n', image=images[-1])
  images.append(ImageTk.PhotoImage(Image.open('./images/dex/turtwig.png').convert('RGBA')))
  background.create_image(640, 0, anchor='ne', image=images[-1])
  background.grid(row=0, column=0, columnspan=3)
  turtwig = tk.Button(startWindow, text='Turtwig', command=lambda:begin(startWindow, root))
  chimchar = tk.Button(startWindow, text='Chimchar', command=lambda:print('chimchar'))
  piplup = tk.Button(startWindow, text='Piplup', command=lambda:print('piplup'))
  chimchar.grid(row=1, column=0, sticky='ew')
  piplup.grid(row=1, column=1, sticky='ew')
  turtwig.grid(row=1, column=2, sticky='ew')
  startWindow.protocol('WM_DELETE_WINDOW', close)
  startWindow.mainloop()