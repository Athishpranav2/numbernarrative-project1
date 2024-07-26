import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data from the CSV file
df = pd.read_csv('/Users/athishpravav/Desktop/New Folder/biden_reddit_sentiment_with_timestamps.csv')

# Convert 'timestamp' to datetime and set as index
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Define a negative sentiment threshold
negative_threshold = -0.1  # Adjust this threshold based on your sentiment analysis range

# Filter negative sentiment comments
negative_comments = df[df['compound'] <= negative_threshold]

# Count negative comments by day
negative_comments_count = negative_comments.resample('D').size()

# Filter data from January to July 2024
negative_comments_count = negative_comments_count.loc['2024-01-01':'2024-07-31']

# Set Seaborn style
sns.set(style='whitegrid')

# Create the plot
plt.figure(figsize=(14, 8))
plt.plot(negative_comments_count.index, negative_comments_count, marker='o', linestyle='-', color='r', label='Negative Comments Frequency')
plt.title('Frequency of Negative Sentiments from January to July 2024', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Negative Comments', fontsize=14)

# Add a trend line
sns.regplot(x=negative_comments_count.index.astype(int), y=negative_comments_count, scatter=False, color='blue', label='Trend Line')

# Add grid, legend, and rotate x-axis labels
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)
plt.xticks(rotation=45)

# Highlight a specific period (e.g., March 2024)
plt.axvspan(pd.to_datetime('2024-03-01'), pd.to_datetime('2024-03-31'), color='yellow', alpha=0.3, label='March 2024')

# Add annotations
plt.annotate('Spike in negative comments', xy=('2024-03-15', negative_comments_count['2024-03-15']),
             xytext=('2024-02-15', max(negative_comments_count)+5),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Final layout adjustments
plt.tight_layout()

# Show plot
plt.show()
