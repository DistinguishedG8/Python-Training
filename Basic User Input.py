
while True:
    user_input = input("Enter a number: ")
    #Prompts user to enter a value

    try:
        user_input = int(user_input)
        break
    #Tests if the input is a number by converting to an integer value and breaks the loop

    except ValueError:
        print("INVALID: Please enter a number! ")
        print()
    #Showcases if the input was not a number and errors

print(4 + user_input)
#Final value plus 4


#OR do this
user_input1 = input("Enter anything here: ")
user_inputs = user_input1.replace("<",".").replace(">",".").replace("?",".").replace("!",".").replace("/",".").replace("\\",".").replace("|",".").replace("=",".").replace("+",".").replace("#",".").replace("^",".").replace("$",".")
print(user_inputs)
#Validates input by removing bad characters
