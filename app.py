import os
import json
import datetime as dt
import math
import requests

import pandas as pd
import plotly.graph_objs as go

from flask import Flask
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

with open('data/osu_buildings.json', 'r') as f:
    osu_buildings = json.load(f)

buildings = pd.read_csv('data/HackathonConfig.csv')
buildings['BuildingName'] = buildings.BuildingName.str.replace('Mendenhall Laboratory', 'Mendenhall, Thomas C, Laboratory')
buildings['BuildingName'] = buildings.BuildingName.str.replace('Page Hall', 'Page, Henry F, Hall')

building_map = dict(
    data = [dict(
        lat = buildings.Latitude.astype(float).to_list(),
        lon = buildings.Longitude.astype(float).to_list(),
        mode = 'markers',
        marker = dict(
            size=3,
            opacity=0
        ),
        text = buildings.BuildingName.to_list(),
        type = 'scattermapbox'
    )],
    layout = dict(
        width=1200,
        height=700,
        hovermode='closest',
        mapbox=dict(
            accesstoken='pk.eyJ1IjoiY3NtaXRoZHMiLCJhIjoiY2syaHV0dTZvMDd4MTNob2hpbTNodWl0aSJ9.DZvSZ91qr3P07AJA0tLU7w',
            bearing=0,
            center=dict(
                lat=40.000,
                lon=-83.020
            ),
            pitch=0,
            zoom=14,
            layers=[
                dict(
                    sourcetype = 'geojson',
                    source = osu_buildings,
                    type = 'fill',
                    color = 'red'
                )
            ]
        ),
        margin=dict(b=0,l=0,r=0,t=0)
    )
)


navbar = dbc.Container()

body = dbc.Container(
    [
        html.H1("Hack OHI/O 2019"),
        dcc.Graph(
            figure = building_map
        )
    ]
)

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([navbar, body])

# @app.callback(
#     Output('building-map', 'figure'),
#     [Input('test-input', 'value')]
# )
# def make_building_map(test_input):
#     data = [go.Scattermapbox(
#             lat=buildings.Latitude.astype(float).to_list(),
#             lon=buildings.Longitude.astype(float).to_list(),
#             mode='markers',
#             marker=dict(
#                 size=3,
#                 opacity=0
#             ),
#             text=buildings.BuildingName.to_list()
#         )]

#     layout = dict(
#         autosize=True,
#         hovermode='closest',
#         mapbox=dict(
#             accesstoken='pk.eyJ1IjoiY3NtaXRoZHMiLCJhIjoiY2syaHV0dTZvMDd4MTNob2hpbTNodWl0aSJ9.DZvSZ91qr3P07AJA0tLU7w',
#             bearing=0,
#             center=go.layout.mapbox.Center(
#                 lat=40.000,
#                 lon=-83.020
#             ),
#             pitch=0,
#             zoom=14,
#             layers=[
#                 dict(
#                     sourcetype = 'geojson',
#                     source = 'data/osu_buildings.json',
#                     type = 'fill',
#                     color = 'red'
#                 )
#             ]
#         ),
#         margin=dict(b=0,l=0,r=0,t=0)
#     )

#     fig = dict(data=data, layout=layout)
#     return fig

# Main
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)