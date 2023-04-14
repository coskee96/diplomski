import pandas as pd
import numpy as np
from textblob import TextBlob
from utils import sentiment_category, time_period

class SentimentAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze_sentiment(self, duration):  # Update function parameters
        self.data['sentiment'] = self.data.apply(lambda x: TextBlob(x['title'] + ' ' + x['description']).sentiment.polarity, axis=1)
        self.data['sentiment'] = self.data['sentiment'].apply(lambda x: (x + 1) * 50)
        self.data['sentiment_category'] = self.data['sentiment'].apply(sentiment_category)
        self.data['created_utc'] = pd.to_datetime(self.data['created_utc'], unit='s').dt.date

        if duration == '24h':
            interval = 'H'
        else:
            interval = 'D'

    # Convert the 'created_utc' column to a DatetimeIndex
        self.data.set_index('created_utc', inplace=True)
        self.data.index = pd.to_datetime(self.data.index)

        return self.data.resample(interval)['sentiment'].mean().reset_index()

