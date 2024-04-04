from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from .components.navbar import navbar
from .components.forecastform import forecast_form


index = html.Div([
    navbar,
    html.Div(id="main-view"),
    html.Div(
        forecast_form,
        style = {
            "position": "absolute",
            "bottom": '20px'
        },
    )
])