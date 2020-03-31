import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

########### Define your variables ######

myheading1='COVID-19 Tax rebate'
tabtitle = 'COVID-19 Income tax calculator'



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle


###### Colors
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
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
                 {'label': "Married", 'value': 2}], value= 1),

    #################### Salary inputs
    html.Label('Enter your gross income on your most recent tax filing 2018 or 2019'),
    dcc.Input(id='salary',  type='number'),



    ######################## Dependents inputs
    html.Label('Enter number of dependents you claimed'),
    dcc.Input(id='dependents', type='number',value=0),

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
    if salary <= 75000*filing_status:
        x = 1200*filing_status
    else:
        difference = (salary)-(75000*filing_status)
        depreciate_amount = int(difference/100)*5
        depreciate_amount = min(1200*filing_status, depreciate_amount)
        x =  1200*filing_status - depreciate_amount
    y = x + 500*dependents
    return y
############ Deploy
if __name__ == '__main__':
    app.run_server()
