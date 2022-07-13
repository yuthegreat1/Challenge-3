import pandas as pd
file = 'Resources/election_data.csv'
df = pd.read_csv(file)
total_votes = (len(df))
candidate_names = df["Candidate"].unique()
candidate_grouped = df.groupby(["Candidate"]
candidate_total = candidate_grouped.count()
total = candidate_total.loc[["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"],"Ballot ID"]