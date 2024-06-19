
import datetime
#Applies a date/time library

currentDate = datetime.date.today()
currentDate2 = datetime.datetime.now()
#Applies dates to this variable
#  print(currentDate)
#Displays current date and time

#  print(currentDate.year)
#  print(currentDate.month)
#  print(currentDate.day)
#Displays the different properties of the date

#  print(currentDate.strftime("%b %d %Y"))
#Testing a custom formatting
#  print(currentDate.strftime("Please attend our gathering on %b %dth %Y."))

# userInput2 = input("Enter your birthday (MM/DD/YYYY): ")
# userInput = userInput2.replace("\\","/").replace(".","/").replace("-","/").replace("_","/")
# userBirthdate = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
# #User providing birthdate, then formatting the birthdate into a float

# daysUntilBday = (currentDate - userBirthdate)
# finalBday = (365 * (currentDate.year - userBirthdate.year) - daysUntilBday.days)

# print("Only {0:.0f} days remaining!".format(finalBday))
# #Display the final result

# print(daysUntilBday)
# print(currentDate2.minute)

userDeadline2 = input("----------------\nEnter a project deadline date (mm/dd/yyyy): ")
userDeadline = userDeadline2.replace("\\","/").replace(".","/").replace("-","/").replace("_","/")
#Validated and formatted user input
print("----------------\n ")

deadline = datetime.datetime.strptime(userDeadline, "%m/%d/%Y").date()
#Modified date and time formatting

daysUntil = (deadline - currentDate)
daysUntil3 = (daysUntil / 7)
#Calculates the days and weeks
daysUntil4 = str(daysUntil3.days)
daysUntil2 = str(daysUntil.days)
#Converts daysUntil to a string

#  print(daysUntil.days)
print("Only " + daysUntil2 + " days remaining! \nThat's roughly " + daysUntil4 + " weeks!\n \n----------------")
#Displays the final values
