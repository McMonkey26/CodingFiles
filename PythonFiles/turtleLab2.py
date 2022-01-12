#circle: go forward 1 pixel and left 1 degree, repeat 360 times
#square: go forward 100 pixels, left 90 degrees, repeat 4 times
#triangle: go forward 100 pixels, left 120 degrees, repeat 3 times
#star: go forward 100 pixels, left 144 degrees, repeat 5 times
import turtle
run = True
steve = turtle.Turtle()
while(run):
    shape = input("Pick a shape: circle, square, triangle, or star: ")
    color = input("Pick a color: orange, citrine, air superiority blue, dark liver, or dark liver (horses): ")
    steve.speed(5)
    steve.shape("turtle")
    steve.color("green")
    turtle.colormode(255)
    if color == "orange":
        steve.pencolor((176,107,38))
    elif color == "air superiority blue":
        steve.pencolor((112,160,197))
    elif color == "citrine":
        steve.pencolor((228,208,10))
    elif color == "dark liver":
        steve.pencolor((83,75,79))
    elif color == "dark liver (horses)":
        steve.pencolor((84,61,55))
    if shape == "circle":
        for x in range(360):
            steve.forward(1)
            steve.left(1)
    elif shape == "square":
        for x in range(4):
            steve.forward(100)
            steve.left(90)
    elif shape == "triangle":
        for x in range(3):
            steve.forward(100)
            steve.left(120)
    elif shape == "star":
        for x in range(5):
            steve.forward(100)
            steve.left(144)
    steve.hideturtle()
    if(input("Would you like to play again?")=="yes"):
        steve.reset()
    else:
        run = False

turtle.done()
