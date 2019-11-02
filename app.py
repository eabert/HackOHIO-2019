import os
import json
import datetime as dt
import math
import requests

import pandas as pd

from flask import Flask
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

# Load data
# with open('data/osu_buildings.json') as f:
#     buildings = json.load(f.read())

navbar = dbc.Container()

body = dbc.Container(
    html.H1("Hack OHI/O 2019"),
    dbc.Spinner()
    #dcc.Input(id='test_input', value='Yes'),
    #dcc.Graph(id='building_map')
)

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([navbar, body])

# @app.callback(
#     Output('building_map', 'figure'),
#     Input('test_input', 'value')
# )
# def make_building_map(test_input):
#     traces = []
#     for well_type, dfff in dff.groupby('Well_Type'):
#         trace = dict(
#             type='scattermapbox',
#             lon=dfff['Surface_Longitude'],
#             lat=dfff['Surface_latitude'],
#             text=dfff['Well_Name'],
#             customdata=dfff['API_WellNo'],
#             name=WELL_TYPES[well_type],
#             marker=dict(
#                 size=4,
#                 opacity=0.6,
#             )
#         )
#         traces.append(trace)
# 
    # figure = dict(data=traces, layout=layout)
    # return figure

# Main
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)