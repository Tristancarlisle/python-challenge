from audioop import maxpp
import csv
import os 
##########################################################################
#1.  Reading CSV file and collecting total cote count and Candidate list



# set path name with os to ensure compatibility with different engines
filepath = os.path.join("Resources","election_data.csv")

#set the vote count as -1 to account for title - first row should not be counted.
votecount = -1

#set a list variable for candidates
candidates = []

Whole_file = []

#Opening and reading each row of the csv file 
with open(filepath) as file:
    reader = csv.reader(file, delimiter=",")

    #parsing through each row of the csv file
    for row in reader:
        #incrementing vote count: as it parses each vote will be counted for total 
       votecount=votecount+1
       #storing whole data set with headers
       Whole_file.append(row)
       #Creating the candidate list if the name voted for is not the title or in the list it is added to the list of candidates
       if row[2] not in candidates:
           if row[2] != "Candidate":
            candidates.append(row[2])

##########################################################################
                    # 2. Totals and percentages for each Candidat



#set another list variable for the total vote count for each candidate
    Totals = []

    #Nested for loop each candidate in the list has their individual count incremented each time they are voted for
    for x in candidates:
        #reseting total for each candidate
        total=0
        #allows us to reread the open csv file
        file.seek(0)
        next(reader)
        #for each row in the file if the candidates name is found increment their votecount
        for row in reader:
            if x == row[2]:
                total = total + 1
        #add each vote count to the list of totals
        Totals.append(total)

#function that calculates and and rounds the percentage of votes each candidate has
def percentage(x):
    return round(((x/votecount)*100),3)

#list of each candidates percentage
Percentages = []
#loop to calculate all percentages and append them to the list refering back to the percentage function
for x in Totals:
    Percentages.append(percentage(x))

##########################################################################
                    # 3.Winner of the Election


#finds max percentage then the index of that percentage in the list and finds the candidate associated
max = max(Percentages)
maxindex = Percentages.index(max)
winner = candidates[maxindex]

##########################################################################
                    # 4. Output 




print("Election Results")
print("-----------------------")
print(f'Total Votes: {votecount}')
print("-----------------------")
for i in range(4):
    print(f'{candidates[i]}: {Percentages[i]}%  ({Totals[i]})')
print("-----------------------")
print(f'Winner: {winner}')
print("-----------------------")


#writing output into a text file named PyPoll_analysis 

filepathanalysis = os.path.join("analysis","PyPoll_analysis.txt")
with open(filepathanalysis, "a") as f:
    print("Election Results", file=f)
    print("-----------------------", file=f)
    print(f'Total Votes: {votecount}', file=f)
    print("-----------------------", file=f)
    for i in range(4):
        print(f'{candidates[i]}: {Percentages[i]}%  ({Totals[i]})', file=f)
    print("-----------------------", file=f)
    print(f'Winner: {winner}', file=f)
    print("-----------------------", file=f)
