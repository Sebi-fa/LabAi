import pandas as pd

dataset = pd.read_csv("data.csv")

def convert_money(x):
    if isinstance(x, str):
        x = x.replace('€', '').replace('K', '000').replace('M', '000000')
        return float(x)
    return x

dataset["Value"] = dataset["Value"].apply(convert_money)
dataset["Wage"] = dataset["Wage"].apply(convert_money)

dataset["is_underpaid"] = dataset["Wage"] < (dataset["Value"] / 100)

print(dataset[["Name", "Wage", "Value", "is_underpaid"]].head())