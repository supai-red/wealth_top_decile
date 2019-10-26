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
pipeline = load('assets/pipeline3.joblib')

column1 = dbc.Col(
    [
        html.Img(src='assets/capital_income_ratio_1917_2014.png', className='img-fluid'),
        dcc.Markdown('#### Year')
    ],

    md = 4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('#### Predictions', className='mb-5'),
        dcc.Markdown('#### Income of top decile', className='mb=5'),
        daq.Slider(min=0.3, max=.5, step=0.2,
                marks={.3: '30%', .35: '35', .40: '40', .45: '45', .50: '50%'}
            )

    ],

    md = 4,
)

column3 = dbc.Col(
    [
        dcc.Markdown('#### Capital/Income Ratio', className='mb=5'),
        daq.Slider(
                 min=2, max=7, step=0.5,
                 marks={2: '2', 2.5: '2.5', 3: '3', 3.5: '3.5',
                 4: '4', 4.5: '4.5', 5: '5', 5.5: '5.5', 6: '6',
                 6.5: '6.5', 7: '7'}
                 )

    ],

    md = 4,
)

layout = dbc.Row([column1, column2, column3])