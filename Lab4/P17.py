from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd

dataset = pd.read_csv("data.csv")

def convert_money(x):
    if isinstance(x, str):
        x = x.replace('€', '').replace('K', '000').replace('M', '000000')
        return float(x)
    return x

dataset["Value"] = dataset["Value"].apply(convert_money)
dataset["Wage"] = dataset["Wage"].apply(convert_money)

output_file("ex17.html")

source = ColumnDataSource(dataset)

p = figure(title="Wage vs Value")

p.scatter("Wage", "Value", size=8, source=source)

hover = HoverTool(tooltips=[
    ("Name", "@Name"),
    ("Wage", "@Wage"),
    ("Value", "@Value")
])

p.add_tools(hover)

show(p)