# Dependencies
import os
import csv

# declare variables
csvpath = os.path.join("Resources", "employee_data.csv")

# open CSV, read it, store headers, store the rest of the data, then close the file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    csvdata = list(csvreader)

# split the Name column into two different columns

# rewrite the DOB column to the proper format

# rewrite the SSN column to the proper format

# change the State column to an abbreviation -- use dictionary

# export results to a new csv