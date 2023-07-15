import os
import csv
#set lists
#set variables
total_votes = 0
CCS_Votes = 0
DD_Votes = 0
RAD_Votes = 0
CCS_percent = 0
DD_percent = 0
RAD_percent = 0

#define CSV file location
budget_data = os.path.join("..", "Resources", "election_data.csv")
#open and read CSV file
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #read file header
    csv_header = next(csv_file)
    #loop through file and extract data
    for row in csv_reader:
        #add up total number of votes
        total_votes += 1
        #add up votes for CCS
        if row[2] == "Charles Casper Stockham":
            CCS_Votes += 1
        #add up votes for DD    
        elif row[2] == "Diana DeGette":
            DD_Votes += 1
        #add up votes for RAD    
        elif row[2] == "Raymon Anthony Doane":
            RAD_Votes += 1
#calculate percentage of votes for each candidate            
CCS_percent = round(((CCS_Votes/total_votes) *100), 3)
DD_percent = round(((DD_Votes/total_votes) *100), 3)
RAD_percent = round(((RAD_Votes/total_votes) *100), 3)

print(f'{CCS_percent}%')
print(f'{DD_percent}%')
print(f'{RAD_percent}%')

     
print("Election Results")
print()
print("---------------------------")
print()
print(f"total Votes: {total_votes}")
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
