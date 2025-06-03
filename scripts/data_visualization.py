import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_stock_price_with_sma(df, title):
    """Plots the stock price with 20 and 50 day SMAs."""
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Close Price', color='blue', alpha=0.7)
    plt.plot(df['SMA_20'], label='SMA 20', color='red', alpha=0.7)
    plt.plot(df['SMA_50'], label='SMA 50', color='green', alpha=0.7)
    plt.title(f'Stock Price with Moving Averages for {title}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_rsi(df, title):
    """Plots the Relative Strength Index."""
    plt.figure(figsize=(14, 4))
    plt.plot(df['RSI'], label='RSI', color='purple', alpha=0.7)
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(f'Relative Strength Index (RSI) for {title}')
    plt.xlabel('Date')
    plt.ylabel('RSI Value')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_macd(df, title):
    """Plots the Moving Average Convergence Divergence."""
    plt.figure(figsize=(14, 6))
    plt.plot(df['MACD'], label='MACD', color='orange', alpha=0.7)
    plt.plot(df['MACD_Signal'], label='Signal Line', color='blue', alpha=0.7)
    plt.bar(df.index, df['MACD_Hist'], label='Histogram', color='gray', alpha=0.5)
    plt.axhline(0, color='black', linestyle='--')
    plt.title(f'MACD for {title}')
    plt.xlabel('Date')
    plt.ylabel('MACD Value')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
def plot_volatility(df, title):
    """Plots the volatility of the stock."""
    plt.figure(figsize=(14, 4))
    plt.plot(df['Volatility'], label='Volatility', color='red', alpha=0.7)
    plt.title(f'Volatility for {title}')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_daily_return(df, title):
    """Plots the daily return of the stock."""
    plt.figure(figsize=(14, 4))
    plt.plot(df['Daily_Return'], label='Daily Return', color='green', alpha=0.7)
    plt.title(f'Daily Return for {title}')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Example Usage (requires a DataFrame 'stock_data' with 'Close', 'SMA_20', 'SMA_50', 'RSI', 'MACD', 'MACD_Signal', 'MACD_Hist','Volatility', 'Daily_Return' columns)
    data = {'Close': [150, 152, 155, 153, 156],
            'SMA_20': [None, None, 152.3, 152.8, 153.5],
            'SMA_50': [None] * 5,
            'RSI': [None, None, 60, 55, 62],
            'MACD': [1, 1.2, 1.5, 1.3, 1.6],
            'MACD_Signal': [0.5, 0.7, 0.9, 1.0, 1.2],
            'MACD_Hist': [0.5, 0.5, 0.6, 0.3, 0.4],
            'Volatility': [0.02, 0.025, 0.022, 0.028, 0.026],
            'Daily_Return': [None, 0.013, 0.019, -0.013, 0.019]}
    example_df = pd.DataFrame(data)
    plot_stock_price_with_sma(example_df, "Sample Stock")
    plot_rsi(example_df, "Sample Stock")
    plot_macd(example_df, "Sample Stock")
    plot_volatility(example_df, "Sample Stock")
    plot_daily_return(example_df, "Sample Stock")