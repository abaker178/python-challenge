import csv
import os

csvpath = os.path.join("Resources","election_data.csv")

# declare variables
total_votes = 0
candidates = {
        "names": [],
        "votes": [],
        "percent": []
    }

# open CSV, read it, store headers, store the rest of the data, then close the file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    csvdata = list(csvreader)
    
# print(csvdata) DO NOT RUN THIS CODE
# store the count of the remaining rows (total votes)

# iterate through each row and count up the votes for each candidate

# iterate through each candidate and store the vote percentage they received

# print results

# write results to a text file
