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

coldshowernum = "125K"
hotshowernum = "150K"
boltnum = "35K"
steamnum = "73K"


navbar = dbc.Container()

body = dbc.Container(
    [
        html.H1("Hack OHI/O 2019"),
        dcc.Graph(
            figure = building_map
        ),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Col(width='300px'),
                        dbc.Col(
                            dbc.CardImg(src='/assets/images/shower.svg', style={'height':'40px','padding-left':'27px','padding-top':'10px'}),
                            width='100px'
                        ),
                        dbc.Col(
                            html.H5(hotshowernum,className="card-title",style={'color':'darkred','text-align':'right','font-size':'400%','font-weight':'bold','font-family':'Arial','padding-left':'15px'}),
                            width='160px'
                        )
                    ]),
                    html.H6("KBTU per hour",className='card-subtitle',style={'color':'darkred','text-align':'center','font-size':'100%','font-family':'Arial'}),
                    dbc.CardBody(
                        [
                            html.H4("Cold Water Usage", className="card-title",style={'text-align':'center'}),
                            html.P("This is equivalent to brewing 540 pots of coffee.",
                            className="card-text",style={'text-align':'center'}
                            )
                    ])
                
                ])
            ],align='stretch'),
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Col(width='300px'),
                        dbc.Col(
                            dbc.CardImg(src='/assets/images/shower.svg', style={'height':'40px','padding-left':'27px','padding-top':'10px'}),
                            width='100px'
                        ),
                        dbc.Col(
                            html.H5(coldshowernum,className="card-title",style={'color':'skyblue','text-align':'right','font-size':'400%','font-weight':'bold','font-family':'Arial','padding-left':'15px'}),
                            width='160px'
                        )
                    ]),
                    html.H6("KBTU per hour",className='card-subtitle',style={'color':'skyblue','text-align':'center','font-size':'100%','font-family':'Arial'}),
                    dbc.CardBody(
                        [
                            html.H4("Cold Water Usage", className="card-title",style={'text-align':'center'}),
                            html.P("This is equivalent to running the microwave for 1 hour every day for a month.",
                            className="card-text",style={'text-align':'center'}
                            )
                    ])
                
                ])
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Col(width='300px'),
                        dbc.Col(
                            dbc.CardImg(src='/assets/images/bolt.svg', style={'height':'40px','padding-left':'50px','padding-top':'10px'}),
                            width='100px'
                        ),
                        dbc.Col(
                            html.H5(boltnum,className="card-title",style={'color':'gold','text-align':'right','font-size':'400%','font-weight':'bold','font-family':'Arial','padding-left':'15px'}),
                            width='160px'
                        )
                    ]),
                    html.H6("Kilowatts per hour",className='card-subtitle',style={'color':'gold','text-align':'center','font-size':'100%','font-family':'Arial'}),
                    dbc.CardBody(
                        [
                            html.H4("Energy Usage", className="card-title",style={'text-align':'center'}),
                            html.P("This is equivalent to operating 24 laptop computers during a standard workday.",
                            className="card-text",style={'text-align':'center'}
                            )
                    ])
                
                ])
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Col(width='300px'),
                        dbc.Col(
                            dbc.CardImg(src='/assets/images/steam.svg', style={'height':'40px','padding-left':'50px','padding-top':'10px'}),
                            width='100px'
                        ),
                        dbc.Col(
                            html.H5(steamnum,className="card-title",style={'color':'gray','text-align':'right','font-size':'400%','font-weight':'bold','font-family':'Arial','padding-left':'15px'}),
                            width='160px'
                        )
                    ]),
                    html.H6("KBTU per hour",className='card-subtitle',style={'color':'gray','text-align':'center','font-size':'100%','font-family':'Arial'}),
                    dbc.CardBody(
                        [
                            html.H4("Steam Usage", className="card-title",style={'text-align':'center'}),
                            html.P("This is equivalent to cooling off a room with a medium air conditioner for 22 hours.",
                            className="card-text",style={'text-align':'center'}
                            )
                    ])
                
                ])
            ]),
        ],style={'padding-top':10,'padding-bottom':10},justify='stretch',align='center',no_gutters=True),
        html.H5("Data provided by ENGIE. Built with " + u"\u2665" + " at Hack OHI/O 2019 by Cole Smith, Elizabeth Gilbert, and Matthew Walker.",style={'text-align':'center'})
    ]
)

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
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