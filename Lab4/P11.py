import pandas as pd

dataset = pd.read_csv("data.csv")

club_mean = dataset.groupby("Club")["Overall"].mean()

best_club = club_mean.idxmax()
best_value = club_mean.max()

print("Club:", best_club)
print("Media Overall:", best_value)