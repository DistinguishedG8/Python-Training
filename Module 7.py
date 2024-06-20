
#*Shipping options*

userAnswer = input("Would you like express shipping? ")
answer = ("Yes")
#User input and create comparative variable

if userAnswer.lower() == (answer.lower()):
#  if userAnswer != ("yes"):
#Checks if userAnswer is not equal to "yes"
    print(" \nThat will be $10 extra.")
#If statement checking for user input equal to and the reaction to a valid if statement

print(" \nHave a nice day!\n-----------\n ")
#Closing phrase


#*Banking Deposit*

depositTrue = False
#Declaring variable

userDeposit = input("How much would you like to deposit? (Enter a number) ")
depositReward = (150)
#Asking user input, setting reward variable, and converting user input

if int(userDeposit) >= depositReward:
    print(" \n-----------\nYour money has been depositted!")
    print("Congrats, you won a free toaster!\n-----------\n ")

    depositTrue = True
    #links to a true if statement (flag)

else:
    print(" \nMoney Deposit Successful!\n-----------\n ")
print("Thank you for using Western Bank and have a lovely day!\n-----------\n ")
#Checks user deposit against the reward amount

print("*-----------*\n ")


#*Car 4 Sale!*

carSelection = input("Would you like the Mustang or Challenger? ")
carWarranty = input("Would you like our 5 year warranty? (Cost: $4000) ")
#Request user input

totalCost = float(0)
warrantyCost = float(4000)
warranty = False
warrantyOption = ("Yes")
mustangSelected = ("Mustang")
challengerSelected = ("Challenger")
#Declaring values

if carWarranty.lower() == warrantyOption.lower():
     warranty = (True)
     print(" \n-----------\nYour warranty has been added!")
#Checking warranty selection and adding it to the cost

if carSelection.lower() == mustangSelected.lower():
    totalCost = (25000)
    print("Thank you for selecting the Mustang!\n-----------\n ")
#Checking user choice and adding cost to cart

if carSelection.lower() == challengerSelected.lower():
    totalCost = (30000)
    print("Thank you for selecting the Challenger!\n-----------\n ")
#Checking user choice and adding cost to cart again

if warranty == True:
    finalCost = (totalCost + warrantyCost)
else:
    finalCost = (totalCost)
#Run final calculations

print("Your total is: $" + str(finalCost) + "\nThank you for shopping at TI Dealers! \n*-----------*\n " )
#Display final cost and closing message
