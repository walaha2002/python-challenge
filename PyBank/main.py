# Import Libraries Generate and Read CSV file
import os
import csv

# Create Path to CSV file
csvpath = os.path.join( 'Resources','budget_data.csv')

 # csv1 = pd.budget_data.csv("first_csv.csv")
# # Create Lists for values

totalMonths=0
totalProfLoss=0
change=0
changeList = []
# nextRow=0
# nextRowValue=0
date=[]
profloss=[]
greatestIncrease=[]
increase=0
greatestDecrease=[]
# currentrow = row
# row=1
# nextrow=row+1
x=0
y=1
z=1
h=1
i=1
j=2
allowance=85

changerecord=[]
# # grandTotal = 0

# # Skip first row when counting total Months

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    # csvreader2 = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
# # print(csv_header)

    for row in csvreader:
        totalMonths=totalMonths+1
        totalProfLoss += int(row[1])
        profloss.append(row[1])
    
    # for z in profloss:
    for z in range (allowance):
        if y>x:
            # for x in profloss:
            #     for y in profloss:
            change = int(profloss[y])-int(profloss[x])
            changerecord.append(change)
            x=x+1
            y=y+1

    # for h in range (allowance):
# row=2
    for h in range (allowance):
        # if changerecord[i] > changerecord[j]:
        if increase>changerecord[i]:
            # increase = int(changerecord[i])
            greatestIncrease=increase
            # greatestIncrease.append(int(changerecord[i]))
        else:
            # greatestIncrease.append(int(changerecord[i]))
            greatestIncrease=int(changerecord[i])
            increase=int(changerecord[i])
            i=i+1
            # j=j+1

# increase = int(changerecord[i])
            
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: "+str(totalMonths))
    print("Total: "+str(totalProfLoss))  
    # print(profloss[x])
    # print(profloss[y])   
    # print(int(profloss[y])-int(profloss[x]))
    # # print(profloss[85])
    avgchange=(int(profloss[85])-int(profloss[0]))/85
    print("Average Change: $"+str(avgchange))
    print(changerecord)
    print(greatestIncrease)
    # print(changerecord[1])

        # change = profloss(row+1[1]-int(row[1]))
        # changerecord.append(change)

        # change = 
        # changerecord.append(change)
        # nextrow=nextrow+1
        # currentrow=currentrow+1
    # print(changerecord)
    # for row in csvreader:
    #     totalMonths=totalMonths+1
    #     totalProfLoss += int(row[1])
    #     profloss.append(row[1])

        
#         profloss.append(row[1])
# # # print(date)

# # # print(row[0]+","+row[1])
# # # print(row)
# # # totalMonths = len(date)
# # # print(totalMonths)
       
        


#         monthlychange=totalProfLoss-nextRowValue
#         # final month-first month/85
        
# #         If row[1] != "":
            

#         # currentRow = row

#         # for row in csvreader2:
#         #     nextRow=2
#         #     change = nextRow[1]-currentRow[1]
#         #     setChange=changeList.append(change)
#         #     print(changeList)

#         # 

        
# #         # for row in next(csvreader):
# #         #     change = (row[1])
# #         #     # change = int(row[1])-totalProfLoss
# #         #     setChange = changeList.append(change)

# #         # change = next(csvreader)-int(row[1])
# #         # setChange = changeList.append(change)
# # #WORKING print(totalMonths)


# # # row=3
# # # previousRow = 2
# # # If row>=3:
# # #     for row in csvreader:
# # #         change = row[1]-previousRow[1]
# # #         setChange = changeList.append(change)

# # # print(changeList)


# # #         for next row in csvreader:
# # #             change = int(row+1[1])-int(row[1])

        
# print("Total Months: "+str(totalMonths))
# print("Total: "+str(totalProfLoss))
# print(monthlychange)
# # print(changeList)
