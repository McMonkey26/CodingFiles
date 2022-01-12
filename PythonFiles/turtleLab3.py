import turtle
#initializing the turtle
etch = turtle.Turtle()
#starting a loop that will run forever
while(True):
    #gets your input, and puts it to a variable
    direction = str(input('text'))
    #using your input to move
    if(direction == "w"):
        etch.setheading(90)
        etch.fd(10)
    elif(direction == "a"):
        etch.setheading(180)
        etch.fd(10)
    elif(direction == "s"):
        etch.setheading(270)
        etch.fd(10)
    elif(direction == "d"):
        etch.setheading(0)
        etch.fd(10)
    elif(direction == "x"):
        etch.reset()
        etch.goto(0,0)
        etch.setheading(90)
    elif(direction == "quit"):
        break
turtle.done()
