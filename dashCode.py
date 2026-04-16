from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import csv

app = Dash()

sale=[]
date=[]
region=[]
with open("data\daily_sales_data_MERGED.csv", newline="") as csvfile:
    reader=csv.reader(csvfile, delimiter=",", quotechar=" ")
    for row in reader:
        sale.append(row[0])
        date.append(row[1])
        region.append(row[2])

    
df = pd.DataFrame(dict(date=date,sales=sale))

fig = px.line(df, x="date", y="sales", title="Pink morsel sales")

app.layout = html.Div(children=[
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)