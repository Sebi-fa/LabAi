import pandas as pd

dataset = pd.read_csv("data.csv")

def convert_money(x):
    if isinstance(x, str):
        x = x.replace('€', '').replace('K', '000').replace('M', '000000')
        return float(x)
    return x

dataset["Value"] = dataset["Value"].apply(convert_money)
dataset["Wage"] = dataset["Wage"].apply(convert_money)

good_deals = dataset[["Name", "Wage", "Value"]].copy()

good_deals["difference"] = good_deals["Value"] - good_deals["Wage"]

good_deals = good_deals.sort_values(by="difference", ascending=False)

print(good_deals.head(10))