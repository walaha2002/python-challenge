## PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## Hints and Considerations

* Consider what we've learned so far. To date, we've learned how to import modules like `csv`; to read and write files in various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. Using what we've learned, try to break down your tasks into discrete mini-objectives. This will be a _much_ better course of action than spending all your time looking for a solution on Stack Overflow.

* As you will discover, for some of these challenges, the datasets are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. While our first instinct, as data analysts, is often to head straight into Excel, creating scripts in Python can provide us with more robust options for handling "big data".

* Write one script for each dataset provided. Run your script separately to make sure that the code works for its respective dataset.

* Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. You get what you put in, and the art of programming is extremely unforgiving to moochers. Dig your heels in, burn the night oil, and learn this while you can! These are skills that will pay dividends in your future career.

* Start early, and reach out for help often! Challenge yourself to identify _specific_ questions for your instructors and TAs. Don't resign yourself to simply saying, "I'm totally lost." If you need help, reach out because we're happy to help. But, come prepared and show us what you have done and your thought process.

* Always commit your work and back it up with GitHub pushes. You don't want to lose hours of your work because you didn't push it to GitHub every half hour or so.

  * Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

  

## Copyright

Trilogy Education Services © 2019. All Rights Reserved.


## Code for PyPoll
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