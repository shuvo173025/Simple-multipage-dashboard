import dash
import pandas as pd
import numpy as np
from dash import dcc, html, Input, Output
from app import app
from app import server

from apps import Sentiment_Bar, Sentiment_pie, depression_bar, depression_pie




app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.H1(children='Hello ( - )', style={'textAlign': 'center'}),
        html.H3(children='Shuvo: Welcome to my UGLY Dashboard.', style={'textAlign': 'center'}),
        html.Br(),
        html.Br(),
    ]),
    html.Div([
        dcc.Link('Pie for Sentiment | ', href='/apps/Sentiment_pie'),
        dcc.Link('Bar for Sentiment | ', href='/apps/Sentiment_Bar'),
        dcc.Link('Pie for Depression | ', href='/apps/depression_pie'),
        dcc.Link('Bar for Depression', href='/apps/depression_bar'),
    ], className="row",style={'textAlign': 'center'}),
    html.Div(id='page-content', children=[])
])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/depression_pie':
        return depression_pie.layout

    if pathname == '/apps/depression_bar':
        return depression_bar.layout

    if pathname == '/apps/Sentiment_pie':
        return Sentiment_pie.layout

    if pathname == '/apps/Sentiment_Bar':
        return Sentiment_Bar.layout



if __name__ == '__main__':
    app.run_server(debug=False)



