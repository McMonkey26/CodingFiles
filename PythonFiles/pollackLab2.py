#ask for an amount of seconds
#store the seconds
#turn it into minutes
#get the remainder of the seconds
#turn the minutes into hours
#get the remainder of the minutes
#print the variables

totalSeconds = int(input("Enter an amount of seconds.\n"))
minutes = int(totalSeconds / 60)
seconds = int(totalSeconds % 60)
hours = int(minutes / 60)
minutes = int(minutes % 60)

print(totalSeconds,"seconds is",hours,"hours,",minutes,"minutes, and",seconds,"seconds.")
