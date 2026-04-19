import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("data.csv")

top5 = dataset["Nationality"].value_counts().head(5)

top5.plot.pie(autopct='%1.1f%%')
plt.title("Top 5 naționalități")
plt.ylabel("")
plt.show()