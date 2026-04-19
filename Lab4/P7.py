import pandas as pd

dataset = pd.read_csv("data.csv")

most_common = dataset["Nationality"].value_counts().idxmax()
print("Cea mai frecventa nationalitate:", most_common)

top5 = dataset["Nationality"].value_counts().head(5)
print("Top 5 nationalitati:")
print(top5)