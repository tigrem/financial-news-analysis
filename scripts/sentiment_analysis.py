import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(news_df):
    analyzer = SentimentIntensityAnalyzer()
    news_df['sentiment_score'] = news_df['headline'].apply(lambda headline: analyzer.polarity_scores(headline)['compound'])
    print("\nSentiment analysis complete. Sample with sentiment scores:")
    print(news_df[['date', 'headline', 'sentiment_score']].head())
    return news_df

def aggregate_daily_sentiment(news_df):
    daily_sentiment = news_df.groupby(news_df['date'].dt.date)['sentiment_score'].mean().reset_index()
    daily_sentiment.rename(columns={'date': 'Date', 'sentiment_score': 'avg_sentiment'}, inplace=True)
    daily_sentiment['Date'] = pd.to_datetime(daily_sentiment['Date'])
    daily_sentiment.set_index('Date', inplace=True)
    print("\nAggregated daily sentiment:")
    print(daily_sentiment.head())
    return daily_sentiment