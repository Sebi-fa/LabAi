import pandas as pd

dataset = pd.read_csv("data.csv")

players_over_40 = dataset[dataset["Age"] > 40]
print(players_over_40)