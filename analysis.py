import pandas as pd
import plotly.graph_objects as go

# Load your data from the CSV file
df = pd.read_csv('/Users/athishpravav/Desktop/New Folder/biden_reddit_sentiment_with_timestamps.csv')

# Convert 'timestamp' to datetime and set as index
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Ensure 'compound' and other sentiment columns are numeric
df['compound'] = pd.to_numeric(df['compound'], errors='coerce')
df['positive'] = pd.to_numeric(df['positive'], errors='coerce')
df['neutral'] = pd.to_numeric(df['neutral'], errors='coerce')
df['negative'] = pd.to_numeric(df['negative'], errors='coerce')

# Calculate daily average sentiment score
daily_sentiment = df[['compound']].resample('D').mean()

# Filter data from January to July 2024
daily_sentiment = daily_sentiment.loc['2024-01-01':'2024-07-31']

# Create an interactive plot
fig = go.Figure()

# Add a trace for daily average sentiment
fig.add_trace(go.Scatter(x=daily_sentiment.index,
                         y=daily_sentiment['compound'],
                         mode='lines+markers',
                         name='Daily Average Sentiment',
                         marker=dict(color='blue'),
                         line=dict(width=2),
                         text=daily_sentiment.index.strftime('%Y-%m-%d'),
                         hoverinfo='text+y'))

# Update layout
fig.update_layout(title='Daily Average Sentiment Score from January to July 2024',
                  xaxis_title='Date',
                  yaxis_title='Average Sentiment Score',
                  xaxis=dict(
                      rangeselector=dict(
                          buttons=[
                              dict(count=1, step='month', stepmode='backward'),
                              dict(count=6, step='month', stepmode='backward'),
                              dict(step='all')
                          ],
                          visible=True
                      ),
                      rangeslider=dict(visible=True),  # Rangeslider should be directly under xaxis
                      type='date'
                  ),
                  yaxis=dict(title='Average Sentiment Score'),
                  hovermode='closest')

# Show plot
fig.show()
