import dash

app = dash.Dash(__name__,suppress_callback_exceptions = True,
                meta_tags = [{'name':'viewport',
                              'content':'widrh=device-width, initial-scale=1.0'}])


server = app.server