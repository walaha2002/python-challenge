# Import Libraries Generate and Read CSV file
import os
import csv

# Create Path to CSV file
csvpath = os.path.join( 'Resources','budget_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    for row in csvreader:
        print(row[0]+","+row[1])