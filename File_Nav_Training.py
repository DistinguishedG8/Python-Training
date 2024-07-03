
# -> * API-Communications * <-

# <*> Key Elements <*>
import os
import csv

# -> Testing how to locate the current file path
fileName = "test.txt"
path = os.getcwd()

# -> Simply combines text to "show" as a proper file path
file_path = os.path.join(path, fileName)

# -> Testing grounds
director = os.listdir()

# -> Sends path to console
print(path)
print(director)


# <*> CSV File Modification <*>

dataFromFile = csv.reader(director, delimiter = ",")
#Opens file as a "copy" labeled myCSVFile, instead of just the main file

for steps in dataFromFile:
    # print(steps)
    comeTogether = ",".join(steps)
    print(comeTogether)

# -> Navigates up one directory
mod_director = os.chdir('..')
path2 = os.getcwd()
print(path2)
