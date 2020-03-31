import dash
import dash_core_components as dcc
import dash_html_components as html

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
    #################### Salary inputs
    html.Label('Enter your gross income on your most recent tax filing 2018 or 2019'),
    dcc.Input(id='Salary',  type='number'),



    ######################## Dependents inputs
    html.Label('Enter number of dependents you claimed'),
    dcc.Input(id='Dependents', type='number'),

])
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

############ Deploy
if __name__ == '__main__':
    app.run_server()
