import plotly.express as px
import csv

with open("./data/coffee_vs_hours_of_sleep.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="Coffee in ml", y="sleep in hours", color="week")
      fig.show()