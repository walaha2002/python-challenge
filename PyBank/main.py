# Import Libraries Generate and Read CSV file
import os
import csv

# Create Path to CSV file
csvpath = os.path.join( 'Resources','budget_data.csv')


# Declaring Variables
totalMonths=0
totalProfLoss=0

# Declaring change variable that holds the results from subtracting next row from current row
change=0

# Creating lists to hold values for date and profloss
date=[]
profloss=[]

# Creating variable that assist with calculating change
x=0
y=1
z=1

# Variable to create limit on # of times to go through For Loop so it keeps checking the If statement right under it 
allowance=85

# This list holds the profit/loss changes from month to month
changerecord=[0]

# These 2 variables hold the values for max/min changes from the changerecord list
maxchange=0
minchange=0

# Zipping the lists together to try and retrieve the date for the high/low changes
# indexes = []
zipper= zip(changerecord,date)
# zipper=set(zipper)


# Skip first row when counting total Months

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    # csvreader2 = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)

    # Reading data in previously opened file to obtain tallies for Total Months and Summing the totals in ProfLoss
    # Also creating a list for all of the dates and a list for profloss so I can use it later in a calculation
    for row in csvreader:
        totalMonths=totalMonths+1
        totalProfLoss += int(row[1])
        profloss.append(row[1])
        date.append(row[0])
    
    # This For Loop and If Statement runs through the entire file and then subtracts the value from the next record 
    # from the current record to calculate the change between each month and then appends the change to a changerecord list
    for z in range (allowance):
        if y>x:
            # for x in profloss:
            #     for y in profloss:
            change = int(profloss[y])-int(profloss[x])
            changerecord.append(change)
            x=x+1
            y=y+1
        

    # Retrieves value for max and min change
    # I Googled this solution to get min and max; min(zipper) isn't working because there's a zero value in the change; No time to troubleshoot
    # maxchange = max(changerecord)
    minchange = min(changerecord)
    maxchange=max(zipper)

    

# Below is the calculation for average change using the in the profloss lists
# https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python#:~:text=Use%20round()%20to%20limit,float%20to%20two%20decimal%20places.
    avgchange=(int(profloss[85])-int(profloss[0]))/85
    a_float=avgchange
    limit_float=round(a_float,2)
    
    # Print Statements Below        
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: "+str(totalMonths))
    print("Total:  $"+str(totalProfLoss))  
    print("Average Change: $"+str(limit_float))
    print("Greatest Increase in Profits:  $"+str((maxchange)))
    print("Greatest Decrease in Profits:  $"+str((minchange)))

# Specifies the File to write to
output_file=os.path.join( 'analysis','pyBankResults.txt')

# Open output file and print to it
with open(output_file,"w") as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Total Months: '+str(totalMonths)])
    csvwriter.writerow(['Total:  $'+str(totalProfLoss)]) 
    csvwriter.writerow(['Average Change: $'+str(limit_float)])
    csvwriter.writerow(['Greatest Increase in Profits:  '+str((maxchange))])
    csvwriter.writerow(['Greatest Decrease in Profits:  '+str((minchange))])


 # Below is a bunch of code I tried that didn't work    
    # 
    # for changerecord in zipper:
    #     print(
        
    

        #     if maxchange == changerecord:
        #         print("Greatest Increase in Profits:  "+date+" ($"+str((maxchange))+")")
        #     elif minchange == changerecord:
        #         print("Greatest Decrease in Profits:  "+date+" ($"+str((minchange))+")")



    # for h in range (allowance):
# row=2
    # for h in range (allowance):
    #     # if changerecord[i] > changerecord[j]:
    #     if increase>changerecord[i]:
    #         # increase = int(changerecord[i])
    #         greatestIncrease=increase
    #         # greatestIncrease.append(int(changerecord[i]))
    #     else:
    #         # greatestIncrease.append(int(changerecord[i]))
    #         greatestIncrease=int(changerecord[i])
    #         increase=int(changerecord[i])
    #         i=i+1
    #         # j=j+1
    # print(date)
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
