import csv

csvpath = "Resources/budget_data.csv"

# declare variables
sum_profits = 0
total_profit_loss = 0
max_profit = {
    "month": "Jan-1900",
    "value": 0
}
max_loss = {
    "month": "Jan-1900",
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
print(f"Total months: {month_count}")
print(f"Total Profit/Loss: ${sum_profits}")
print(f"Average Profit/Loss change per Month: ${average_delta}")
print(f"Greatest Profit: {max_profit['month']} with ${max_profit['value']}")
print(f"Greatest Loss: {max_loss['month']} with -${abs(max_loss['value'])}")