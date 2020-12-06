# Dependencies
import csv
import os

# declare variables
csvpath = os.path.join("Resources", "budget_data.csv")
sum_profits = 0
total_profit_loss = 0
max_profit = {
    "month": "placeholder",
    "value": 0
}
max_loss = {
    "month": "placeholder",
    "value": 0
}

# check if the new row has a greater profit. If so, set new max profit pairing
# if the new row has a greater loss, set new max loss pairing
def checkGreatest(current, previous_value):
    profit_loss = current[1] - previous_value
    if profit_loss > max_profit["value"]:
        max_profit["month"] = current[0]
        max_profit["value"] = profit_loss
    elif profit_loss < max_loss["value"]:
        max_loss["month"] = current[0]
        max_loss["value"] = profit_loss

# default value for checking first data row since previous row is headers and not captured in csvdata
# every subsequent row, store previous row's data
def getPreviousRowValue(i):
    if i != 0:
        return csvdata[i-1][1]
    else:
        return 0

# convert to string and make sure the negative values are properly formatted
def toFormattedString(value):
    if value < 0:
        return "-$" + str(abs(value))
    else:
        return "$" + str(value)

# open CSV, read it, store headers, store the rest of the data, then close the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    csvdata = list(csvreader)

# store the count of the remaining rows (total months)
month_count = len(csvdata)
    
# for each row: check if the row has the greatest profit or loss, add the profit value to the total profits
for i in range(len(csvdata)):
    current_row = csvdata[i]
    current_row[1] = int(current_row[1]) # convert the value string to an int
    checkGreatest(current_row, getPreviousRowValue(i))
    sum_profits += current_row[1]

# get the total profit/loss and calculate the average per month
total_profit_loss = csvdata[-1][1] - csvdata[0][1]
average_delta = round(total_profit_loss / (month_count-1), 2) # calculate average delta

# print results
title = "Financial Analysis"
print(title)
print("-" * len(title))
print("Total months: " + str(month_count))
print("Total Profit/Loss: " + toFormattedString(sum_profits))
print("Average Profit/Loss shift per Month: " + toFormattedString(average_delta))
print("Greatest Profit shift: " + max_profit['month'] + " with " + toFormattedString(max_profit['value']))
print("Greatest Loss shift: " + max_loss['month'] + " with " + toFormattedString(max_loss['value']))

# write results to a text file
with open("financial-analysis.txt", "w") as textoutput:
    textoutput.writelines([
        title,
        "\n"+("-" * len(title)),
        "\nTotal months: " + str(month_count),
        "\nTotal Profit/Loss: " + toFormattedString(average_delta),
        "\nAverage Profit/Loss shift per Month: " + toFormattedString(average_delta),
        "\nGreatest Profit shift: " + max_profit['month'] + " with " + toFormattedString(max_profit['value']),
        "\nGreatest Loss shift: " + max_loss['month'] + " with " + toFormattedString(max_loss['value'])
    ])