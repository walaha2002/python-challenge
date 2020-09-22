## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.


## Code for PyBank
# Import Modules that allow working with files from different operating systems and to use csv calls
import os
import csv

# Create path to CSV File we're reading
csvpath = os.path.join( 'Resources','election_data.csv')

# Create Function that prints election results
# Printing the results was a beast but I did it all myself except for the Percent formatting that Jeni Lamoureux shared with me
def print_results():
    print("Election Results")
    print("-----------------------")
    print("Total Votes: "+str(total_votes))
    print("-----------------------")
    print("Khan: "+ "{:.3%}".format((votes_by_candidate["Khan"])/total_votes) +" ("+str(votes_by_candidate["Khan"])+")")
    print("Correy: "+ "{:.3%}".format((votes_by_candidate["Correy"])/total_votes) +" ("+str(votes_by_candidate["Correy"])+")")
    print("Li: "+ "{:.3%}".format((votes_by_candidate["Li"])/total_votes) +" ("+str(votes_by_candidate["Li"])+")")
    print("O'Tooley: "+ "{:.3%}".format((votes_by_candidate["O'Tooley"])/total_votes) +" ("+str(votes_by_candidate["O'Tooley"])+")")
    # print("O'Tooley: "+ "{:.3%}".format((votes_by_candidate["O'Tooley"]))
    print("-----------------------")
    print("Winner: "+max_key)
    print("-----------------------")
   

# Create calculation that tally votes
total_votes=0

# Creating a list of unique names
unique_names=[]

# Create dictionary for all candidates
votes_by_candidate={}

# Open the file we created a path to using the variable created for the file    
with open(csvpath,newline='') as csvfile:

    # Read the file and define what the delimiter is in the file
    csvreader = csv.reader(csvfile,delimiter=",")

    # Skip the first row of the file
    csv_header = next(csvreader)

    # Create loop to go through every row of the file and get a count
    for row in csvreader:
        # Create a tally of votes to be added to the total_votes variable we declared
        total_votes = total_votes+1

        # Loop through every name in column 3 of the file and add the name to a list
        candidate = row[2]
        
        # Create unique list of names by first checking to see if the name already exists in the list
        if candidate not in unique_names:
            unique_names.append(candidate)
            #This keeps adding the names to the dictionary as keys
            votes_by_candidate[candidate]=0
            
            
        #This is a counter to keep track of how many times we're encountering the name which is essentially how many votes the candidate has                       
        votes_by_candidate[candidate] = votes_by_candidate[candidate]+1
        # percent=(int(row[0])/int(total_votes)) 
        
        
# I googled this part to see if there was an easy way to find the max value in a dictionary; it worked perfectly
# https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python
max_key = max(votes_by_candidate,key=votes_by_candidate.get)

# Prints to terminal using function
print_results()

# Specifies the File to write to
output_file=os.path.join( 'analysis','pyPollResults.txt')

# Open output file
# I tried to use my print_results function to write to the file so I wouldn't repeat myself but was unable to successfully write a solution

with open(output_file,"w") as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-----------------------------------'])
    csvwriter.writerow(['Total Votes: '+str(total_votes)])
    csvwriter.writerow(['-----------------------------------'])
    csvwriter.writerow(["Khan: "+ "{:.3%}".format((votes_by_candidate["Khan"])/total_votes) +" ("+str(votes_by_candidate["Khan"])+")"])
    csvwriter.writerow(["Correy: "+ "{:.3%}".format((votes_by_candidate["Correy"])/total_votes) +" ("+str(votes_by_candidate["Correy"])+")"])
    csvwriter.writerow(["Li: "+ "{:.3%}".format((votes_by_candidate["Li"])/total_votes) +" ("+str(votes_by_candidate["Li"])+")"])
    csvwriter.writerow(["O'Tooley: "+ "{:.3%}".format((votes_by_candidate["O'Tooley"])/total_votes) +" ("+str(votes_by_candidate["O'Tooley"])+")"])
    csvwriter.writerow(['-----------------------------------'])
    csvwriter.writerow(['Winner: '+max_key])
    csvwriter.writerow(['-----------------------------------'])

# Tried to Close the file but nothing I did worked
# output_file.close()

# Below is a bunch of stuff I tried but it didn't pan out
            # candidate_dictionary["Name"]=unique_names
            # candidate_dictionary["Vote Tally"]=votes_by_candidate
        # for unique_names in (row[2]):
        #     votes_by_candidate = votes_by_candidate+1
        #     candidate_dictionary["Vote Tally"]=votes_by_candidate

        # if unique_names == (row[2]):
        #     votes_by_candidate = votes_by_candidate+1
        #     candidate_dictionary["Name"]=unique_names
        #     candidate_dictionary["Vote Tally"]=votes_by_candidate

            # votes_by_candidate = votes_by_candidate+1
            # candidate_dictionary = {"Name":unique_names,"Vote Tally":votes_by_candidate}



