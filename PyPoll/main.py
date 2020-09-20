import os
import csv

csvpath = os.path.join( 'Resources','election_data.csv')

# Create Function that passes election data
def election_results(voter_data):
    voter_ID = int(election_data[0])
    county = str(election_data[1])
    candidate = str(election_data[2])

# Create calculations that tally votes
    total_votes=0
    
    # candidate_votes = 

    print("Total Votes: "+str(total_votes))
    
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        


