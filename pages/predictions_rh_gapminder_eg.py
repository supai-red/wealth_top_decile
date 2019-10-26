# Import from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
import pandas as pd

# Imports from this app
from app import app

# Load pipeline
from joblib import load
pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown('##P Predictions', className='mb-5'),
        dcc.Markdown('#### Year'),
        dcc.Slider(
            id='year',
            min=1955,
            max=2055,
            step=5,
            value=2020,
            marks={n: str(n) for n in range(1960,2060,20)},
            className='mb-5',
        ),
        dcc.Markdown('#### Continent'),
        dcc.Dropdown(
            id='continent',
            options = [
                {'label': 'Africa', 'value': 'Africa'},
                {'label': 'Americas', 'value': 'Americas'},
                {'label': 'Asia', 'value': 'Asia'},
                {'label': 'Europe', 'value': 'Europe'},
                {'label': 'Oceania', 'value': 'Oceania'},
            ],
            value = 'Africa',
            className='mb-5',

        ),
    #     daq.Slider(
    #       id='slider1',
    #       targets={"25": {"label": "TARGET"}},
    #       min=0, max=100, value=100,
    #       marks={'0': '0',
    #             '25': '25',
    #             '50': '50',
    #             '75': '75',
    #             '100': '100'},
    #     className='mb=10',
    #     ),
    #
    #     dcc.Markdown(id='out1')
    #     #("here's some more text and a link to [google](google.com)", id='out1')
    ],
    md=4,
)

column2 = dbc.Col(
    [

    html.H2('Expected Lifespan', className='mb-5'),
    html.Div(id='prediction-content', className='lead')
#     daq.Gauge(
#   id='my-daq-gauge',
#   max=100,
#   value=20,
#   min=0
# )

    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('year', 'value'), Input('continent', 'value')],
)
def predict(year, continent):
    df = pd.DataFrame(
        columns=['year', 'continent'],
        data=[[year, continent]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f} years'

# @app.callback(
#     Output(component_id='my-daq-gauge', component_property='value'),
#     [Input(component_id='slider1', component_property='value')]
# )
# def update_output_div(input_value):
#     return input_value
