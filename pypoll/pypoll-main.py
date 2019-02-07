
# PYTHON CHALLENGE: PyPoll

# -----------------------------------------------------------------
# REQUIREMENTS

# Goal:
#   Create a Python script for analyzing election data. See GitHub for details: https://github.com/bbobba/UTAUS201810DATA2/tree/master/03_Python/Homework/Instructions
#   In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.) 

# Dataset: 
#   Poll data stored in a csv called election_data.csv. 
#   The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.

# Calculate:
#   The total number of votes cast
#   A complete list of candidates who received votes
#   The percentage of votes each candidate won
#   The total number of votes each candidate won
#   The winner of the election based on popular vote.

# Deliverables:
#   Print the analysis to the terminal
#   Export a text file with the results


# -----------------------------------------------------------------
# ANALYSIS
# See 3>Activities>08-Par_Wrestling>Solved

# Import the necessary dependencies for os.path.join()
import os
import csv

# Set file path
csv_path = os.path.join('data', 'election_data.csv')

# Declare variables
# empty lists


# Open and read the csv file
with open(csv_path, newline = '') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    # Skip header
    csv_header = (csv_reader, None)

# -----------------------------------------------------------------
# OUTPUT

# Print results to the terminal:


# Export results in a .txt file: