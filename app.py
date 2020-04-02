import dash
import dash_core_components as dcc
import dash_html_components as html
import openpyxl
from dash.dependencies import Input, Output
import pandas as pd
import pickle
import csv

########### Define your variables ######

myheading1='COVID-19 Tax rebate'
tabtitle = 'COVID-19 Income tax calculator'

###### create storage



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle


###### Colors
colors = {
    'background': '#111111',
    'text': 'rgb(60,5,224)'
}

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1,
            style = {'color': colors['text']}
),
    #Filing Status
    html.Label('Filing status'),

    dcc.Dropdown(
        id='filing_status',
        options=[{'label': "Single", 'value': 1},
                 {'label': "Married Filing Jointly", 'value': 2}], value= 1),

    #################### Salary inputs
    html.Label('Enter your Adjusted Gross Income'),
    dcc.Input(id='salary',  type='number'),



    ######################## Dependents inputs
    html.Label('Enter the number of dependent children under the age of 17'),
    dcc.Input(id='dependents', type='number',value=0, min=0, max=5),

    ######## output functions
    html.H4(id='my-div3', style={'color': colors['text']}),], style = {'columnCount': 1}
)

########## callbacks
@app.callback(
    Output(component_id='my-div3', component_property='children'),
    [Input(component_id='filing_status', component_property='value'),
     Input(component_id='salary', component_property='value'),
     Input(component_id='dependents', component_property='value')])

####### tax logic function
def update_output_div(filing_status,salary,dependents):
    fields = [filing_status,salary,dependents]
    with open('file_inputs.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    ########## Define variables

    dependent_allowance = 500*dependents
    max_allowance = 1200*filing_status + dependent_allowance
    min_threshold= (75000 * filing_status)
    ###### Apply simple situation logic
    if salary <= min_threshold:
        return max_allowance
    ###### Apply logic for reduction
    else:
        difference = (salary - min_threshold)
        depreciate_allowance = max_allowance - (difference*.05)
        absolute_allowance = max(0,depreciate_allowance)
        return absolute_allowance



############ Deploy
if __name__ == '__main__':
    app.run_server()

