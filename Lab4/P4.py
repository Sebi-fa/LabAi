import pandas as pd

dataset = pd.read_csv("data.csv")

sorted_players = dataset.sort_values(by="Skill Moves", ascending=False)
print(sorted_players)