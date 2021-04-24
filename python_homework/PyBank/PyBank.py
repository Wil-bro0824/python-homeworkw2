# Import neccessary libraries
import os
import csv
from pathlib import Path

# Set the file path
csvpath = Path('budget_data.csv')

# Initialize a list of total months, total amount, and the average change
# Initialize Metric Varibles for calculation
total_months = []
net_total = []
avg_change = []
max_increase = 0
max_decrease = 0
greatest_inc = 0
greatest_dec = 0

#Open budget_data.csv as a file object
with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
#Coverting strings to ints for numerical calculations    
    for row in csvreader:
        
        total_months.append(row[0])
        net_total.append(int(row[1]))
#Calculate the average change        
    for x in range(len(net_total)-1):
        avg_change.append(net_total[x+1]-net_total[x])
#Calculate the greatest increase/decrease        
max_increase = max(avg_change)
max_decrease = min(avg_change)
        
        
greatest_inc = avg_change.index(max(avg_change)) +1
greatest_dec = avg_change.index(min(avg_change)) +1
        
    

#Print Results       
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change:{round(sum(avg_change)/len(avg_change),2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_inc]} ${str(max_increase)}")
print(f"Greatest Decrease in Profits: {total_months[greatest_dec]} $({str(max_decrease)})")

#Set output path and create a txt file
output = Path('PyBank.txt')

#Edit the txt document and input Results
with open(output, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvfile.write("Financial Analysis")
    csvfile.write("\n")
    csvfile.write("-------------------------")
    csvfile.write(f"\nTotal Months: {len(total_months)}")
    csvfile.write(f"\nTotal: ${sum(net_total)}")
    csvfile.write(f"\nAverage Change:{round(sum(avg_change)/len(avg_change),2)}")
    csvfile.write(f"\nGreatest Increase in Profits: {total_months[greatest_inc]} ${str(max_increase)}")
    csvfile.write(f"\nGreatest Decrease in Profits: {total_months[greatest_dec]} $({str(max_decrease)})")

