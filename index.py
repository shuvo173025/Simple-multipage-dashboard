import dash
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import numpy as np
from dash import dcc, html, Input, Output
from app import app
from app import server

from apps import Sentiment_Bar, Sentiment_pie, depression_bar, depression_pie



#### Collecting Data from responses form
def getting_data_from_responses_file():
    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)


    # The ID of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1mo2PwKH_IC0thDX0AAmnQotfJerjmv6GvlXau14yDLE'


    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    #### finding how many data we have
    res = service.spreadsheets().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                     fields='sheets(data/rowData/values/userEnteredValue,properties(index,sheetId,title))').execute()
    sheetIndex = 0
    lastRow = len(res['sheets'][sheetIndex]['data'][0]['rowData'])
    data = str("Here We have " + str(lastRow) + " individual Data")
    return data







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
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(children=[
        html.H4(html.Code(getting_data_from_responses_file()),style={'textAlign': 'center'})
    ]),
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



