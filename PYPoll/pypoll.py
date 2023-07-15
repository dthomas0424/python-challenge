import os
import csv
#set lists
#set variables

#define CSV file location
budget_data = os.path.join("..", "Resources", "election_data.csv")
#open and read CSV file
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #read file header
    csv_header = next(csv_file)

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
