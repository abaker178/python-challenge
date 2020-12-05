import csv

csvpath = "Resources/budget_data.csv"

# declare variables
sum_profits = 0
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
def checkMax(r):
    if r[1] > max_profit["value"]:
        max_profit["month"] = r[0]
        max_profit["value"] = r[1]
    elif r[1] < max_loss["value"]:
        max_loss["month"] = r[0]
        max_loss["value"] = r[1]


# open CSV, read it, get headers
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    
    # store the count of the remaining rows (total months)
    month_count = len(list(csvreader))

    # check each row to see if its profit/loss is greater than the current greatest profit or loss
    for row in csvreader:
        checkMax(row)
        sum_profits += row[1] # add the current row's value to the sum_profits counter

    average = sum_profits / month_count
    print(f"Total months: {month_count}")
    print(f"Total Profit/Loss: {sum_profits}")
    print(f"Average Profit/Loss per Month: {average}")
    print(f"Greatest Profit: {max_profit['month']} with ${max_profit['value']}")
    print(f"Greatest Loss: {max_loss['month']} with -${abs(max_loss['value'])}")