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
highestchange_PL = 0
lowestchange_PL = 0
highestchangeindex = 0
lowestchangeindex = 0
highestmonthindex = 0
lowestmonthindex = 0
highest_month = ""
lowest_month = ""
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
    #sum the total of changes in the list for averaging        
    PL_sum = sum(change_list)
    #calculate average change 
    average_PL = round(PL_sum/(month_count -1), 2)
    #set the maximun and minumum values from the change list
    highestchange_PL = max(change_list)
    lowestchange_PL = min(change_list)
    #locate the Index values for the highest and lowest values
    highestchangeindex = change_list.index(highestchange_PL)
    lowestchangeindex = change_list.index(lowestchange_PL)
    #locate the index of the highest and lowest month
      #highestmonthindex = month_list.index(highestchange_PL)
      #lowestmonthindex = month_list.index(lowestchange_PL)
    highest_month = month_list[highestchangeindex]
    lowest_month = month_list[lowestchangeindex]


#print(average_PL)
#print(highest_month)
#print(lowest_month)
#print(highestchange_PL)
#print(lowestchange_PL)

print("Financial Analysis")
print()
print('--------------------------------------')
print()
print(f'Total Months: {month_count}')
print(f'Total: {total_PL}')
print(f'Average Change: {average_PL}')
print(f'Greatest Increase in Profits: {highest_month} {highestchange_PL}')
print(f'Greatest Decrease in Profits: {lowest_month} {lowestchange_PL}')

#create and export a file with the printed results
budget_data_file = os.path.join("budget_data.txt")
with open(budget_data_file, "w") as budget_data_output:
    budget_data_output.write("Financial Analysis\n")
    budget_data_output.write('\n')
    budget_data_output.write('--------------------------------------\n')
    budget_data_output.write('\n')
    budget_data_output.write(f'Total Months: {month_count}\n')
    budget_data_output.write(f'Total: {total_PL}\n')
    budget_data_output.write(f'Average Change: {average_PL}\n')
    budget_data_output.write(f'Greatest Increase in Profits: {highest_month} {highestchange_PL}\n')
    budget_data_output.write(f'Greatest Decrease in Profits: {lowest_month} {lowestchange_PL}\n')

    



