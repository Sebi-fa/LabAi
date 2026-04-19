import pandas as pd

dataset = pd.read_csv("data.csv")

dataset["Contract Valid Until"] = dataset["Contract Valid Until"].astype(str)
print(dataset[dataset["Contract Valid Until"].str.contains("2021", na=False)])