# Python Challenge: PyBank
# -----------------------------------------------------------------

# Import the necessary dependencies for os.path.join()
import os
import csv

# Set file path
# SYNTAX: csvpath = os.path.join('folder', 'filename.csv') 
budget_data = os.path.join('data', 'budget_data.csv')

# Read in the csv file
# SYNTAX:
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    # csvreader specifies the delimiter and the variable that holds the contents