
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has
twelve columns.
There are three main layout components in dash-bootstrap-components: Container,
Row, and Col.
The layout of your app should be built as a series of rows of columns.
We set md=4 indicating that on a 'medium' sized or larger screen each column
should take up a third of the width. Since we don't specify behaviour on
smaller size screens Bootstrap will allow the rows to wrap so as not to squash
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Wealth concentration and economic policy

            Economic policy affects our ability to acquire wealth.

            Elected and appointed officials create economic policy.

            The bottom line is, if you care about money, then politics and policy matter.

            The good news is that diving into these topics might be easier and more interesting than you think!

            """
        ),
        dcc.Link(dbc.Button('Learn more', color='light'), href='/predictions')
    ],

    md=4,
)

column2  = dbc.Col(
        [
            html.Img(src='assets/top_1_1917_2014_wealth.png', className='img-fluid')
        ],

)
# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)
#
# column2 = dbc.Col(
#     [
#         dcc.Graph(figure=fig),
#     ]
# )

layout = dbc.Row([column1, column2])
