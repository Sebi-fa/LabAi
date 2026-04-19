import pandas as pd

dataset = pd.read_csv("data.csv")

dataset["Position"] = dataset["Position"].fillna("Unknown")

print(dataset["Position"].isnull().sum())