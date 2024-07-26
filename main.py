import praw
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime

reddit = praw.Reddit(
    client_id='xmvjtCe-MMyv3w4vklpCNw',
    client_secret='qg4MRLXt0zN3gUQG52rFaX66EWWY1A',
    user_agent='my-app by u/m_runthat',
    username='Otherwise-Village812',
    password='Athish@2408'
)

search_term = 'Joe Biden'
subreddit_name = 'politics'

# Fetch posts from the subreddit
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.search(search_term, limit=100)

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Create a list to store results
results = []

# Fetch comments and analyze sentiment
for post in posts:
    post.comments.replace_more(limit=0)
    for comment in post.comments.list():
        sentiment = analyzer.polarity_scores(comment.body)
        timestamp = datetime.fromtimestamp(comment.created_utc)
        results.append({
            'post_id': post.id,
            'comment_id': comment.id,
            'comment': comment.body,
            'timestamp': timestamp,
            'compound': sentiment['compound'],
            'positive': sentiment['pos'],
            'neutral': sentiment['neu'],
            'negative': sentiment['neg']
        })

# Convert results to a DataFrame
df = pd.DataFrame(results)

# Save to a CSV file
df.to_csv('biden_reddit_sentiment_with_timestamps.csv', index=False)

print(df.head())
