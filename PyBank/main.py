# Import Libraries Generate and Read CSV file
import os
import csv

# Create Path to CSV file
csvpath = os.path.join( 'Resources','budget_data.csv')

# csv1 = pd.budget_data.csv("first_csv.csv")

totalMonths=0
totalProfLoss=0

# grandTotal = 0

# Skip first row when counting total Months

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
# print(csv_header)

    for row in csvreader:
# print(row[0]+","+row[1])
# print(row)
        totalMonths = totalMonths+1
        totalProfLoss += int(row[1])
print("Total Months: "+ str(totalMonths))
print("Total: "+ str(totalProfLoss))
        # if grandTotal.isdigit():
        #     grandTotal = int(row[1])
# grandTotal = [sum(row[1])for row in zip(csvreader)]
# print(index)

# grandTotal = grandTotal+int(row[1])

# print("Total Months: "+ str(totalMonths))
# print(grandTotal)
# print(row[0])
