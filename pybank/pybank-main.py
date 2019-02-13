# SETUP:
# Import the necessary dependencies for os.path.join()
import os
import csv

# Set csv path for data file and store in a variable
csv_path = os.path.join('data','budget_data.csv')

# Set txt path for output file and store in a variable
output_file = os.path.join('budget_analysis.txt')


# ANALYSIS:
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

# 1. The total number of months included in the dataset
total_months = len(dates)        

# Test print
# print(f'Total Months: {total_months}')


# 2. The total net amount of "Profit/Losses" over the entire period
net_profit = sum(profit_loss)

# Test print
# print(f'Total: ${net_profit}')


# 3. The average change in "Profit/Losses" between months over the entire period
for i in range(1, len(profit_loss)):
    change.append(profit_loss[i] - profit_loss[i-1])

average_change = round(sum(change)/len(change),2)
    
# Test print
# print(f'Average Change: ${average_change}')


# 4. The greatest increase in profits (date and amount) over the entire period
max_change = max(change)
max_index = change.index(max_change)
max_date = dates[max_index + 1]

# Test print
# print(f'Greatest Increase in Profits: {max_date} (${max_change})')


# 5. The greatest decrease in losses (date and amount) over the entire period
min_change = min(change)
min_index = change.index(min_change)
min_date = dates[min_index + 1]

# Test print
# print(f'Greatest Decrease in Profits: {min_date} (${min_change})')


# OUTPUT:
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