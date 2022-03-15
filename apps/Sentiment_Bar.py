from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import dash
import plotly.graph_objects as go
from dash import dcc
from dash import html
from app import app
from app import server


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

    #### finding the range automatically
    res = service.spreadsheets().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                     fields='sheets(data/rowData/values/userEnteredValue,properties(index,sheetId,title))').execute()
    sheetIndex = 0
    sheetName = res['sheets'][sheetIndex]['properties']['title']
    lastRow = len(res['sheets'][sheetIndex]['data'][0]['rowData'])
    lastColumn = max([len(e['values']) for e in res['sheets'][sheetIndex]['data'][0]['rowData'] if e])
    _range_ = str(sheetName) + '!A1:G' + str(lastRow)

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=_range_).execute()
    values = result.get('values', [])
    Data = pd.DataFrame(values)
    return Data





#### cleaning Data
def clean_label_data():
    Data = getting_data_from_responses_file()
    sentiment = Data[4].value_counts()
    sentiment = sentiment.drop(['Sentiment'])
    sentiment_labels = sentiment.index.tolist()
    return sentiment_labels


def clean_value_data():
    Data = getting_data_from_responses_file()
    sentiment = Data[4].value_counts()
    sentiment = sentiment.drop(['Sentiment'])
    sentiment_values = sentiment.values.tolist()
    return sentiment_values



#chart
layout = html.Div(children=[
    html.Div([

        html.Br(),
        html.Br(),

        html.H4('Bar Chart for Sentiment Data ', style={"textAlign": "center"}),

        dcc.Graph(
                id='graph1',
                figure=go.Figure(data=[go.Bar(x=clean_label_data(), y=clean_value_data())])
            )
    ]),
])
















