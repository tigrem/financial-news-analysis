import pandas as pd
import os

def load_and_prepare_data(file_path):
    """Loads and prepares stock data from a CSV file."""
    try:
        df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
        df.columns = [col.capitalize() for col in df.columns]
        required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']

        if not all(col in df.columns for col in required_cols):
            print(f"Warning: Not all required OHLCV columns found in {os.path.basename(file_path)}.")
            print(f"Expected: {required_cols}, Found: {df.columns.tolist()}")
            column_mapping = {'Adj Close': 'Close', 'Adjclose': 'Close', 'Datetime': 'Date'}
            df.rename(columns=column_mapping, inplace=True)
            if not all(col in df.columns for col in required_cols):
                print("Attempted column mapping, but still missing required OHLCV columns. Please check your CSV column names.")
                for col in required_cols:
                    if col not in df.columns:
                        print(f"Creating dummy column for missing: {col}")
                        df[col] = df['Close']
                if 'Volume' not in df.columns:
                    df['Volume'] = 1000000

        df.sort_index(inplace=True)
        print(f"Data loaded successfully from {os.path.basename(file_path)}. First 5 rows:")
        print(df.head())
        print(f"DataFrame shape: {df.shape}")
        return df

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except KeyError as e:
        print(f"Error: Missing expected column in CSV '{os.path.basename(file_path)}': {e}. Please check your CSV headers.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading '{os.path.basename(file_path)}': {e}")
        return None
def load_stock_data(stock_data_dir, stock_data_files):
    stock_data = {}
    for file_name in stock_data_files:
        ticker = file_name.split('_')[0]
        file_path = os.path.join(stock_data_dir, file_name)
        try:
            df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
            df.columns = [col.capitalize() for col in df.columns]
            if 'Adj Close' in df.columns:
                df.rename(columns={'Adj Close': 'Close'}, inplace=True)
            elif 'Adjclose' in df.columns:
                df.rename(columns={'Adjclose': 'Close'}, inplace=True)
            stock_data[ticker] = df[['Close']]
            print(f"Loaded stock data for {ticker}: {df.shape}")
        except FileNotFoundError:
            print(f"Error: Stock data not found at {file_path}")
    print("\nStock data loading complete.")
    return stock_data
def load_news_data(news_file_path):
    try:
        news_df = pd.read_csv(news_file_path)
        news_df['date'] = pd.to_datetime(news_df['date'], format='mixed', utc=True)
        print(f"\nLoaded news data: {news_df.shape}")
        return news_df
    except FileNotFoundError:
        print(f"Error: News data not found at {news_file_path}")
        return None
if __name__ == '__main__':
    data_dir = '../data/'
    file_name = 'AAPL_historical_data.csv'
    file_path = os.path.join(data_dir, file_name)
    aapl_data = load_and_prepare_data(file_path)
    if aapl_data is not None:
        print("\nExample of loaded AAPL data:")
        print(aapl_data.head())