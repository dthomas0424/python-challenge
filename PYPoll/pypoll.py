import os
import csv
#set lists
#set variables
total_votes = 0
CCS_Votes = 0
DD_Votes = 0
RAD_Votes = 0

#define CSV file location
budget_data = os.path.join("..", "Resources", "election_data.csv")
#open and read CSV file
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #read file header
    csv_header = next(csv_file)
    for row in csv_reader:
        total_votes += 1
        if row[2] == "Charles Casper Stockham":
            CCS_Votes += 1
        elif row[2] == "Diana DeGette":
            DD_Votes += 1
        elif row[2] == "Raymon Anthony Doane":
            RAD_Votes += 1
print(f'{CCS_Votes}')
print(f'{DD_Votes}')
print(f'{RAD_Votes}')
     
print("Election Results")
print()
print("---------------------------")
print()
print("total Votes:")
print()
print("---------------------------")
print()
print("Charles Casper Stockham:")
print("Diana DeGette:")
print("Anthony Doane:")
print()
print("---------------------------")
print()
print("Winner:")
print()
print("---------------------------")
