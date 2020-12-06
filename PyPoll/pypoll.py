import csv
import os

csvpath = os.path.join("Resources","election_data.csv")

# declare variables
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

# store the count of the remaining rows (total votes)
total_votes = len(csvdata)

print(total_votes)

# iterate through each row and count up the votes for each candidate
for row in csvdata:
    # if the next candidate is not currently in the list, add them and a new vote counter for them
    if row[2] not in candidates["names"]:
        candidates["names"].append(row[2])
        candidates["votes"].append(0)
    # tally the vote for the applicable candidate
    candidates["votes"][candidates["names"].index(row[2])] += 1

print(candidates)
# iterate through each candidate and store the vote percentage they received

# print results

# write results to a text file
