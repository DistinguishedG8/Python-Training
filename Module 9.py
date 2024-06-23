
import turtle

#*Bird loop*

birdState = False
copyPaste = 2
#Declares variable

while birdState == False:
    userGuess = input("What can fly with wings? ").lower()
    userGuess = userGuess.replace("birds","bird")
    #Takes user input, makes small changes

    if userGuess == "bird":
        birdState = True
        print("You are correct!")
        for variableLoop in range(copyPaste):
            print("----\nFly you fools!")
            print(variableLoop)
        #For loop, that repeats 3 times
        break
    #Checks user guess

    else:
        print("Incorrect, please guess again.")
    #Error message, indicating an issue with the user input

for steps in [1,5,2]:
    print("----\ntest")
    print(steps)
#For Loop that iterates values as listed in the []


#*Draw a Color!*

userShape = input("-------\nWould you like to draw a shape? (Yes or No) ").lower()
userShape = userShape.replace("yes","y").replace("no","n")
#Requests user input, Checking if the user wants a shape

userSides = "one"
userColor = "black"
lineShape = False
angleShape = False
triangleShape = False
squareShape = False
pentagonShape = False
hexagonShape = False
heptagonShape = False
octagonShape = False
nonagonShape = False
decagonShape = False
#Declare variables

if userShape == "y":
    userDraw = True
    print("Let's begin!\n ")
#Checking if the user wants a shape

    userSides = input("How many sides would it have? (Max 10) ").lower()
    userColor = input("What color should it be? (Red, Green, or Blue) ").lower()
    #Request user input

elif userShape == "n":
    userDraw = False
    print("Okay, have a good day :(")
#Checking if the user does not want a shape

userSides = userSides.replace("one","1").replace("two","2").replace("three","3").replace("four","4").replace("five","5").replace("six","6").replace("seven","7").replace("eight","8").replace("nine","9").replace("ten","10")
userSides = int(userSides)
#Change userSides to a proper number

while userDraw == True:
        
    if userSides == 1:
        lineShape = True
        turtle.color(userColor)
        turtle.forward(100)
    #If the user wants a single line

    if userSides == 2:
        angleShape = True
        for sideLoop in range(userSides):
            turtle.color(userColor)
            turtle.forward(100)
            turtle.left(180/userSides)
            for secondSideLoop in range(userSides):
                turtle.color(userColor)
                turtle.forward(50)
                turtle.left(180/userSides)
                

    if userSides == 3:
        triangleShape = True
        for sideLoop in range(userSides):
            turtle.color(userColor)
            turtle.forward(100)
            turtle.left(360/userSides)
            for secondSideLoop in range(userSides):
                turtle.color(userColor)
                turtle.forward(50)
                turtle.left(360/userSides)
                

    if userSides == 4:
        squareShape = True
        for sideLoop in range(userSides):
            turtle.color(userColor)
            turtle.forward(100)
            turtle.left(360/userSides)
            for secondSideLoop in range(userSides):
                turtle.color(userColor)
                turtle.forward(50)
                turtle.left(360/userSides)
                

    if userSides == 5:
        pentagonShape = True
        for sideLoop in range(userSides):
            turtle.color(userColor)
            turtle.forward(100)
            turtle.left(360/userSides)
            for secondSideLoop in range(userSides):
                turtle.color(userColor)
                turtle.forward(50)
                turtle.left(360/userSides)
                

    if userSides == 6:
        hexagonShape = True
        for sideLoop in range(userSides):
            turtle.color(userColor)
            turtle.forward(100)
            turtle.left(360/userSides)
            for secondSideLoop in range(userSides):
                turtle.color(userColor)
                turtle.forward(50)
                turtle.left(360/userSides)
                

    if userSides == 7:
        heptagonShape = True
        for sideLoop in range(userSides):
            turtle.color(userColor)
            turtle.forward(100)
            turtle.left(360/userSides)
            for secondSideLoop in range(userSides):
                turtle.color(userColor)
                turtle.forward(50)
                turtle.left(360/userSides)
                

    if userSides == 8:
        octagonShape = True
        for sideLoop in range(userSides):
            turtle.color(userColor)
            turtle.forward(100)
            turtle.left(360/userSides)
            for secondSideLoop in range(userSides):
                turtle.color(userColor)
                turtle.forward(50)
                turtle.left(360/userSides)
                

    if userSides == 9:
        nonagonShape = True
        for sideLoop in range(userSides):
            turtle.color(userColor)
            turtle.forward(100)
            turtle.left(360/userSides)
            for secondSideLoop in range(userSides):
                turtle.color(userColor)
                turtle.forward(50)
                turtle.left(360/userSides)
                

    if userSides == 10:
        decagonShape = True
        for sideLoop in range(userSides):
            turtle.color(userColor)
            turtle.forward(100)
            turtle.left(360/userSides)
            for secondSideLoop in range(userSides):
                turtle.color(userColor)
                turtle.forward(50)
                turtle.left(360/userSides)
    break
#Runs your selection and produces the right shape

if lineShape == True:
    print(" \nReally only one side?\n ")
if angleShape == True:
    print(" \nIs it really a shape?\n ")
if triangleShape == True:
    print(" \noOH a triangle!\n ")
if squareShape == True:
    print(" \nA Sqaure, classic!\n ")
if pentagonShape == True:
    print(" \nMr. President, we built it\n ")
if hexagonShape == True:
    print(" \n6 Sides is better then 1!\n ")
if heptagonShape == True:
    print(" \nWhat a funny name.. heptagon...\n ")
if octagonShape == True:
    print(" \nMy pet octagon, I mean octopus\n ")
if nonagonShape == True:
    print(" \nNonagon's, Roll Out!\n ")
if decagonShape == True:
    print(" \n10 times the fun with a decagon!\n ")
#Checks what shape and replies based on your shape
