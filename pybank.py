import os
import csv
#set variables
month_count = 0
month_PL = 0
total_PL = 0
#define CSV file location
budget_data = os.path.join("..", "Resources", "budget_data.csv")
#open and read CSV file
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #read file header
    csv_header = next(csv_file)

    #loop through file to extract data
    for row in csv_reader:
        #add up months in file
        month_count += 1
        #add profit loss values from file
        month_PL = int(row[1])
        total_PL += month_PL






print("Financial Analysis")
print()
print('--------------------------------------')
print()
print(f'Total Months: {month_count}')
print(f'Total: {total_PL}')

