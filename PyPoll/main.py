import pandas as pd
file = 'Resources/election_data.csv'
df = pd.read_csv(file)
#finding the file 
total_votes = (len(df))
#finding total votes
candidate_names = df["Candidate"].unique()
#series of names of candidataes
candidate_grouped = df.groupby(["Candidate"])
candidate_total = candidate_grouped.count()
#group by candidate and total the votes
total = candidate_total.loc[["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"],"Ballot ID"]
#this seems useless but my code errors when i don't inclue it
sum = total.sum()
percentage = (total*100/sum).map("{:,.2f}%".format)
#formatting percentage
ordered_totals = candidate_total.sort_values("Ballot ID",ascending=False)
#sort to find the winner
winner = str(ordered_totals.iloc[0])
#print results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(percentage)
print("-------------------------")
print("Winner: "+ winner)
print("-------------------------")

