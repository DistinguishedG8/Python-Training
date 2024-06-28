
import csv
fileOpener = "Save_data.csv"
accessMode = "r"
with open(fileOpener, accessMode) as dataFile:
#Import function, set to read from file, sort through csv

    dataFromFile = csv.reader(dataFile, delimiter = ",")
    #Opens file as a "copy" labeled myCSVFile, instead of just the main file

    for steps in dataFromFile:
        # print(steps)
        comeTogether = ",".join(steps)
        print(comeTogether)
    #Displays the parts of a file
        # for steppie in steps:
        #     print(steppie)
        #Displays individual values
