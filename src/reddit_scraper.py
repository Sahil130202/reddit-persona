# src/reddit_scraper.py

import praw
import os
from dotenv import load_dotenv

# Load API credentials from .env file
load_dotenv()

# Set up Reddit API client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def scrape_user_data(username, max_items=100):
    """
    Scrapes submissions and comments from a given Reddit user.

    Args:
        username (str): The Reddit username.
        max_items (int): Max number of posts and comments to fetch.

    Returns:
        (list, list): Two lists containing posts and comments.
    """
    posts, comments = [],[]

    try:
        user = reddit.redditor(username)

        # Scrape posts
        posts = [{
            "title": submission.title,
            "body": submission.selftext,
            "subreddit": str(submission.subreddit),
            "url": f"https://www.reddit.com{submission.permalink}"
        } for submission in user.submissions.new(limit=max_items)]

        # Scrape comments
        comments = [{
            "body": comment.body,
            "subreddit": str(comment.subreddit),
            "url": f"https://www.reddit.com{comment.permalink}"
        } for comment in user.comments.new(limit=max_items)]

    except Exception as e:
        print(f"Error scraping user {username}: {e}")

    return posts, comments
