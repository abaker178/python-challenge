# dependencies
import os
import csv
from us_state_abbrev import us_state_abbrev as usa
    # **source: https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
    
# variables
csvpath = os.path.join("PyBoss", "Resources", "employee_data.csv") # initial csv file's path
emp_list = [["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]] # headers in a nested list

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

# split the SSN, take the last segment, tack it onto "***-**-", and add it to the new employee list
def formatSSN(i, ssn):
    ssn_list = ssn.split("-")
    emp_list[i+1].append("***-**-" + ssn_list[-1])

def formatState(i, state):
    emp_list[i+1].append(usa[state])

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
    formatSSN(i, csvdata[i][3]) # rewrite the SSN column to the proper format
    formatState(i, csvdata[i][4]) # change the State column to an abbreviation -- use dictionary
    # print(emp_list[i+1])

# export results to a new csv
with open(os.path.join("PyBoss", "employee_data_new.csv"), "w", newline="") as csvoutput:
    csvwriter = csv.writer(csvoutput, delimiter=',')
    for row in emp_list:
        csvwriter.writerow(row)