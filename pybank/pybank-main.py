# Python Challenge: PyBank
# -----------------------------------------------------------------

# Import the necessary dependencies for os.path.join()
import os
import csv

# Set file path
csvpath = os.path.join('data', 'budget_data.csv')

# Declare variables


# Read in the csv file
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')