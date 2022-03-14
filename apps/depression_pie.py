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
    SERVICE_ACCOUNT_FILE = 'assets/keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)


    # The ID of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1mo2PwKH_IC0thDX0AAmnQotfJerjmv6GvlXau14yDLE'


    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Form Responses 1!A1:G1076").execute()
    global values
    values = result.get('values', [])
    global Data
    Data = pd.DataFrame(values)

getting_data_from_responses_file()



#### cleaning Data
depression = Data[6].value_counts()
depression = depression.drop(['Depression Level'])
depression_labels = depression.index.tolist()
depression_values = depression.values.tolist()



#chart
layout = html.Div(children=[
    html.Div([

        html.Br(),
        html.Br(),

        html.H4('Pie Chart for Depression Data ', style={"textAlign": "center"}),

        dcc.Graph(
                id='graph1',
                figure=go.Figure(data=[go.Pie(labels=depression_labels, values=depression_values, hole=.3)])
            )
    ]),
])
















