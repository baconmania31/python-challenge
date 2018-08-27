import os
import csv
#define path
csvpath = os.path.join('..','Resources', 'election_data.csv')
#define empty lists
voter = []
county = []
canidate = []
#pulls out needed data from csv
with open(csvpath, newline ='') as csvfile:
    pollSet = csv.reader(csvfile, delimiter = ',')
    #skip header
    next(pollSet,None)
    for row in pollSet:
      voter.append(row[0])
      county.append(row[1])
      canidate.append(row[2])
#count the num of votes
votes = len(voter)
#find list of unique canidate values
uniqCand = list(set(canidate))
#set up blank list for canidate votes
candVotes = []
#count num of times each value in uniqCands appears in canidate = # votes for each canidate. candVote index = uniqCand index.
i = 0
while i <= len(uniqCand)-1:
    candVotes.append(canidate.count(uniqCand[i]))
    i = i + 1
#Calculate the percentage of the vote each canidate got
pctVotes = [(x/votes)*100 for x in candVotes]
#find the canidate with the max number of votes
winner = uniqCand[candVotes.index(max(candVotes))]
#print results
print("Election Results \n")
print("-------------------- \n")
print("Total Votes: " + str(votes) + "\n")
print("-------------------- \n")
print("Khan: " + str(pctVotes[0]) + "% (" + str(candVotes[0]) + ") \n")
print("O'Tooley: " + str(pctVotes[1]) + "% (" + str(candVotes[1]) + ") \n")
print("correy: " + str(pctVotes[2]) + "% (" + str(candVotes[2]) + ") \n")
print("Li: " + str(pctVotes[3]) + "% (" + str(candVotes[3]) + ") \n")
print("--------------------- \n")
print("Winner: " + str(winner))
output_file = os.path.join("vote_final.txt")
with open(output_file, "w") as f:
    f.write("Election Results \n")
    f.write("-------------------- \n")
    f.write("Total Votes: " + str(votes) + "\n")
    f.write("-------------------- \n")
    f.write("Khan: " + str(pctVotes[0]) + "% (" + str(candVotes[0]) + ") \n")
    f.write("O'Tooley: " + str(pctVotes[1]) + "% (" + str(candVotes[1]) + ") \n")
    f.write("correy: " + str(pctVotes[2]) + "% (" + str(candVotes[2]) + ") \n")
    f.write("Li: " + str(pctVotes[3]) + "% (" + str(candVotes[3]) + ") \n")
    f.write("--------------------- \n")
    f.write("Winner: " + str(winner))