from dash import Dash, dcc, html, Input, Output, callback
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
        if row[0]!="Date":
            sale.append(row[0])
            date.append(row[1])
            region.append(row[2])

    
df = pd.DataFrame(dict(date=date,sales=sale,region=region))

#fig = px.line(df, x="date", y="sales", title="Pink morsel sales")

# initialize dash
dash_app = Dash(__name__)

app.layout = html.Div(children=[
    dcc.Graph(
        id='graph',
        #figure=fig
    ),

    dcc.RadioItems(['All', 'North', 'East', 'South', 'West'], 'All', inline=True, id="region")
])

@callback(
    Output('graph', 'figure'),
    Input('region', 'value'))
def update_figure(input_value):
    if input_value=="All":
        filtered_df = pd.DataFrame(dict(date=date,sales=sale,region=region))
        fig = px.line(filtered_df, x="date", y="sales", title="Pink morsel sales")
    else:
        filtered_df = df[df.region == input_value.lower()]
        fig = px.line(filtered_df, x="date", y="sales", title="Pink morsel sales")
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    dash_app.run_server()