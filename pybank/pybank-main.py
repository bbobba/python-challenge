
# PYTHON CHALLENGE: PyBank


# -----------------------------------------------------------------
# INSTRUCTIONS

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
csvpath = os.path.join('data', 'budget_data.csv')

# Declare variables


# Read in the csv file
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #skip header


# -----------------------------------------------------------------
# OUTPUT

# Print results to the terminal:

#Financial Analysis
#----------------------------
#Total Months:
#Total:
#Average  Change:
#Greatest Increase in Profits:
#Greatest Decrease in Profits:

# Export results in a .txt file:

