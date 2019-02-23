
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


# # -----------------------------------------------------------------
# # ANALYSIS

# Import the necessary dependencies for os.path.join()
import os
import csv

# Set csv path for data file and store in a variable
csv_path = os.path.join('data','election_data.csv')

# Set txt path for output file and store in a variable
output_file = os.path.join('election_analysis.txt')

# Create empty lists
candidate_name = []
unique_candidates = []
candidate_votes = []
candidate_percentage = []

# Counter
total_votes = 0

# Open and read the csv file
with open(csv_path, newline='') as csv_file:

     # Store contents in a variable called csv_reader
    csv_reader = csv.reader(csv_file, delimiter=',') 

    # Read header
    header = next(csv_reader)

    # Iterate through the rows
    for row in csv_reader:
        
        # Append candidate names to new list
        candidate_name.append(row[2])
        
        # Tally votes
        total_votes = total_votes + 1

# Find unique candidates who recieved votes and store in a list
for candidate in candidate_name:
    if candidate not in unique_candidates:
        unique_candidates.append(candidate)



# # -----------------------------------------------------------------
# # OUTPUT
with open(output_file,'w') as txt_file:
    
    # Print election summary to the terminal
    election_summary = (f'\n\
    Election Results\n\
    ----------------------------\n\
    Total Votes: {total_votes}\n\
    ----------------------------')
    print(election_summary)
    
    # Save election summary in the text file
    txt_file.write(election_summary)
    
    # Calculate the percentage of votes and total number of votes each candidate won
    for i in range(0, len(unique_candidates)):
        candidate_votes.append(candidate_name.count(unique_candidates[i]))
        candidate_percentage.append(candidate_name.count(unique_candidates[i]) / total_votes * 100)
        candidate_summary = f'{unique_candidates[i]}: {candidate_percentage[i]:0.3f}% ({candidate_votes[i]})\n'
        
        # Print candidate summary to the terminal
        print(candidate_summary, end='')
        
        # Save candidate summary in the text file
        txt_file.write(candidate_summary)

    # Find the winner of the election based on popular vote
    winner_votes = max(candidate_votes)
    winner_index = candidate_votes.index(winner_votes)
    winner_name = unique_candidates[winner_index]

    # Print winner summary to the terminal
    winner_summary = (f'\n\
    ----------------------------\n\
    Winner: {winner_name}\n\
    ----------------------------')
    print(winner_summary)
    
    # Save winner summary in the text file
    txt_file.write(winner_summary)


    