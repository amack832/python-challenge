#Path to the csv file and setting up the reader
import os   
import csv

csvpath=os.path.join('Resources','election_data.csv')

with open(csvpath, newline='') as csvfile:

    poll_data= csv.reader(csvfile, delimiter=',')

    csv_header = next(poll_data)
    #Putting each column of data in it's own series
    candidate=[]
    
    for row in poll_data:
        candidate.append(row[2])
#Run a count of votes of each candidate.       
Kvotes = candidate.count("Khan")
Cvotes = candidate.count("Correy")
Lvotes = candidate.count("Li")
Ovotes = candidate.count("O'Tooley")
#Sum the total number of votes to find the total.
totalVotes = Kvotes + Cvotes + Lvotes + Ovotes
#Find the percentages of the total votes each candidate had.
Kperc = (Kvotes / totalVotes) * 100
Cperc = (Cvotes / totalVotes) * 100
Lperc = (Lvotes / totalVotes) * 100
Operc = (Ovotes / totalVotes) * 100
#Place each vote count into a dictionary with the corresponding candidate's name. 
Votes = {"Khan":Kvotes, "Correy":Cvotes, "Li":Lvotes, "O'Tooley":Ovotes}
#Then run a max function to find the winnner and have the variable say the winner's name, not the value that won.
winner = max(Votes, key=Votes.get)

print('Election Results')
print('-------------------------')
print(f'Total Votes: {totalVotes}')
print('-------------------------')
print(f'Khan: {round(Kperc, 2)}% ({Kvotes})')
print(f'Correy: {round(Cperc,2)}% ({Cvotes})')
print(f'Li: {round(Lperc, 2)}% ({Lvotes})')
print(f"O'Tooley: {round(Operc, 2)}% ({Ovotes})")
print('-------------------------')
print(f'Winner: {winner}')






        