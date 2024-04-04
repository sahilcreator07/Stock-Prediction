import dash_bootstrap_components as dbc
from dash import html

from .plot import generate_forecast_graph

def get_forecast_detail(accuracy, graph):
    forecast_detail = dbc.Col(
        dbc.Container([
            dbc.Row(html.H3("Error Margin: {}".format(accuracy)), align='center', className="g-0"),
            generate_forecast_graph(graph)
        ]),
        align="center"
    )
    return forecast_detail