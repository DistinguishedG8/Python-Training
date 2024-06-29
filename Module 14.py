
#*Functions*


#Main function, runs secondary functions
def main(userName):
    cleaned_up = sanitized(userName)
    printHello(cleaned_up)
    return

#Creates very simple function
def printHello(p_userName):
    print("Hello there! " + p_userName + "\nThank you, for all of your help!")
    return

#Function to sanitize user input
def sanitized(user_input):
    cleaned_input = user_input.replace(",","").replace(".","").replace("<","").replace(">","").replace("?","").replace("!","").replace("/","").replace("\\","").replace("|","").replace("=","").replace("+","").replace("#","").replace("^","").replace("$","")
    return cleaned_input

#Calls functions
main(input("What is your name? "))
