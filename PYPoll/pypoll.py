import os
import csv
#set variables
total_votes = 0
CCS_Votes = 0
DD_Votes = 0
RAD_Votes = 0
CCS_percent = 0
DD_percent = 0
RAD_percent = 0
CCS_name = ""
DD_name = ""
RAD_name = ""
winner_name = ""
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
            CCS_name = "Charles Casper Stockham"
        #add up votes for DD    
        elif row[2] == "Diana DeGette":
            DD_Votes += 1
            DD_name = "Diana DeGette"
        #add up votes for RAD    
        elif row[2] == "Raymon Anthony Doane":
            RAD_Votes += 1
            RAD_name = "Raymon Anthony Doane"
#calculate percentage of votes for each candidate            
CCS_percent = round(((CCS_Votes/total_votes) *100), 3)
DD_percent = round(((DD_Votes/total_votes) *100), 3)
RAD_percent = round(((RAD_Votes/total_votes) *100), 3)
#set winner_name to the candidate with the most votes
if (CCS_Votes) > (DD_Votes) and (CCS_Votes) > (RAD_Votes):
    winner_name = (CCS_name)
elif (DD_Votes) > (CCS_Votes) and (DD_Votes) > (RAD_Votes):
    winner_name = (DD_name)
elif (RAD_Votes) > (DD_Votes) and (RAD_Votes) > (CCS_Votes):
    winner_name = (RAD_name)
#print the results         
print("Election Results")
print()
print("---------------------------")
print()
print(f"total Votes: {total_votes}")
print()
print("---------------------------")
print()
print(f"Charles Casper Stockham: {CCS_percent}% {CCS_Votes}")
print(f"Diana DeGette: {DD_percent}% {DD_Votes}")
print(f"Anthony Doane: {RAD_percent}% {RAD_Votes}")
print()
print("---------------------------")
print()
print(f"Winner: {winner_name}")
print()
print("---------------------------")
#write the results to a file
election_data_file = os.path.join("election_data.txt")
with open(election_data_file, "w") as election_data_output:
    election_data_output.write("Election Results\n")
    election_data_output.write("\n")
    election_data_output.write("---------------------------\n")
    election_data_output.write("\n")
    election_data_output.write(f"total Votes: {total_votes}\n")
    election_data_output.write("\n")
    election_data_output.write("---------------------------\n")
    election_data_output.write("\n")
    election_data_output.write(f"Charles Casper Stockham: {CCS_percent}% {CCS_Votes}\n")
    election_data_output.write(f"Diana DeGette: {DD_percent}% {DD_Votes}\n")
    election_data_output.write(f"Anthony Doane: {RAD_percent}% {RAD_Votes}\n")
    election_data_output.write("\n")
    election_data_output.write("---------------------------\n")
    election_data_output.write("\n")
    election_data_output.write(f"Winner: {winner_name}\n")
    election_data_output.write("\n")
    election_data_output.write("---------------------------")
