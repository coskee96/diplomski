from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from scraper import RedditScraper
from analyzer import SentimentAnalyzer
from utils import SUBREDDIT_OPTIONS, DURATION_OPTIONS, time_period

CLIENT_ID = "-pxbhNZKUNqZOR2Dn0yC9A"
SECRET_KEY = "I_m-vmYRzdohlzDm_Vg0D_cZLWIsdg"
USER_AGENT = "vts-project"

def register_callbacks(app):
    @app.callback(
        Output("sentiment-chart", "figure"),
        [Input("submit-button", "n_clicks")],
        [State("crypto-input", "value"),
        State("subreddit-dropdown", "value"),
        State("duration-dropdown", "value")],
        prevent_initial_call=True
    )
    def update_chart(n_clicks, crypto, subreddit, duration):
        start_time, end_time = time_period(duration)
        scraper = RedditScraper(CLIENT_ID, SECRET_KEY, USER_AGENT)
        data = scraper.scrape(crypto, subreddit, start_time, end_time)  # Modify the scrape function accordingly

        analyzer = SentimentAnalyzer(data)
        daily_sentiment = analyzer.analyze_sentiment(duration)  # Modify the analyze_sentiment function accordingly

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=daily_sentiment["created_utc"], y=daily_sentiment["sentiment"],  
            mode="lines+markers",
            name="Sentiment",
            line=dict(color="royalblue", width=2),
            connectgaps=True,
        ))

        if duration == '24h':
            xaxis_tickformat = '%H:%M'
        else:
            xaxis_tickformat = '%d/%m'

        fig.update_layout(title="Daily Average Sentiment",
            xaxis_title="Date", xaxis_tickformat=xaxis_tickformat,
            yaxis_title="Sentiment Score",
            font=dict(size=14),
            title_font=dict(size=22, color="darkblue"),
            xaxis_title_font=dict(size=16, color="darkblue"),
            yaxis_title_font=dict(size=16, color="darkblue")
        )


        return fig
