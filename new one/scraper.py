import praw
import pandas as pd
from datetime import datetime, timedelta
from utils import time_period

class RedditScraper:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def scrape(self, crypto, subreddit, start_time, end_time):  # Update function parameters
        query = f"{crypto} subreddit:{subreddit}"

        return pd.DataFrame([{
            'title': post.title,
            'description': post.selftext,
            'created_utc': post.created_utc
        } for post in self.reddit.subreddit('all').search(query, time_filter='all') if start_time <= post.created_utc <= end_time])
