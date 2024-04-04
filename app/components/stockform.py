from datetime import date, timedelta
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

stock_form = dbc.Row(
    [
        # Column for the ticker input
        dbc.Col(
            dbc.Input(placeholder="TICKR", id="tickr-input", className="mr-3"), 
            align="center", 
            width=3
        ),

        # Column for the date picker range
        dbc.Col(
            dcc.DatePickerRange(
                id='stock-date-picker-range',
                min_date_allowed=(date.today() - timedelta(days=3*365)),
                max_date_allowed=date.today(),
                initial_visible_month=date.today()
            )
        ),
        
        # Column for the filter button
        dbc.Col(
            dbc.Button("Filter", color="primary", id="form-submit"), 
            width=3, 
            align="center"
        ),
    ],
    className="ml-auto flex-nowrap mt-md-0",
    align="end",
)