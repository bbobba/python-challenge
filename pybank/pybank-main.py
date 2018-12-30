
# PYTHON CHALLENGE: PyBank

# -----------------------------------------------------------------
# REQUIREMENTS

# Goal:
#   Create a Python script for analyzing company financial records. See GitHub for details: https://github.com/bbobba/UTAUS201810DATA2/tree/master/03_Python/Homework/Instructions
# 
# Dataset: 
#   Company financial data stored in a csv called budget_data.csv. 
#   The dataset is composed of two columns: Date and Profit/Losses.

# Calculate:
#   The total number of months included in the dataset
#   The total net amount of "Profit/Losses" over the entire period
#   The average change in "Profit/Losses" between months over the entire period
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in losses (date and amount) over the entire period

# Deliverables:
#   Print the analysis to the terminal
#   Export a text file with the results


# -----------------------------------------------------------------
# ANALYSIS

# Import the necessary dependencies for os.path.join()
import os
import csv

# Set file path
csv_path = os.path.join('data', 'budget_data.csv')

# Declare variables
# empty lists

total_months = []
net_revenue = []
avg_change = []
max_profit_date = []
min_profit_date = []
max_profit_amount = []
min_profit_amount = []

# Open and read the csv file
with open(csv_path, newline = '') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    # Skip header
    csv_header = (csv_reader, None)

    

# METHOD 2. See 3>Activities>08-Par_Wrestling>Solved ??

# -----------------------------------------------------------------
# OUTPUT

# Print results to the terminal:
#Financial Analysis
#----------------------------
#Total Months:
#Total:
#Average Change:
#Greatest Increase in Profits:
#Greatest Decrease in Profits:

# Export results in a .txt file:
# SEE 2>Activities>09-Ins_WriteCSV

