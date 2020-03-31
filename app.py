import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from collections import deque, Counter

########### Define your variables ######

myheading1='COVID-19 Tax rebate'
tabtitle = 'COVID-19 Income tax calculator'



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
 
    dcc.Input(id='my-id',  type='number'),
    html.Div(id='my-div')
])
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


############ Deploy
if __name__ == '__main__':
    app.run_server()
