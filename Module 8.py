
#*Country Questionare*

userCountry = input("What country are you from? ").lower()
userCountry = userCountry.replace("canada","ca").replace("america","us").replace("france","fr").replace("germany","de").replace("united states","us").replace("usa","us").replace("united states of america","us")
#Request user location and replace variables

countryID = False
#Country Variable Declared

if userCountry.lower() == "ca":
    countryID = True
    print("Oh soory, goood day!")
if userCountry.lower() == "us":
    countryID = True
    print("Good morning sunshine!")
if userCountry.lower() == "fr":
    countryID = True
    print("Bonjour!")
if userCountry.lower() == "de":
    countryID = True
    print("Guten Tag!")
elif countryID == False:
    print("Your not from around these parts are you?")
#Identifies the country entered by the user and displays a hello message


#*Coffee Machine*

userCoffee = input("Do you have coffee (Yes or No)? ").lower()
#Accepting user input and replacing values

print(" \n------------")

if userCoffee =="yes":
    creamCoffee = input("Would you like cream or sugar? ").lower()
    #Requesting additional user input and replacing values

    if userCoffee == "yes" and creamCoffee == "cream":
        print("That'll be $7\nEnjoy your coffee with cream!")
        #Checking if user asked for cream

    if userCoffee == "yes" and creamCoffee != "cream":
        print("That'll be $6\nEnjoy your coffee with sugar!")
        #Checking if user did not ask for cream

print(" \n------------\nHave a lovely day!")
#Final closing remarks
