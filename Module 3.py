
#  print("What is your name?")
#  name = input()
#Input field for user's name

#  print(name)
#Displays the input "name" value
#  print("----------")

#  print("What name would you like?")
#  name2 = input()
#  print(name2)
#Testing overriding user input for a variable

#  name2 = ("John")
#  print(name2)
#Replacement for variable name2


#*Story Time!*

print("----------")

firstName1 = input("What is your first name? ")
lastName1 = input("What is your last name? ")
#Acquires details from the writer

firstName = firstName1.replace("<",".").replace(">",".").replace("?",".").replace("!",".").replace("/",".").replace("\\",".").replace("|",".").replace("=",".").replace("+",".").replace("#",".").replace("^",".").replace("$",".")
lastName = lastName1.replace("<",".").replace(">",".").replace("?",".").replace("!",".").replace("/",".").replace("\\",".").replace("|",".").replace("=",".").replace("+",".").replace("#",".").replace("^",".").replace("$",".")
#Validates user input does not contain bad characters

print(" \n----------")
print("Hi there! " + firstName.capitalize() + " " + lastName.capitalize())
#Combines user input into a display statement
print("----------")

print("Lets write a story!")
description1 = input("Pick a descriptive word: ")
animal1 = input("Name an animal: ")
action1 = input("Pick an action word: ")
adverb1 = input("Pick an adverb: ")
#User can input values to build out the story

description = description1.replace("<",".").replace(">",".").replace("?",".").replace("!",".").replace("/",".").replace("\\",".").replace("|",".").replace("=",".").replace("+",".").replace("#",".").replace("^",".").replace("$",".")
animal = animal1.replace("<",".").replace(">",".").replace("?",".").replace("!",".").replace("/",".").replace("\\",".").replace("|",".").replace("=",".").replace("+",".").replace("#",".").replace("^",".").replace("$",".")
action = action1.replace("<",".").replace(">",".").replace("?",".").replace("!",".").replace("/",".").replace("\\",".").replace("|",".").replace("=",".").replace("+",".").replace("#",".").replace("^",".").replace("$",".")
adverb = adverb1.replace("<",".").replace(">",".").replace("?",".").replace("!",".").replace("/",".").replace("\\",".").replace("|",".").replace("=",".").replace("+",".").replace("#",".").replace("^",".").replace("$",".")
#Validates user input on story text
print(" \n----------")

print("The Tale of the " + description.capitalize() + " " + animal.capitalize() + "\n  Written by " + firstName.capitalize() + " " + lastName.capitalize())
#The story is played and the use is heled responsible for their writting
print(" ")

print("Long ago, in the dark void of space")
print("a " + description.lower() + " " + animal.lower() + " came into existance.")
print("Brimming with new life, the " + animal.lower() + " " + action.lower() + ' up as if to say "Hello Universe this is me!"' + "\nThen out of nowhere a space ship " + adverb.lower() + " the " + animal.lower())
print("and that was the short but insightful tale of the " + description.lower() + " " + animal.lower() + ".")
print(" -The end!")
#This section writes out the story including the user written elements for dramatic effect, adjusts user imput to lowercase
print(" \n----------")
