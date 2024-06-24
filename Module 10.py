
#*Easy A*

userAnswer = "1"
answerState = False
#Declaring variables

while answerState != True:
    userAnswer = input("What is (3 x 4)? ").lower()
    userAnswer = userAnswer.replace("twelve", "12")
    #Correcting possible user input

    if userAnswer == "12":
        answerState = True
        print("You got it, nicely done!\n ")
        break
    #End of loop with the correct answer
    else:
        print("It's alright, try again\n ")
    #Repeat loop


#*Etch a Sketch*

import turtle

userLine = 1
userState = False
#Declare Variables

userStart = input("Want to sketch something? (Yes or No) ").lower()
userStart = userStart.replace("yes", "y")
#Ask if the user wants to use the program

if userStart == "y":
    userState = True
    #Checks the state of the program

    while userLine != 0:
        userLine = input("How long should the line be? (Enter 0 to end) ").lower()
        userColor = input("What color should the line be? (Black, Red, Green, Blue) ").lower()
        userAngle = input("What angle will the line be? ").lower()
        #Request user input to use the app

        userLine = int(userLine)
        userAngle = int(userAngle)
        #Correct Variable types for use
 
        turtle.color(userColor)
        turtle.right(userAngle)
        turtle.forward(userLine)
        #Sends the turtle downa guided path
        
elif userState == False:
    print(" \nOh, well we could have had fun :(\n ")

if userLine == 0:
    print(" \nThanks for playing, good bye!\n ")
