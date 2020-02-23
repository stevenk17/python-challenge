import os
import csv

#CSV file import form file path
election_data = os.path.join("election_data.csv")

#Variables
total_votes = 0
candidates = []
percent_votes = []
num_votes = []


with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Calculating percentages, equation, rounding percentages due to orginal output showing many decimal places 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percent_votes.append(percentage)
    
    # Determining the winning candidate 
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Show on terminal

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to .txt file
output = open("election_results.txt", "w")

line1 = "Election Results\n"

line2 = "--------------------------\n"

line3 = str(f"Total Votes: {str(total_votes)}\n")

line4 = str("--------------------------\n")

output.write(line1)
output.write(line2)
output.write(line3)
output.write(line4)

for i in range(len(candidates)):
    line5 = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})\n")
    output.write(line5)

line6 = "--------------------------\n"

line7 = str(f"Winner: {winning_candidate}\n")

line8 = "--------------------------\n"

output.write(line6)
output.write(line7)
output.write(line8)

