import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output

myheading1='AIRINC April 2020 Prices of Toilet Paper and Disinfectant'
tabtitle = 'Commodity Prices'
AIRINC_link='https://airshare.air-inc.com/covid-19-comparison-global-prices-for-impacted-goods'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

colors = {
    'background': '#111111',
    'text': 'rgb(60,5,224)'
}
df = pd.read_csv('prices.csv')

fig = go.Figure(go.Bar(
    x=df['Price per 500 ml of Disinfectant'],
    y=df['City'],
    orientation='h'))

app.layout = html.Div([

    html.H1(myheading1,
            style = {'color': colors['text']}),
    html.A('Link back to AIRINC Blog', href=AIRINC_link),


    #Commoditity input
    html.Label('Choose a product'),
    dcc.Dropdown(
        id='product',
        options=[
            {'label':'Disinfectant Prices','value': 'Price per 500 ml of Disinfectant'},
            {'label':'Toilet paper prices','value': 'Price of a Toilet Paper Roll'}],value = 'Price per 500 ml of Disinfectant'),
    ##### Graph
    dcc.Graph(id = 'plot', figure = fig),
    ######## output functions
    ],
)


@app.callback(
    Output(component_id='plot', component_property='figure'),
    [Input(component_id='product', component_property='value')])

def update_figure(product):
    df_live=df.sort_values(product)

    fig = go.Figure(go.Bar(
        x=df_live[product],
        y=df_live['City'],
        orientation='h'))
    fig.update_traces(texttemplate=df_live['City'], textposition='outside')
    fig.update_layout(
    title= product,
    xaxis = dict(
        title='Prices in USD',
        titlefont_size=16,
        tickfont_size=14),
    yaxis=dict(
        title='Select Survey Cities',
        titlefont_size=16,
        tickfont_size=14,
        showticklabels=False,)
)
    return fig

if __name__ == '__main__':
    app.run_server(port=8080, debug=True)
