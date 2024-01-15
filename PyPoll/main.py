#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

import os
import csv

#relative path to the budget data csv file
election_data_import = os.path.join ("python-challenge", "PyPoll", "Resources", "election_data.csv")

#set up lists to store data in
vote_tally = []
# counties = [] not actually using county data
candidate_tally = []
candidates = []
votes_for_each = []
percent_each = []

with open(election_data_import) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #first, skip header row to start for loop through the dataset
    next(csvreader)

    #build lists from csv data
    for row in csvreader:
        #add up number of votes
        vote_tally.append(row[0])
        #save all candidates in a list
        candidate_tally.append(row[2])

    #makde a list of unique candidates (sources:https://datagy.io/python-count-unique-values-list/)
    for tally in candidate_tally:
        if tally not in candidates:
            candidates.append(tally)

    #make a list of the number of times each candidates appears in candidate_tally (one appearance = one vote)
    for each in candidates:
        votes_for_each.append((candidate_tally.count(str(each))))
    
    #calculate percentage of votes won (converted to percentage, formatted to two decimal points)
    percent_each = [f'{float(round((int(tally)/int(len(vote_tally)))*100, 3))} %' for tally in votes_for_each]
    
    #zip together the candidate, percentage of votes won, and number of votes won
    candidate_summary = zip(candidates, percent_each, votes_for_each)

    #find the location of the winner in votes for each
    winner_index = votes_for_each.index(max(votes_for_each))
    #then use that index value to find the name of the winner in candidates
    winner = candidates[int(winner_index)]

    #final results
    print("Election Reusults")
    print("-------------------------------------------")
    print(f'Total votes: {str(len(vote_tally))}')
    for candidate in candidate_summary:
        print(candidate)
    print("----------------------------------------------")
    print(f'The winner is: {winner}')