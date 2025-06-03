import talib
import pandas as pd

def calculate_technical_indicators(df):
    """Calculates common technical indicators."""
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    macd, macdsignal, macdhist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['MACD'] = macd
    df['MACD_Signal'] = macdsignal
    df['MACD_Hist'] = macdhist
    return df

def calculate_financial_metrics(df):
    """Calculates basic financial metrics."""
    df['Daily_Return'] = df['Close'].pct_change()
    df['Volatility'] = df['Daily_Return'].rolling(window=20).std() * (252**0.5)
    return df
def calculate_correlations(stock_data, daily_sentiment):
    correlation_results = {}
    for ticker, df in stock_data.items():
        if df is not None and daily_sentiment is not None:
            df['Daily_Return'] = df['Close'].pct_change()
            merged_df = pd.merge(df[['Daily_Return']], daily_sentiment, left_index=True, right_index=True, how='inner')
            correlation = merged_df['Daily_Return'].corr(merged_df['avg_sentiment'])
            correlation_results[ticker] = correlation
            print(f"\nCorrelation between news sentiment and {ticker} daily return: {correlation:.4f}")
    print("\nCorrelation analysis complete.")
    return correlation_results
if __name__ == '__main__':
    # Example usage (requires a DataFrame named 'stock_data')
    data = {'Close': [150, 152, 155, 153, 156]}
    stock_data = pd.DataFrame(data)
    indicators_df = calculate_technical_indicators(stock_data.copy())
    metrics_df = calculate_financial_metrics(stock_data.copy())
    print("Example Indicators:")
    print(indicators_df)
    print("\nExample Metrics:")
    print(metrics_df)