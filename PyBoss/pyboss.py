# dependencies
import os
import csv

# variables
csvpath = os.path.join("Resources", "employee_data.csv")
emp_list = [["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]]

# functions
# split the name into first and last and append both to the new employee list
def splitName(i, name):
    emp_list[i+1].append(name.split(" ")[0]) # split the Name column into two different columns
    emp_list[i+1].append(name.split(" ")[1])

# split the DOB into year, month, and day, reorder them, then rejoin them with "/"
def formatDOB(i, dob):
    dob_list = dob.split("-")
    dob_list.append(dob_list[0]) # add year to the end of the list...
    dob_list.pop(0) # ... then remove it
    emp_list[i+1].append("/".join(dob_list))

# open CSV, read it, store headers, store the rest of the data, then close the file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    csvdata = list(csvreader)

for i in range(len(csvdata)):
    emp_list.append([]) # add new list(row) to the new employee list
    emp_list[i+1].append(csvdata[i][0]) # store the Emp ID unchanged
    splitName(i, csvdata[i][1]) # split the Name column into two different columns
    formatDOB(i, csvdata[i][2]) # rewrite the DOB column to the proper format
    print(emp_list[i+1])

# rewrite the SSN column to the proper format

# change the State column to an abbreviation -- use dictionary

# export results to a new csv