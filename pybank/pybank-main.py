
#PYTHON CHALLENGE: PyBank

#INSTRUCTIONS

# Goal:
#   Create a Python script for analyzing company financial records. See GitHub for details: https://github.com/bbobba/UTAUS201810DATA2/tree/master/03_Python/Homework/Instructions
# 
# Dataset: 
#   Company financial data stored in a csv called budget_data.csv. 
#   The dataset is composed of two columns: Date and Profit/Losses.

# Calculate:
#   1. The total number of months included in the dataset
#   2. The total net amount of "Profit/Losses" over the entire period
#   3. The average change in "Profit/Losses" between months over the entire period
#   4. The greatest increase in profits (date and amount) over the entire period
#   5. The greatest decrease in losses (date and amount) over the entire period

# Deliverables:
#   Print the analysis to the terminal
#   Export a text file with the results


# -----------------------------------------------------------------
# SETUP

# Import the necessary dependencies for os.path.join()
import os
import csv

# Set file path
csv_path = os.path.join('data', 'budget_data.csv')

# Declare variables
# empty lists

total_months = 
total_revenue = 
avg_change = 
max_profit_date = 
min_profit_date = 
max_profit_amount = 
min_profit_amount = 

# Open and read the csv file
with open(csv_path, newline = '') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
#   Skip header
    #csv_header = (csv_reader, None)
    next(csv_reader)

# EXPLORATION

# ANALYSIS

# 1. The total number of months included in the dataset
# YOUR CODE HERE
# Count the number rows of data in the Date col (len)

# 2. The total net amount of "Profit/Losses" over the entire period
# YOUR CODE HERE

# 3. The average change in "Profit/Losses" between months over the entire period
# YOUR CODE HERE

# 4. The greatest increase in profits (date and amount) over the entire period
# YOUR CODE HERE

# 5. The greatest decrease in losses (date and amount) over the entire period
# YOUR CODE HERE

# -----------------------------------------------------------------
# PRESENTATION

# Print results to the terminal:
# YOUR CODE HERE

#Financial Analysis
#----------------------------
#print(f'Total Months: {str(total_months)}')
#print(f'Total: {str(total_revenue)}')
#print(f'Average Change: {str(avg_change)}')
#print(f'Greatest Increase in Profits: {str(max_profit_date)} ({str(max_profit_amount)})'
#print(f'Greatest Decrease in Profits: {str(min_profit_date)} ({str(min_profit_amount)})'

# Export results in a .txt file:
# YOUR CODE HERE
# SEE 2>Activities>09-Ins_WriteCSV

