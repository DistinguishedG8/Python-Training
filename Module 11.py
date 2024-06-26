
#*Listing Hats*

hatColors = ["green", "red", "blue", "purple"]
hatPrices = [6, 3, 4, 9]
#Creating list values

if (hatColors[2]) == "blue":
    (hatPrices[2]) = 4
#Checking values and comparing (Values called using coding counting 0, 1, 2, etc.)

if (hatColors[-2]) == "blue":
    (hatPrices[-2]) = 4
#Index values can be called with negatives, starting for the end (Starts at -1)

hatColors.append("yellow")
hatPrices.append(7)
#Adds values to the end of the list

hatColors.remove("yellow")
hatPrices.remove(7)
#Removes the value (same as del)

del hatColors[2]
del hatPrices[2]
#Deletes value from the list (same as remove)

hatColors.append("yellow")
hatPrices.append(7)
hatColors.append("blue")
hatPrices.append(4)
hatColors.append("yellow")
hatPrices.append(7)
#Adds duplicate values

hatColors = ["green", "red", "blue", "purple", "yellow", "blue", "yellow"]
hatPrices = [6, 3, 4, 9, 7, 4, 7]
#Creating list values


for steps in (hatColors):
#Checks the list

    if steps == "yellow":
        hatValue = hatColors.index(steps)
        #Checks values of the steps variable to see where in the array a value matches

        hatColors.pop(hatValue)
        hatPrices.pop(hatValue)
        print(hatColors)
        print(hatPrices)
        #Removes matching values from both the HatColor and HatPrices arrays

    # elif steps != "yellow":
    #     print(hatColors)
    #     print(hatPrices)
    #     #Prints values to check the progress of the program
# hatPrices.sort()
# hatColors.sort()

# print(hatColors)
# print(hatPrices)