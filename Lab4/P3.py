import pandas as pd

dataset = pd.read_csv("data.csv")

top_players = dataset[(dataset["Overall"] >= 85) & (dataset["Age"] < 25)]
print(top_players)