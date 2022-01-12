#random word from list, random color from list
#must enter the color, not the word
#30 seconds to play
#get 1 point for correct answer, lose a point for incorrect answer
#pick a new random word color combo after they answer and press button
#score is shown
#list of colors to use (use color names)

import tkinter as tk
import random

def countdown():
    global timeLeft

    # if a game is in play
    if timeLeft > 0:

        # decrement the timer.
        timeLeft -= 1

        # update the time left label
    timeLabel.config(text = "Time left: "
                               + str(timeLeft))

        # run the function again after 1 second.
    timeLabel.after(1000, countdown)

#we've learned this in class
def buttonPress():
    global timeLeft, score
    #if a game is running
    if timeLeft > 0:
        #if the answer is correct
        if userGuess.get() == colorWord['fg']:
            score += 1
        else:
            score -= 1
        #make a new random color word and random color
        nextWordIndex = random.randint(0, len(possColors)-1)
        nextColorIndex = random.randint(0, len(possColors)-1)
        colorWord.config(text=possColors[nextWordIndex], fg=possColors[nextColorIndex])
        #update the score
        scoreLabel.config(text="Score: "+str(score))
        #empty the entry box
        userGuess.delete(0, 'end')
    #if the game just ended and the user didnt input their last answer in time
    elif userGuess.get() != '':
        #delete the answer
        userGuess.delete(0, 'end')
        #make the color invisible
        colorWord.config(text='')
    #if the game needs to start
    else:
        #makes 30 seconds left and resets score to 0
        timeLeft = 30
        score = 0
        #sets the color to a random color
        colorWord.config(text=possColors[random.randint(0, len(possColors)-1)], fg=possColors[random.randint(0, len(possColors)-1)])
        #sets the score to 0
        scoreLabel.config(text="Score: 0")

#we haven't learned this
def enterColor(event):
    global timeLeft, score
    #if a game is running
    if timeLeft > 0:
        #if the answer is correct
        if userGuess.get() == colorWord['fg']:
            score += 1
        else:
            score -= 1
        #make a new random color word and random color
        nextWordIndex = random.randint(0, len(possColors)-1)
        nextColorIndex = random.randint(0, len(possColors)-1)
        colorWord.config(text=possColors[nextWordIndex], fg=possColors[nextColorIndex])
        #update the score
        scoreLabel.config(text="Score: "+str(score))
        #empty the entry box
        userGuess.delete(0, 'end')
    #if the game just ended and the user didnt input their last answer in time
    elif userGuess.get() != '':
        #delete the answer
        userGuess.delete(0, 'end')
        #make the color invisible
        colorWord.config(text='')
    #if the game needs to start
    else:
        #makes 30 seconds left and resets score to 0
        timeLeft = 30
        score = 0
        #sets the color to a random color
        colorWord.config(text=possColors[random.randint(0, len(possColors)-1)], fg=possColors[random.randint(0, len(possColors)-1)])
        #sets the score to 0
        scoreLabel.config(text="Score: 0")


#make a new window
root = tk.Tk()

#make a list of all the colors
possColors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white']

#initialize score and timer variables
score = 0
timeLeft = 0


#label to display time remaining
timeLabel = tk.Label(root, text="Click Play to start", bg=root['bg'])
timeLabel.pack()

#label to display score
scoreLabel = tk.Label(root, text="Score: 0", bg=root['bg'])
scoreLabel.pack()

#label to display color word
colorWord = tk.Label(root, text='', bg=root['bg'], font=('Helvetica', 32))
colorWord.pack()

#entry point for user to guess from
userGuess = tk.Entry(root, highlightbackground=root['bg'], relief='ridge')
userGuess.bind('<Return>', enterColor) #we haven't learned this
userGuess.pack()

#comment out line 122 and decomment lines 128 and 129 for what we have learned in class

#button for user to input answer
#guessButton = tk.Button(root, text='Start', command=buttonPress, highlightbackground=root['bg'], relief='ridge')
#guessButton.pack()

#starts the counter
countdown()
root.mainloop()
