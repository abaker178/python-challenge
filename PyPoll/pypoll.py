import csv
import os

csvpath = os.path.join("Resources","election_data.csv")

# declare variables
candidates = {
        "names": [],
        "votes": [],
        "percent": []
    }

# compare each vote count to see who wins
# return winner text
def getWinner(c):
    curr_winner_votes = 0
    for i in range(len(c["votes"])):
        if c["votes"][i] > curr_winner_votes:
            curr_winner = c["names"][i]
            curr_winner_votes = c["votes"][i]
            tie = False
        elif c["votes"][i] == curr_winner_votes:
            curr_winner += (" and " + c["names"][i])
            tie = True
    
    # check if there is a tie
    if tie is True:
        return "We have a tie between " + curr_winner
    else:
        return "Winner: " + curr_winner

# open CSV, read it, store headers, store the rest of the data, then close the file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    csvdata = list(csvreader)

# store the count of the remaining rows (total votes)
total_votes = len(csvdata)

# iterate through each row and count up the votes for each candidate
for row in csvdata:
    # if the next candidate is not currently in the list, add them and a new vote counter for them
    if row[2] not in candidates["names"]:
        candidates["names"].append(row[2])
        candidates["votes"].append(0)
    # tally the vote for the applicable candidate
    candidates["votes"][candidates["names"].index(row[2])] += 1

# iterate through each candidate and store the vote percentage they received rounded with proper formatting
for i in range(len(candidates["names"])):
    temp_percent = (candidates["votes"][i] / total_votes) * 100
    temp_rounded_percent = round(temp_percent, 3)
    candidates["percent"].append(str(temp_rounded_percent) + "%")

# print results
title = "Election Results"
divider = "-" * len(title)
winner = getWinner(candidates)
print(title)
print(divider)
print(f'Total Votes: {total_votes}')
print(divider)
# print each candidate as "Name: Percent (Votes)"
for i in range(len(candidates["names"])):
    print(f'{candidates["names"][i]}: {candidates["percent"][i]} ({candidates["votes"][i]})')
print(divider)
print(winner)
print(divider)

# write results to a text file
with open("poll_results.txt", "w") as textoutput:
    textoutput.writelines([
        title,
        "\n" + divider,
        "\n" + "Total Votes: " + str(total_votes),
        "\n" + divider
    ])
    # print each candidate as "Name: Percent (Votes)"
    for i in range(len(candidates["names"])):
        textoutput.writelines([
            "\n" + candidates["names"][i] + ": ",
            str(candidates["percent"][i]) + " ",
            "(" + str(candidates["votes"][i]) + ")"
        ])
    textoutput.writelines([
        "\n" + divider,
        "\n" + winner,
        "\n" + divider
    ])