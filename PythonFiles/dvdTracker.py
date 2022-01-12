# import turtle as tl
# # tl.screensize(200, 200)
# screenSize = (90, 160)
# margin = 2
# distance = 3
# tl.setworldcoordinates(-margin, -margin, screenSize[0]+margin, screenSize[1]+margin)
# logo = tl.Turtle()
# logo.setpos(0, 0)
# logo.setpos(screenSize[0], 0)
# logo.setpos(screenSize[0], screenSize[1])
# logo.setpos(0, screenSize[1])
# logo.setpos(0, 0)
# # input(0)
# logo.left(45)
# # print(logo.heading())
# # logo.right(90)
# # print(logo.heading())
# # logo.right(90)
# # print(logo.heading())
# # logo.right(90)
# # print(logo.heading())
# # logo.left(90)
# # print(logo.heading())
# # logo.left(90)
# # print(logo.heading())
# logo.forward(1)
# logo.speed(0)
# # logo.ht()
# print(tl.screensize())
# while not logo.pos() == (0, 0):
#   if logo.pos()[0] > screenSize[0] and logo.heading() == 45.0:
#     # logo.backward(distance)
#     logo.left(90)
#   elif logo.pos()[0] > screenSize[0] and logo.heading() == 315.0:
#     # logo.backward(distance)
#     logo.right(90)
#   elif logo.pos()[0] < 0 and logo.heading() == 225.0:
#     # logo.backward(distance)
#     logo.left(90)
#   elif logo.pos()[0] < 0 and logo.heading() == 135.0:
#     # logo.backward(distance)
#     logo.right(90)
#   if logo.pos()[1] > screenSize[1] and logo.heading() == 135.0:
#     # logo.backward(distance)
#     logo.left(90)
#   elif logo.pos()[1] > screenSize[1] and logo.heading() == 45.0:
#     # logo.backward(distance)
#     logo.right(90)
#   elif logo.pos()[1] < 0 and logo.heading() == 225.0:
#     # logo.backward(distance)
#     logo.right(90)
#   elif logo.pos()[1] < 0 and logo.heading() == 315.0:
#     # logo.backward(distance)
#     logo.left(90)
#   logo.forward(distance)
#   # print(logo.pos(),logo.heading())
#   # num += 1
#   # if num % 1000 == 0:
#   #   break
# tl.done()
import tkinter as tk
size = (400,300)
class switch:
  def __init__(self, value):
    self.v = value
  def case(self, test):
    return test == self.v

def drawLine(canvas, startPos, maxPos, angle):
  s = switch(angle)
  if s.case(0):
    canvas.create_line(startPos[0], startPos[1], startPos[0], 0)
    angle = 4
    return ((startPos[0], 0), angle)
  elif s.case(1):
    x = maxPos[0] - startPos[0]
    y = startPos[1]
    distance = x if x < y else y
    canvas.create_line(startPos[0], startPos[1], startPos[0]+distance, startPos[1]-distance)
    angle = 5
    return ((startPos[0]+distance, startPos[1]+distance), angle)
  elif s.case(2):
    canvas.create_line(startPos[0], startPos[1], maxPos[0], startPos[1])
    angle = 6
    return ((maxPos[0], startPos[1]), angle)
  elif s.case(3):
    x = maxPos[0] - startPos[0]
    y = maxPos[1] - startPos[1]
    distance = x if x < y else y
    canvas.create_line(startPos[0], startPos[1], startPos[0]+distance, startPos[1]+distance)
    angle = 7
    return ((startPos[0]+distance, startPos[1]+distance), angle)
  elif s.case(4):
    canvas.create_line(startPos[0], startPos[1], startPos[0], maxPos[1])
    angle = 0
    return ((startPos[0], maxPos[1]), angle)
  elif s.case(5):
    x = startPos[0]
    y = startPos[1]
    distance = x if x < y else y
    canvas.create_line(startPos[0], startPos[1], startPos[0]-distance, startPos[1]+distance)
    angle = 1
    return ((startPos[0]-distance, startPos[1]+distance), angle)
  elif s.case(6):
    canvas.create_line(startPos[0], startPos[1], 0, startPos[1])
    angle = 2
    return ((0, startPos[1]), angle)
  elif s.case(7):
    x = startPos[0]
    y = startPos[1]
    distance = x if x < y else y
    canvas.create_line(startPos[0], startPos[1], startPos[0]-distance, startPos[1]-distance)
    angle = 3
    return ((startPos[0]-distance, startPos[1]-distance), angle)
stop = True
pos = (0, 0)
angle = 3
def dvd(canvas):
  global stop, pos, angle
  # while not stop:
  pos, angle = drawLine(canvas, pos, size, angle)
def stopDraw():
  global stop, canvas
  dvd(canvas)
  stop = not stop
  print('Stop:{}, Pos:{}, Angle:{}'.format(stop, pos, angle))
  stopStart.text = 'Start' if stop else 'Stop'
root = tk.Tk()
root.geometry(f'{size[0]+4}x{size[1]+34}')
canvas = tk.Canvas(root, height=size[1], width=size[0], bg='green')
r = 50
coords = (0,0)
canvas.create_oval(coords[0]-r, coords[1]-r, coords[0]+r, coords[1]+r, fill='red')
coords = (size[0], 0)
canvas.create_oval(coords[0]-r, coords[1]-r, coords[0]+r, coords[1]+r, fill='blue')
coords = (size[0], size[1])
canvas.create_oval(coords[0]-r, coords[1]-r, coords[0]+r, coords[1]+r, fill='white')
coords = (0, size[1])
canvas.create_oval(coords[0]-r, coords[1]-r, coords[0]+r, coords[1]+r, fill='gray')
dvd(canvas)
canvas.place(x=2, y=2, width=size[0], height=size[1])
stopStart = tk.Button(root, text='Stop', command=stopDraw)
stopStart.place(x=0, y=size[1]+10)
root.mainloop()