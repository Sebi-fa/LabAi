import pandas as pd

dataset = pd.read_csv("data.csv")

rows, cols = dataset.shape
print("Numar randuri:", rows)
print("Numar coloane:", cols)

unique_players = dataset["Name"].nunique()
print("Numar jucatori unici:", unique_players)