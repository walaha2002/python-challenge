# Import Libraries Generate and Read CSV file
import os
import csv

# Create Path to CSV file
csvpath = os.path.join( 'Resources','budget_data.csv')

# csv1 = pd.budget_data.csv("first_csv.csv")
# Create Lists for values
# date=[]
# profloss=[]

totalMonths=0
totalProfLoss=0
change=0
changeList = []
# nextRow=0
nextRowValue=0

# grandTotal = 0

# Skip first row when counting total Months

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
# print(csv_header)

    for row in csvreader:
#         date.append(row[1])
# print(date)

# print(row[0]+","+row[1])
# print(row)
# totalMonths = len(date)
# print(totalMonths)
       
        totalMonths=totalMonths+1
        totalProfLoss += int(row[1])


        nextRow = next(csvreader)
        nextRowValue += int(row[1])
        change = nextRowValue-int(row[1])
        setChange = changeList.append(change)

        
        # for row in next(csvreader):
        #     change = (row[1])
        #     # change = int(row[1])-totalProfLoss
        #     setChange = changeList.append(change)

        # change = next(csvreader)-int(row[1])
        # setChange = changeList.append(change)
#WORKING print(totalMonths)


# row=3
# previousRow = 2
# If row>=3:
#     for row in csvreader:
#         change = row[1]-previousRow[1]
#         setChange = changeList.append(change)

# print(changeList)


#         for next row in csvreader:
#             change = int(row+1[1])-int(row[1])

        
print("Total Months: "+ str(totalMonths))
print("Total: "+ str(totalProfLoss))
print(changeList)