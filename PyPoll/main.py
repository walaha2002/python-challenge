import os
import csv

csvpath = os.path.join( 'Resources','election_data.csv')

# Create Function that passes election data
def print_results():
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

# Prints to terminal
print_results()

# Specifies the File to write to
output_file=os.path.join( 'Resources','pyPollResults.csv')

# Open output file
with open(output_file,"w", newline='') as csvfile:
    # csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter=csv.writer(csvfile,delimiter=',')
    # csvwriter.writerows([print_results()])
    # csvwriter.print_results()
    # writer.print_results()
    # print_results()
# print("Election Results")
# print("-----------------------")
# print("Total Votes: "+str(total_votes))
# print("-----------------------")
# # print(votes_by_candidate)
# print(f'Khan: {votes_by_candidate["Khan"]}')
# print(f'Correy: {votes_by_candidate["Correy"]}')
# print(f'Li: {votes_by_candidate["Li"]}')
# print("O'Tooley: "+ str({votes_by_candidate["O'Tooley"]}))
# print("-----------------------")
# print("Winner: "+max_key)
