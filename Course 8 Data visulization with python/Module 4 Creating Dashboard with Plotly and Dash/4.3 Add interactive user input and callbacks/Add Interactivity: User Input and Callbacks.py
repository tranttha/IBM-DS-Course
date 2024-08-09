import pandas as pd 
import plotly.express as px 
import dash 
from dash import doc
from dash import html


airline_date = pd.read_csv(''https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})


data = airline_data.sample(n=500, random_state=42)

app = dash.Dash(__name__) # dash application layout
app.layout = html.Div(children=[html.H1(),\
                                   html.Div(["Input Year", dcc.Input,],
                                   style = {}),
                                   html.Br(),
                                   html.Br(),
                                   html.Div(),
                                   ])
# add callback decorator
@app.callback(Output(),
            Input())
# Add computation to callback function and return graph
def get_graph(entered_year):
    # Select data based on the entered year
    df =  airline_data[airline_data['Year']==int(entered_year)]
    
    # Group the data by Month and compute the average over arrival delay time.
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()
    
    # 
    fig = go.Figure(data=go, x = line_date['Month'], y= line_data['ArrDelay'], mode='lines', marker=dict(color='red'))

    fig.update_layout(title = 'Month vs. Avg Flight Delay time', xasix_title = 'Month', yaxis_title = 'Avg time delayed (Hours)')
    
    return fig
    
    
#ex1 
# title_change =  ('Total number of flights to the destination state split by reporting air',
#                 style={'textAlign': 'center',
#                         'color': '#503D36',
#                         'font-size': 50})
# Run the app
if __name__ == '__main__':
    app.run_server()

    