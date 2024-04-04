import dash_bootstrap_components as dbc
from dash import html

def generate_ticker_details(
    info: dict
): 
    ticker_detail = dbc.Col(
        dbc.Container([
            dbc.Row([
                dbc.Col(html.Img(src=info["logo_url"], height="75px", width="75px"), width=2, align="center"),
                dbc.Col(html.H2(info["name"], className="display-3"), width=10),
            ],
            className="g-0"
            ),
            dbc.Row(
                dbc.Col(html.P(html.Small(info["description"])))
            ),
            dbc.Row([
                dbc.Col(html.P(info["city"], className="text-muted")),
                dbc.Col(html.P(info["state"], className="text-muted")),
                dbc.Col(html.P(info["country"], className="text-muted")),
            ])],
        ),
        width=5,
        align="center"
    )

    return ticker_detail