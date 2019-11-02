import os
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

navbar = dbc.Container()

body = dbc.Container(
    html.H1("Hack OHI/O 2019"),
    dcc.Input(id='test_input', value='Yes')
    dcc.Graph(id='building_map')
)

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([navbar, body])

@app.callback(
    Output('building_map'),
    Input('test_input')
)

# Main
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)