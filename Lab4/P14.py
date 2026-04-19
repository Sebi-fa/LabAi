import pandas as pd

dataset = pd.read_csv("data.csv")

dataset["Score"] = (
    0.3 * dataset["Overall"] +
    0.3 * dataset["Potential"] +
    0.2 * dataset["SprintSpeed"] +
    0.2 * dataset["ShortPassing"]
)

print(dataset[["Name", "Score"]])