import os
import csv

# CSV file import from file path
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_p_l = 0
value = 0
change = 0
#need to find dates
dates = []
#need to find profits
profits = []
#defining output for text file along with name of txt file
file_to_output = "budget_analized.txt"

#Opening and reading the file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

  
    csv_header = next(csvreader)

    
    first_row = next(csvreader)
    total_months += 1
    total_p_l += int(first_row[1])
    value = int(first_row[1])
    
   
    for row in csvreader:
       
        dates.append(row[0])
        
        # Calculating the change
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_p_l = total_p_l + int(row[1])

    #Calculation for increase in profits, focusing on max value and ate
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    #Finding date when there was a greatest increase to show on output
    greatest_date = dates[greatest_index]

    #Calcuation for decrease in profits, focusing on min value and date 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    #Finding date when there was a greatest decrease to show on output
    worst_date = dates[worst_index]

    #Calcuation for average change
    
    avg_change = sum(profits)/len(profits)
    

#Show on terminal 

output=( 
f"\n Financial Analysis\n"
f"---------------------\n"
f"Total Months: {str(total_months)}\n"
f"Total: ${str(total_p_l)}\n"
f"Average Change: ${str(round(avg_change,2))}\n"
f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)}\n"
f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})\n")

# show output

print(output)

# produce  .txt file

with open(file_to_output,"w")as txt_file:
    txt_file.write(output)

