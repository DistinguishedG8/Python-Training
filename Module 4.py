
#  age = 42
#  print(age)
#Age value is stored as a number because of no "quotations"

#  width = 20
#  height = 5
#Displays values for each side

#  addition = (width + height)
#Adds values
#  subtraction = (width - height)
#Subtracts values
#  multiply = (width * height)
#Multiplies values
#  divide = (width / height)
#Divides values
#  exponent = (width ** height)
#To the power of...
#  modulo = (width % height)
#Modulates values

#  area = (width * height)
#  perimeter = 2 * (width + height)
#sets variables to formulas

#  area2 = ("%.0f" % area)
#  perimeter2 = ("%.0f" % perimeter)
#Converting float types to string (%.0f is needed to add area which is a float into a string)

#  print("Here are the Area and Perimeter: " + area2 + \
#        " and " + perimeter2)
#Displays the formula calculations for area and perimeter ( backslash \ is used after a string to move the code to another line) 

#  print("Does it work for Area {0:.0f} and Perimeter {1:.0f}?".format(area, perimeter))
#Display using the format option

#  salary = input("Please enter your salary: ")
#  bonus = input("Please enter your bonus: ")
#Obtain user data for salary and bonus

#  salary = (salary.replace(",","").replace("$",""))
#  bonus = (bonus.replace(",","").replace("$",""))
#Removes commas and validates user input

#  payCheckAmount = (float(salary) + float(bonus))
#  print("Annual Paycheck: ${0:.0f}".format(payCheckAmount))
#Displays the paycheck amount, which is combining salary and bonus pay


#*Loan Calculator 9000*

print(" \n------------- \nWelcome to LastNet loan calculator! \nWe calculate loans free for all, \nlets get started! \n-------------\n ")
#Introductory text

loanAmount = 0
interestRate = 0
loanLength = 0
paymentNumber = 0
monthlyPayment = 0
#Declare values

loanAmount2 = input("Enter total loan amount: ")
interestRate2 = input("Enter the interest rate percentage: ")
loanLength2 = input("Enter how many years will the loan last: ")
#Request user to enter values

loanAmount2 = (loanAmount2.replace(",","").replace(".","").replace("$","").replace("%",""))
interestRate2 = (interestRate2.replace(",","").replace(".","").replace("$","").replace("%",""))
loanLength2 = (loanLength2.replace(",","").replace(".","").replace("$","").replace("%",""))
#Sanatizes the amounts/input

loanAmount = float(loanAmount2)
interestRate = float(interestRate2)
loanLength = float(loanLength2)
interestRate = (interestRate / 100)
#Converts numbers from string to a float

paymentNumber = (loanLength * 12)
monthlyPayment = (loanAmount * (interestRate * (1 + interestRate) * paymentNumber) / ((1 + interestRate) * (paymentNumber - 1)))
#Calculates the loan

print(" \n-------------")
print("Your monthly payment is: ${0:.0f}".format(monthlyPayment) + "\nCongrats on your new loan!")
print("-------------\n ")
#Showcases the end resualt