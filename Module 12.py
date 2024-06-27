
fileName = "Save_data.csv"

READ = "r"
WRITE = "w"
APPEND = "a"
BINARY = "b"
READWRITE = "r+"
WRITEREAD = "w+"
#File Operation modes

file = open(fileName, READWRITE)
#Opens a file named Save_Data, with read write permissions 
#(Read = r, Write = w, Append = a, binary file = b, ReadWrite = w+ or r+)

# userFirstName = input("Supply a single first name: ")
# userAge = input("Supply a single age: ")
#User input, adding a variable to the file

file.write("John, 24" + "\n")
file.write("Ronda, 28" + "\n")
# file.write(userFirstName + ", " + userAge)
#Writes words with quotes to the file

fileRead = file.read()
print(fileRead)
#Reading the current file, before writing

file.close()
print(" \nFile updated\n ")
#Always close a file if you open it