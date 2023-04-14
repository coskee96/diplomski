from dash import dcc, html
import dash_bootstrap_components as dbc
from utils import SUBREDDIT_OPTIONS, DURATION_OPTIONS

layout = dbc.Container([
    html.Div([
        html.H1("Crypto Sentiment Analyzer", className="text-center mt-4 mb-4 main-title")
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("Cryptocurrency:", className="mb-1 form-label"),
            dbc.Input(id="crypto-input", type="text", placeholder="Enter cryptocurrency", className="mb-4 form-dropdown")
        ], width=3),

        dbc.Col([
            html.Label("Subreddit:", className="mb-1 form-label"),
            dcc.Dropdown(id="subreddit-dropdown", options=SUBREDDIT_OPTIONS, value="", className="mb-4 form-dropdown")
        ], width=3),

        dbc.Col([
            html.Label("Duration:", className="mb-1 form-label"),
            dcc.Dropdown(id="duration-dropdown", options=DURATION_OPTIONS, value="day", className="mb-4 form-dropdown")
        ], width=3),

        dbc.Col([
            html.Button("Submit", id="submit-button", className="btn btn-primary mt-4 submit-button")
        ], width=3, className="d-flex justify-content-center")
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id="sentiment-chart")
        ], width=6),

        dbc.Col([
            dcc.Graph(id="average-sentiment-chart")
        ], width=6)
    ])
])

