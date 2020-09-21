import os
import csv

csvpath = os.path.join( 'Resources','election_data.csv')

# Create Function that passes election data
# def election_results(voter_data):
#     voter_ID = int(election_data[0])
#     county = str(election_data[1])
#     candidate_name = str(election_data[2])

# Create calculations that tally votes
total_votes=0
candidate_list = []
unique_names=[]
vote_tally=[]
candidate_dictionary=dict()
votes_by_candidate=dict()

total_votes=total_votes+1
#percent_votes=/total_votes
    
    # candidate_votes = 
    
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes+1
        candidate_list.append(row[2])
        candidate = row[2]
        
        # if candidate_name in (candidates):
        if candidate not in unique_names:
            unique_names.append(candidate)
            votes_by_candidate[candidate]=0
            
        votes_by_candidate[candidate] = votes_by_candidate[candidate]+1
        
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
max_key = max(votes_by_candidate,key=votes_by_candidate.get)
print("Election Results")
print("-----------------------")
print("Total Votes: "+str(total_votes))
print("-----------------------")
# print(votes_by_candidate)
print(f'Khan: {votes_by_candidate["Khan"]}')
print(f'Correy: {votes_by_candidate["Correy"]}')
print(f'Li: {votes_by_candidate["Li"]}')
print("O'Tooley: "+ str({votes_by_candidate["O'Tooley"]}))
print("-----------------------")
print("Winner: "+max_key)
