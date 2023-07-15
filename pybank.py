import os
import csv

month_count = 0

budget_data = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)


    for row in csv_reader:

        month_count += 1



print("Financial Analysis")
print()
print('--------------------------------------')
print()
print(f'Total Months: {month_count}')

