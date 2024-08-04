# !pip install packaging
# !pip install pandas dash
# !pip3 install httpx==0.20 dash plotly
# !pip3 install httpx==0.20 dash plotly


# TASK 1
# Import required packages
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

# TASK 2
# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.

# TASK 3
# Add a title to the dashboard
title_change = ('Airline On-time Performance Dashboard',
                style={'textAlign': 'center',
                        'color': '#503D36',
                        'font-size': 50})
app.layout = html.Div(children=[html.H1( title_change), # Ex 1
                                html.P('Proportion of distance group (250 mile distance interval group) by flights.', 
                                       # TASK 4
                                       # Add description about the graph

                                       style={'textAlign':'center', 'color': '#F57241'}
),
                                dcc.Graph(figure=fig),
                                # TASK 5
                                # Add the pie chart to the dashboard
                                               
                    ])

# Run the application                   
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port =8050)



# TASK 6
# !python3 dash_basics.py


# Exercise : Practice Tasks
# You will practice some tasks to update the dashboard.

# 1 Change the title to the dashboard from “Airline Dashboard” to “Airline On-time Performance Dashboard” using HTML H1 component and font-size as 50.
# title_change = ('Airline On-time Performance Dashboard',
#                 style={'textAlign': 'center',
#                         'color': '#503D36',
#                         'font-size': 50})
## DONE 

# app.layout = html.Div(children=[html.H1( title_change)])

# 2 Save the above changes and relaunch the dashboard application to see the updated dashboard title.


# # Write a command to stop the running app in the terminal
# app.status = 'stop'

# print(python._version())