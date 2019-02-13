# PYTHON CHALLENGE: PyBank

# -----------------------------------------------------------------
# OVERVIEW: Python script that analyzes a set of company financial records.
#
# DATASET: Company financial data stored in a csv called budget_data.csv.
#
# DELIVERABLE: Python script that...
#   1. Calculates:
#      - The total number of months included in the dataset
#      - The total net amount of "Profit/Losses" over the entire period
#      - The average change in "Profit/Losses" between months over the entire period
#      - The greatest increase in profits (date and amount) over the entire period
#      - The greatest decrease in losses (date and amount) over the entire period
#   2. Prints analysis to the terminal
#   3. Exports results in a text file

# ASSUMPTIONS:
#   The dataset is complete and clean (i.e. no nulls, missing values or duplicate records)
#   The data is sorted chronologically by month ('date')
#   Financial figures are in USD ('profit/loss')

# DOCUMENTATION:
#   csv_path = csv file path for data set (update this path if the name and/or location of the data set changes)
#   output_file = text file path for final analysis (update this path according to the desired name and location of the new text file)
#   total_months = the total number of months included in the dataset
#   net_profit = the total net amount of "Profit/Losses" over the entire period
#   average_change = the average change in "Profit/Losses" between months over the entire period
#   max_change = the greatest increase in profits (dollar amount) over the entire period
#   max_date = the month in which the greatest increase in profits occured over the entire period
#   min_change = the greatest decrease in losses (dollar amount) over the entire period
#   min_date = the month in which the greatest decrease in losses occured over the entire period
#   budget_summary = summary of results to be printed to the terminal and exported in a text file


# -----------------------------------------------------------------
# ANALYSIS

# Import the necessary dependencies for os.path.join()
import os
import csv

# Set csv path for data file and store in a variable
csv_path = os.path.join('data','budget_data.csv')

# Set txt path for output file and store in a variable
output_file = os.path.join('budget_analysis.txt')

# Create empty lists
dates = []
profit_loss = []
change = []
 
# Open and read the csv file
with open(csv_path, newline='') as csv_file:

     # Store contents in a variable called csv_reader
    csv_reader = csv.reader(csv_file, delimiter=',') 

    # Skip header
    next(csv_reader)

    # Iterate through the rows
    for row in csv_reader: 

        # Append
        dates.append(row[0])
        profit_loss.append(int(row[1]))

# Calculate the total number of months included in the dataset; use the len() function to return the number of items in the dates list
total_months = len(dates)        


# Calculate the total net amount of "Profit/Losses" over the entire period
net_profit = sum(profit_loss)


# Calculate the average change in "Profit/Losses" between months over the entire period
for i in range(1, len(profit_loss)):
    change.append(profit_loss[i] - profit_loss[i-1])

average_change = round(sum(change)/len(change),2)
    

# Calculate the greatest increase in profits (date and amount) over the entire period
max_change = max(change)
max_index = change.index(max_change)
max_date = dates[max_index + 1]


# Calculate the greatest decrease in losses (date and amount) over the entire period
min_change = min(change)
min_index = change.index(min_change)
min_date = dates[min_index + 1]


# Summarize the results and store in a variable called budget_summary
budget_summary = (f'\n\
    Financial Analysis\n\
    ----------------------------\n\
    Total Months: {total_months}\n\
    Total: ${net_profit}\n\
    Average Change: ${average_change}\n\
    Greatest Increase in Profits: {max_date} (${max_change})\n\
    Greatest Decrease in Profits: {min_date} (${min_change})')

# Print the analysis to the terminal
print(budget_summary)

# Export the analysis in a text file
with open(output_file,'w') as txt_file:
    txt_file.write(budget_summary)