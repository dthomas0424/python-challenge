import os
import csv
#set lists
month_list = []
change_list = []
#set variables
month_count = 0
month_PL = 0
total_PL = 0
previousmonth_PL = 0
change_PL = 0
PL_sum = 0
average_PL = 0
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
        #set initial profit loss for getting changes
        if (month_count == 1):
            previousmonth_PL = month_PL
        #calculate remaining profit loss and add to a list for adding up    
        else:
            change_PL = month_PL - previousmonth_PL
            month_list.append(row[0])
            change_list.append(change_PL)
            previousmonth_PL = month_PL
    PL_sum = sum(change_list)
    average_PL = round(PL_sum/(month_count -1), 2)

#print(average_PL)



print("Financial Analysis")
print()
print('--------------------------------------')
print()
print(f'Total Months: {month_count}')
print(f'Total: {total_PL}')
print(f'Average Change: {average_PL}')

